"""
Quality Gate Validator
All documents must pass 5 gates before shipping
"""

import re
import json
from typing import Dict, List, Any


class QualityGateValidator:
    """
    5 Quality Gates:
    1. Validation - YAML, metadata, structure
    2. Structure - Required sections present
    3. Content - Clarity, accuracy, examples
    4. Metrics - Token budget, quality score
    5. Shipping - Ready for production
    """
    
    def __init__(self):
        self.required_yaml_fields = [
            'title', 'description', 'version', 'date', 'author', 'category', 'status', 'tags'
        ]
        self.required_sections = {
            'Product': ['Overview', 'Prerequisites', 'Problem Statement', 'Solution Overview', 
                       'Success Metrics', 'Acceptance Criteria', 'Why This Matters', "What's Next"],
            'Design': ['Overview', 'Prerequisites', 'User Journeys', 'Wireframe Descriptions',
                      'Interaction Patterns', 'Accessibility', 'Why This Matters', "What's Next"],
            'Engineering': ['Overview', 'Prerequisites', 'Architecture', 'API Endpoints',
                           'Performance', 'Security', 'Why This Matters', "What's Next"],
            'Business': ['Overview', 'Prerequisites', 'Target Customer', 'Pricing', 
                        'Revenue Model', 'Projections', 'Why This Matters', "What's Next"],
            'Skill': ['Overview', 'When to Use', 'Capabilities', 'Examples',
                     'Implementation Guide', 'Why This Matters', "What's Next"],
            'Project': ['System Message', 'Capabilities', 'Tools', 'Memory System',
                       'Example Interactions', 'Why This Matters'],
            'Analysis': ['Overview', 'Key Findings', 'Recommendations', 'Gaps',
                        'Implementation Readiness', 'Why This Matters', "What's Next"],
            'Custom': ['Overview', 'Prerequisites', 'Why This Matters', "What's Next"]
        }
        self.token_budgets = {
            'Product': 3000,
            'Design': 2500,
            'Engineering': 2500,
            'Business': 2000,
            'Skill': 1500,
            'Project': 3000,
            'Analysis': 1500,
            'Custom': 2500
        }
    
    def gate_1_validation(self, document: str) -> tuple[bool, List[str]]:
        """Gate 1: Validate YAML frontmatter and metadata"""
        errors = []
        
        # Check for YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---', document, re.DOTALL)
        if not yaml_match:
            errors.append("Missing YAML frontmatter (---...---)")
            return False, errors
        
        yaml_content = yaml_match.group(1)
        
        # Check for required fields
        for field in self.required_yaml_fields:
            if f'{field}:' not in yaml_content:
                errors.append(f"Missing YAML field: {field}")
        
        # Check status field
        if 'status: PRODUCTION_READY' not in yaml_content:
            errors.append("Status must be PRODUCTION_READY")
        
        return len(errors) == 0, errors
    
    def gate_2_structure(self, document: str, category: str) -> tuple[bool, List[str]]:
        """Gate 2: Validate document structure and sections"""
        errors = []
        
        required = self.required_sections.get(category, self.required_sections['Custom'])
        
        # Check each required section exists
        for section in required:
            # Check for markdown heading (## Section Name)
            section_pattern = rf'^## {re.escape(section)}'
            if not re.search(section_pattern, document, re.MULTILINE):
                errors.append(f"Missing section: {section}")
        
        # Check for overview (typically 1-2 sentences)
        overview_match = re.search(r'## Overview\n\n(.+?)(?:\n## |\Z)', document, re.DOTALL)
        if overview_match:
            overview = overview_match.group(1).strip()
            sentences = len(re.split(r'[.!?]+', overview.strip())) - 1
            if sentences > 3:
                errors.append(f"Overview too long ({sentences} sentences, max 2-3)")
        
        # Check for expected output table
        if '| ' not in document:
            errors.append("Missing expected output table")
        
        return len(errors) == 0, errors
    
    def gate_3_content(self, document: str) -> tuple[bool, List[str]]:
        """Gate 3: Validate content quality and clarity"""
        errors = []
        
        # Check for vague language
        vague_phrases = [
            r'\bensure quality\b',
            r'\bmake sure everything\b',
            r'\bconfigure properly\b',
            r'\bdo the right thing\b',
            r'\bas needed\b',
            r'\bas appropriate\b',
            r'\bif necessary\b',
            r'\betc\b',
            r'\byou should\b',
            r'\bneed to\b'
        ]
        
        for phrase in vague_phrases:
            if re.search(phrase, document, re.IGNORECASE):
                errors.append(f"Vague language found: '{phrase}' - be specific")
        
        # Check for examples
        if 'Example' not in document and 'example' not in document:
            errors.append("No examples provided - include at least 3")
        
        # Check for links/references
        internal_links = re.findall(r'\[.*?\]\(#.*?\)', document)
        if len(internal_links) < 2:
            errors.append("Few cross-references - link related sections")
        
        # Check formatting
        if document.count('```') < 1:
            errors.append("Consider including code blocks or structured examples")
        
        return len(errors) == 0, errors
    
    def gate_4_metrics(self, document: str, category: str) -> tuple[bool, Dict[str, Any]]:
        """Gate 4: Check token budget and quality metrics"""
        errors = []
        metrics = {}
        
        # Estimate tokens (rough: 1 token ≈ 4 characters)
        token_estimate = len(document) / 4
        budget = self.token_budgets.get(category, 2500)
        
        metrics['tokens'] = int(token_estimate)
        metrics['budget'] = budget
        metrics['token_ratio'] = token_estimate / budget
        
        if token_estimate > budget:
            errors.append(f"Exceeds token budget ({int(token_estimate)} > {budget})")
        
        # Quality scoring (0-100)
        quality_score = 100
        
        # Deduct for issues
        if len(document) < 1000:
            quality_score -= 10  # Too short
        if document.count('\n##') < 4:
            quality_score -= 10  # Too few sections
        if not re.search(r'\| .+ \|', document):
            quality_score -= 10  # No tables
        if quality_score < 80:
            errors.append(f"Quality score too low ({quality_score}/100, min 80)")
        
        metrics['quality_score'] = max(0, quality_score)
        
        return len(errors) == 0, errors, metrics
    
    def gate_5_shipping(self, gate_results: Dict[str, Any]) -> tuple[bool, str]:
        """Gate 5: All gates pass = PRODUCTION_READY"""
        
        all_passed = (
            gate_results['gate_1'] and
            gate_results['gate_2'] and
            gate_results['gate_3'] and
            gate_results['gate_4']['pass']
        )
        
        status = 'PRODUCTION_READY' if all_passed else 'NEEDS_REVIEW'
        
        return all_passed, status
    
    def validate_all(self, document: str, doc_type: str) -> Dict[str, Any]:
        """Run all 5 gates and return comprehensive report"""
        
        # Run all gates
        gate_1_pass, gate_1_errors = self.gate_1_validation(document)
        gate_2_pass, gate_2_errors = self.gate_2_structure(document, doc_type)
        gate_3_pass, gate_3_errors = self.gate_3_content(document)
        gate_4_pass, gate_4_errors, gate_4_metrics = self.gate_4_metrics(document, doc_type)
        
        # Compile results
        results = {
            'gate_1_validation': gate_1_pass,
            'gate_1_errors': gate_1_errors,
            'gate_2_structure': gate_2_pass,
            'gate_2_errors': gate_2_errors,
            'gate_3_content': gate_3_pass,
            'gate_3_errors': gate_3_errors,
            'gate_4': {
                'pass': gate_4_pass,
                'errors': gate_4_errors,
                'metrics': gate_4_metrics
            },
            'quality_score': gate_4_metrics.get('quality_score', 0),
        }
        
        # Gate 5
        gate_5_pass, status = self.gate_5_shipping({
            'gate_1': gate_1_pass,
            'gate_2': gate_2_pass,
            'gate_3': gate_3_pass,
            'gate_4': results['gate_4']
        })
        
        results['gate_5_shipping'] = gate_5_pass
        results['status'] = status
        
        # Compile all failures
        all_failures = []
        if gate_1_errors:
            all_failures.extend(gate_1_errors)
        if gate_2_errors:
            all_failures.extend(gate_2_errors)
        if gate_3_errors:
            all_failures.extend(gate_3_errors)
        if gate_4_errors:
            all_failures.extend(gate_4_errors)
        
        results['failures'] = all_failures
        results['passed_gates'] = sum([gate_1_pass, gate_2_pass, gate_3_pass, gate_4_pass, gate_5_pass])
        
        return results
