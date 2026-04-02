#!/usr/bin/env python3
"""
Docgen HTTP Server
Wraps CLI backend with REST API for widget communication
"""

import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

try:
    from flask import Flask, request, jsonify
except ImportError:
    print("Installing Flask...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'flask', 'python-dotenv'])
    from flask import Flask, request, jsonify

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add code directory to path
import sys
sys.path.insert(0, str(Path(__file__).parent / "code"))

from generators.base_generator import get_generator
from gates.validator import QualityGateValidator
from destinations.zip_handler import ZipHandler

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Initialize components
validator = QualityGateValidator()
zip_handler = ZipHandler(output_dir="output")


class DocgenAPI:
    """Docgen API handler"""
    
    def __init__(self):
        self.generation_log = []
    
    def generate(self, project_id: int, answers: Dict[str, str], 
                destinations: list) -> Dict[str, Any]:
        """Main generation endpoint"""
        
        try:
            logger.info(f"Generating: Project {project_id}, Destinations: {destinations}")
            
            # Step 1: Generate document
            logger.info("Step 1: Generating document...")
            generator = get_generator(project_id)
            result = generator.generate(answers)
            logger.info(f"✓ Generated: {result['filename']}")
            
            # Step 2: Run quality gates
            logger.info("Step 2: Running quality gates...")
            gates_result = validator.validate_all(
                document=result['content'],
                doc_type=result['metadata']['category']
            )
            
            if gates_result['status'] != 'PRODUCTION_READY':
                logger.warning(f"Quality gate failed: {gates_result['failures']}")
                return {
                    'status': 'FAILED',
                    'error': 'Quality gate validation failed',
                    'details': gates_result['failures'],
                    'quality_score': gates_result['quality_score']
                }
            
            logger.info(f"✓ Quality score: {gates_result['quality_score']}/100")
            
            # Add gates metadata to document
            doc_with_gates = {
                'filename': result['filename'],
                'content': result['content'],
                'metadata': {
                    **result['metadata'],
                    **gates_result
                }
            }
            
            # Step 3: Deliver to destinations
            logger.info("Step 3: Delivering to destinations...")
            delivery_report = {}
            
            if 'zip' in destinations:
                try:
                    logger.info("  → Zip delivery...")
                    zip_path = zip_handler.create_zip([doc_with_gates])
                    delivery_report['zip'] = {
                        'status': 'SUCCESS',
                        'path': str(zip_path)
                    }
                    logger.info(f"  ✓ Zip created: {zip_path}")
                except Exception as e:
                    logger.error(f"  ✗ Zip failed: {e}")
                    delivery_report['zip'] = {
                        'status': 'FAILED',
                        'error': str(e)
                    }
            
            # Log generation
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'project_id': project_id,
                'status': 'SUCCESS',
                'quality_score': gates_result['quality_score'],
                'destinations': destinations
            }
            self.generation_log.append(log_entry)
            
            logger.info("✅ Generation complete")
            
            return {
                'status': 'SUCCESS',
                'document': {
                    'filename': result['filename'],
                    'word_count': result['metadata']['word_count'],
                    'tokens': result['metadata']['token_estimate']
                },
                'quality': {
                    'score': gates_result['quality_score'],
                    'status': gates_result['status'],
                    'gates_passed': gates_result['passed_gates']
                },
                'delivery': delivery_report,
                'generation_id': len(self.generation_log)
            }
        
        except Exception as e:
            logger.error(f"Generation failed: {e}", exc_info=True)
            return {
                'status': 'ERROR',
                'error': str(e),
                'message': 'An unexpected error occurred during generation'
            }


# Initialize API
api = DocgenAPI()


# Routes
@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0'
    })


@app.route('/api/docgen/generate', methods=['POST'])
def generate_docs():
    """Main generation endpoint"""
    
    try:
        # Parse request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'status': 'ERROR',
                'error': 'No JSON data provided'
            }), 400
        
        # Validate required fields
        required_fields = ['project', 'answers', 'destinations']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'status': 'ERROR',
                    'error': f'Missing required field: {field}'
                }), 400
        
        project_id = int(data['project'])
        answers = data['answers']
        destinations = data['destinations']
        
        # Validate project ID
        if project_id < 1 or project_id > 10:
            return jsonify({
                'status': 'ERROR',
                'error': f'Invalid project ID: {project_id} (must be 1-10)'
            }), 400
        
        # Validate destinations
        valid_destinations = ['zip', 'github', 'notion', 'drive', 'email']
        for dest in destinations:
            if dest not in valid_destinations:
                return jsonify({
                    'status': 'ERROR',
                    'error': f'Invalid destination: {dest}'
                }), 400
        
        # Generate
        result = api.generate(project_id, answers, destinations)
        
        status_code = 200 if result['status'] == 'SUCCESS' else 400
        return jsonify(result), status_code
    
    except json.JSONDecodeError:
        return jsonify({
            'status': 'ERROR',
            'error': 'Invalid JSON format'
        }), 400
    
    except ValueError as e:
        return jsonify({
            'status': 'ERROR',
            'error': f'Invalid data format: {str(e)}'
        }), 400


