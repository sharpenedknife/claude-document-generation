#!/usr/bin/env python3
"""
Docgen CLI - Generate production-ready documentation
Usage: python cli.py generate --project 1 --answers answers.json --destinations zip,github
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generators.base_generator import get_generator
from gates.validator import QualityGateValidator
from destinations.zip_handler import ZipHandler
from destinations.github_handler import GitHubHandler
from destinations.notion_handler import NotionHandler
from destinations.drive_handler import GoogleDriveHandler


class DocgenCLI:
    def __init__(self):
        self.validator = QualityGateValidator()
        self.generated_docs = []
        self.delivery_report = {}
    
    def generate(self, project_id: int, answers: dict, destinations: list) -> dict:
        """Main generation pipeline"""
        
        print(f"🚀 Docgen: Generating documentation")
        print(f"   Project: {project_id}")
        print(f"   Destinations: {', '.join(destinations)}")
        print()
        
        # Step 1: Generate document
        print("⏳ Step 1: Generating document...")
        generator = get_generator(project_id)
        result = generator.generate(answers)
        
        print(f"   ✓ Generated: {result['filename']}")
        print(f"   ✓ Content: {result['metadata']['word_count']} words")
        
        # Step 2: Run quality gates
        print()
        print("⏳ Step 2: Running quality gates...")
        
        gates_result = self.validator.validate_all(
            document=result['content'],
            doc_type=result['metadata']['category']
        )
        
        if gates_result['status'] == 'PRODUCTION_READY':
            print(f"   ✓ Gate 1 (Validation): PASS")
            print(f"   ✓ Gate 2 (Structure): PASS")
            print(f"   ✓ Gate 3 (Content): PASS")
            print(f"   ✓ Gate 4 (Metrics): PASS ({gates_result['quality_score']}/100)")
            print(f"   ✓ Gate 5 (Shipping): PASS - {gates_result['status']}")
        else:
            print(f"   ✗ Quality check failed: {gates_result['failures']}")
            return {
                'status': 'FAILED',
                'error': gates_result['failures'],
                'docs': []
            }
        
        # Store generated document
        self.generated_docs.append({
            'filename': result['filename'],
            'content': result['content'],
            'metadata': {**result['metadata'], **gates_result}
        })
        
        # Step 3: Deliver to destinations
        print()
        print("⏳ Step 3: Delivering to destinations...")
        
        for destination in destinations:
            print(f"   → {destination}...", end=' ', flush=True)
            try:
                if destination == 'zip':
                    handler = ZipHandler()
                    link = handler.create_zip(self.generated_docs)
                    self.delivery_report['zip'] = {'status': 'SUCCESS', 'link': link}
                    print("✓")
                
                elif destination == 'github':
                    handler = GitHubHandler()
                    link = handler.push(self.generated_docs)
                    self.delivery_report['github'] = {'status': 'SUCCESS', 'link': link}
                    print("✓")
                
                elif destination == 'notion':
                    handler = NotionHandler()
                    link = handler.create_pages(self.generated_docs)
                    self.delivery_report['notion'] = {'status': 'SUCCESS', 'link': link}
                    print("✓")
                
                elif destination == 'drive':
                    handler = GoogleDriveHandler()
                    link = handler.upload(self.generated_docs)
                    self.delivery_report['drive'] = {'status': 'SUCCESS', 'link': link}
                    print("✓")
                
            except Exception as e:
                self.delivery_report[destination] = {'status': 'FAILED', 'error': str(e)}
                print(f"✗ ({e})")
        
        # Step 4: Return summary
        print()
        print("✅ Complete!")
        print()
        print("📊 Summary:")
        print(f"   Documents generated: {len(self.generated_docs)}")
        print(f"   Quality score: {gates_result['quality_score']}/100")
        print(f"   Status: {gates_result['status']}")
        print()
        print("📍 Available at:")
        for dest, report in self.delivery_report.items():
            if report['status'] == 'SUCCESS':
                print(f"   • {dest}: {report['link']}")
        
        return {
            'status': 'SUCCESS',
            'docs': self.generated_docs,
            'delivery': self.delivery_report,
            'quality_score': gates_result['quality_score']
        }


def main():
    parser = argparse.ArgumentParser(description='Docgen: Generate documentation')
    parser.add_argument('command', choices=['generate'], help='Command to run')
    parser.add_argument('--project', type=int, required=True, help='Project ID (1-10)')
    parser.add_argument('--answers', type=str, required=True, help='JSON file with answers')
    parser.add_argument('--destinations', type=str, required=True, 
                       help='Comma-separated: zip,github,notion,drive')
    
    args = parser.parse_args()
    
    if args.command == 'generate':
        # Load answers
        with open(args.answers, 'r') as f:
            answers = json.load(f)
        
        # Parse destinations
        destinations = [d.strip() for d in args.destinations.split(',')]
        
        # Run generation
        cli = DocgenCLI()
        result = cli.generate(args.project, answers, destinations)
        
        # Exit with appropriate code
        sys.exit(0 if result['status'] == 'SUCCESS' else 1)


if __name__ == '__main__':
    main()
