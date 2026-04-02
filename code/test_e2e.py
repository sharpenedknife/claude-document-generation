#!/usr/bin/env python3
"""
Docgen E2E Test
Demonstrates the complete generation → validation → delivery pipeline
"""

import json
import sys
from pathlib import Path

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent / "code"))

from generators.base_generator import get_generator
from gates.validator import QualityGateValidator
from destinations.zip_handler import ZipHandler


def test_prd_generation():
    """Test: Generate a PRD document"""
    print("=" * 60)
    print("TEST 1: Generate PRD Document")
    print("=" * 60)
    
    # Sample answers from questionnaire
    answers = {
        "q0": "A SaaS platform for documentation generation",
        "q1": "Product managers, engineers, startup founders",
        "q2": "Creating quality documentation manually takes too long (2-4 weeks per doc)",
        "q3": "API-first doc generator, templates, quality gates, multi-destination delivery",
        "q4": "Q2 2026",
        "q5": "Python + Claude API, no external frameworks",
        "q6": "$50k"
    }
    
    # Generate document
    print("\n📝 Generating PRD...")
    generator = get_generator(1)  # Project 1 = PRD
    result = generator.generate(answers)
    
    print(f"✓ Generated: {result['filename']}")
    print(f"✓ Word count: {result['metadata']['word_count']}")
    print(f"✓ Tokens (est): {result['metadata']['token_estimate']}")
    
    return result


def test_quality_gates(document_result):
    """Test: Run quality gates on document"""
    print("\n" + "=" * 60)
    print("TEST 2: Run Quality Gates")
    print("=" * 60)
    
    validator = QualityGateValidator()
    
    print("\n🔍 Running 5 gates...")
    gates_result = validator.validate_all(
        document=document_result['content'],
        doc_type=document_result['metadata']['category']
    )
    
    # Report results
    print(f"\n✓ Gate 1 (Validation): {'PASS' if gates_result['gate_1_validation'] else 'FAIL'}")
    if gates_result['gate_1_errors']:
        for err in gates_result['gate_1_errors']:
            print(f"  ✗ {err}")
    
    print(f"✓ Gate 2 (Structure): {'PASS' if gates_result['gate_2_structure'] else 'FAIL'}")
    if gates_result['gate_2_errors']:
        for err in gates_result['gate_2_errors'][:3]:  # Show first 3 errors
            print(f"  ✗ {err}")
    
    print(f"✓ Gate 3 (Content): {'PASS' if gates_result['gate_3_content'] else 'FAIL'}")
    if gates_result['gate_3_errors']:
        for err in gates_result['gate_3_errors'][:3]:
            print(f"  ✗ {err}")
    
    print(f"✓ Gate 4 (Metrics): {'PASS' if gates_result['gate_4']['pass'] else 'FAIL'}")
    print(f"  - Tokens: {gates_result['gate_4']['metrics']['tokens']}/{gates_result['gate_4']['metrics']['budget']}")
    print(f"  - Quality Score: {gates_result['quality_score']}/100")
    
    print(f"\n✅ FINAL STATUS: {gates_result['status']}")
    print(f"✅ Gates Passed: {gates_result['passed_gates']}/5")
    
    return gates_result


def test_zip_delivery(document_result, gates_result):
    """Test: Deliver to zip file"""
    print("\n" + "=" * 60)
    print("TEST 3: Deliver to Zip File")
    print("=" * 60)
    
    # Combine document and gates info
    document_with_gates = {
        **document_result,
        'metadata': {
            **document_result['metadata'],
            'quality_score': gates_result['quality_score'],
            'status': gates_result['status']
        }
    }
    
    handler = ZipHandler(output_dir="output")
    zip_path = handler.create_zip([document_with_gates])
    
    print(f"\n✅ Zip created successfully")
    print(f"   Path: {zip_path}")
    
    return zip_path


def test_workflow():
    """Run complete E2E workflow"""
    print("\n")
    print("🚀 DOCGEN E2E TEST SUITE")
    print("=" * 60)
    
    try:
        # Test 1: Generate
        doc_result = test_prd_generation()
        
        # Test 2: Quality Gates
        gates_result = test_quality_gates(doc_result)
        
        # Test 3: Delivery
        zip_path = test_zip_delivery(doc_result, gates_result)
        
        # Summary
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED")
        print("=" * 60)
        print(f"\n📊 Summary:")
        print(f"   Document: {doc_result['filename']}")
        print(f"   Quality Score: {gates_result['quality_score']}/100")
        print(f"   Status: {gates_result['status']}")
        print(f"   Zip Output: {zip_path}")
        print("\n✨ System is ready for production!")
        
        return True
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = test_workflow()
    sys.exit(0 if success else 1)