@app.route('/api/docgen/status', methods=['GET'])
def status():
    """Get generation status and logs"""
    
    generation_id = request.args.get('id', type=int)
    
    if generation_id:
        if 0 < generation_id <= len(api.generation_log):
            return jsonify({
                'status': 'found',
                'generation': api.generation_log[generation_id - 1]
            })
        else:
            return jsonify({
                'status': 'not_found',
                'error': f'Generation ID {generation_id} not found'
            }), 404
    
    # Return recent logs
    recent_logs = api.generation_log[-10:]  # Last 10
    return jsonify({
        'status': 'ok',
        'total_generations': len(api.generation_log),
        'recent': recent_logs
    })


@app.route('/api/docgen/projects', methods=['GET'])
def list_projects():
    """List all available projects"""
    
    projects = [
        {'id': 1, 'name': 'Fast Product MVP', 'time': '2h', 'questions': 7},
        {'id': 2, 'name': 'Feature Release', 'time': '2.5h', 'questions': 8},
        {'id': 3, 'name': 'Workflow Automation', 'time': '2h', 'questions': 6},
        {'id': 4, 'name': 'Revenue Stream', 'time': '1.5h', 'questions': 6},
        {'id': 5, 'name': 'Brand Marketing', 'time': '2h', 'questions': 7},
        {'id': 6, 'name': 'Product Marketing', 'time': '2.5h', 'questions': 8},
        {'id': 7, 'name': 'Summarize Files', 'time': '30m', 'questions': 3},
        {'id': 8, 'name': 'Custom Docs', 'time': 'Variable', 'questions': 5},
        {'id': 9, 'name': 'AI Skill', 'time': '1.5h', 'questions': 7},
        {'id': 10, 'name': 'Claude Project', 'time': '2h', 'questions': 8}
    ]
    
    return jsonify({
        'status': 'ok',
        'projects': projects,
        'total': len(projects)
    })


@app.route('/api/docgen/validate', methods=['POST'])
def validate_document():
    """Validate a document against quality gates"""
    
    try:
        data = request.get_json()
        
        if not data or 'content' not in data or 'category' not in data:
            return jsonify({
                'status': 'ERROR',
                'error': 'Missing required fields: content, category'
            }), 400
        
        content = data['content']
        category = data['category']
        
        # Run gates
        gates_result = validator.validate_all(content, category)
        
        return jsonify({
            'status': 'ok',
            'validation': gates_result,
            'production_ready': gates_result['status'] == 'PRODUCTION_READY'
        })
    
    except Exception as e:
        logger.error(f"Validation failed: {e}", exc_info=True)
        return jsonify({
            'status': 'ERROR',
            'error': str(e)
        }), 500


@app.route('/api/docgen/info', methods=['GET'])
def info():
    """Get API information"""
    
    return jsonify({
        'name': 'Docgen API',
        'version': '1.0',
        'status': 'operational',
        'endpoints': {
            'POST /api/docgen/generate': 'Generate documentation',
            'GET /api/docgen/projects': 'List available projects',
            'GET /api/docgen/status': 'Get generation status',
            'POST /api/docgen/validate': 'Validate document',
            'GET /health': 'Health check'
        },
        'generations_count': len(api.generation_log)
    })


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'ERROR',
        'error': 'Endpoint not found',
        'path': request.path
    }), 404


@app.errorhandler(500)
def server_error(error):
    logger.error(f"Server error: {error}", exc_info=True)
    return jsonify({
        'status': 'ERROR',
        'error': 'Internal server error'
    }), 500


def main():
    """Run the server"""
    
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Docgen API server on port {port}")
    logger.info(f"Debug mode: {debug}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug,
        use_reloader=False
    )


if __name__ == '__main__':
    main()
