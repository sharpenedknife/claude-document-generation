#!/usr/bin/env python3
"""
Docgen Integration Test Suite
Tests HTTP server, generation, validation, and delivery
"""

import json
import time
import subprocess
import requests
from pathlib import Path
from threading import Thread
import sys

# Configuration
API_URL = "http://localhost:5000"
SAMPLE_ANSWERS = {
    "q0": "A SaaS platform for documentation generation",
    "q1": "Product managers, engineers, startup founders",
    "q2": "Manual docs take 2-4 weeks per doc",
    "q3": "API-first generator with quality gates and delivery",
    "q4": "Q2 2026",
    "q5": "Python + Claude API backend, React frontend",
    "q6": "$50,000"
}


class DocgenIntegrationTester:
    def __init__(self):
        self.server_process = None
        self.passed = 0
        self.failed = 0
    
    def start_server(self):
        """Start the HTTP server in background"""
        print("🚀 Starting HTTP server...")
        self.server_process = subprocess.Popen(
            ['python3', 'code/server.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to start
        max_retries = 10
        for i in range(max_retries):
            try:
                response = requests.get(f"{API_URL}/health", timeout=2)
                if response.status_code == 200:
                    print("✓ Server started successfully")
                    return True
            except:
                if i < max_retries - 1:
                    time.sleep(0.5)
        
        print("✗ Server failed to start")
        return False
    
    def stop_server(self):
        """Stop the HTTP server"""
        if self.server_process:
            print("\n🛑 Stopping server...")
            self.server_process.terminate()
            self.server_process.wait()
            print("✓ Server stopped")
    
    def test(self, name: str, func):
        """Run a test and report results"""
        print(f"\n📋 {name}...", end=' ')
        try:
            func()
            print("✓ PASS")
            self.passed += 1
        except AssertionError as e:
            print(f"✗ FAIL: {e}")
            self.failed += 1
        except Exception as e:
            print(f"✗ ERROR: {e}")
            self.failed += 1
    
    def run_tests(self):
        """Run all tests"""
        print("=" * 60)
        print("DOCGEN INTEGRATION TEST SUITE")
        print("=" * 60)
        
        # Start server
        if not self.start_server():
            print("Failed to start server")
            return False
        
        try:
            # Test 1: Health check
            def test_health():
                response = requests.get(f"{API_URL}/health")
                assert response.status_code == 200
                data = response.json()
                assert data['status'] == 'healthy'
            
            self.test("Health Check", test_health)
            
            # Test 2: List projects
            def test_list_projects():
                response = requests.get(f"{API_URL}/api/docgen/projects")
                assert response.status_code == 200
                data = response.json()
                assert len(data['projects']) == 10
                assert data['projects'][0]['id'] == 1
            
            self.test("List Projects", test_list_projects)
            
            # Test 3: Get API info
            def test_api_info():
                response = requests.get(f"{API_URL}/api/docgen/info")
                assert response.status_code == 200
                data = response.json()
                assert data['name'] == 'Docgen API'
                assert 'endpoints' in data
            
            self.test("API Info", test_api_info)
            
            # Test 4: Validate document (before generation)
            def test_validate_document():
                doc_content = """---
title: Test Document
description: A test document
version: 1.0
date: 2026-04-02
author: Docgen
category: Product
status: PRODUCTION_READY
tags: [test]
---

## Overview
This is a test document.

## Prerequisites
- Test environment
- Python 3.8+

## Why This Matters
Documentation is important.

## What's Next
Run more tests.
"""
                response = requests.post(
                    f"{API_URL}/api/docgen/validate",
                    json={
                        'content': doc_content,
                        'category': 'Product'
                    }
                )
                assert response.status_code == 200
                data = response.json()
                assert 'validation' in data
            
            self.test("Validate Document", test_validate_document)
            
            # Test 5: Generate PRD (Note: requires ANTHROPIC_API_KEY)
            def test_generate_prd():
                response = requests.post(
                    f"{API_URL}/api/docgen/generate",
                    json={
                        'project': 1,
                        'answers': SAMPLE_ANSWERS,
                        'destinations': ['zip']
                    }
                )
                assert response.status_code == 200
                data = response.json()
                assert data['status'] == 'SUCCESS'
                assert 'document' in data
                assert 'quality' in data
                assert data['quality']['status'] == 'PRODUCTION_READY'
                assert data['quality']['score'] >= 80
            
            self.test("Generate PRD (with Claude API)", test_generate_prd)
            
            # Test 6: Check generation status
            def test_get_status():
                response = requests.get(f"{API_URL}/api/docgen/status")
                assert response.status_code == 200
                data = response.json()
                assert 'total_generations' in data
            
            self.test("Get Generation Status", test_get_status)
            
            # Test 7: Invalid project ID
            def test_invalid_project():
                response = requests.post(
                    f"{API_URL}/api/docgen/generate",
                    json={
                        'project': 99,
                        'answers': SAMPLE_ANSWERS,
                        'destinations': ['zip']
                    }
                )
                assert response.status_code == 400
                data = response.json()
                assert 'error' in data
            
            self.test("Invalid Project ID Error", test_invalid_project)
            
            # Test 8: Missing required fields
            def test_missing_fields():
                response = requests.post(
                    f"{API_URL}/api/docgen/generate",
                    json={
                        'project': 1
                        # Missing 'answers' and 'destinations'
                    }
                )
                assert response.status_code == 400
            
            self.test("Missing Required Fields Error", test_missing_fields)
            
            # Test 9: Invalid destination
            def test_invalid_destination():
                response = requests.post(
                    f"{API_URL}/api/docgen/generate",
                    json={
                        'project': 1,
                        'answers': SAMPLE_ANSWERS,
                        'destinations': ['invalid-destination']
                    }
                )
                assert response.status_code == 400
            
            self.test("Invalid Destination Error", test_invalid_destination)
            
            # Test 10: 404 handling
            def test_404():
                response = requests.get(f"{API_URL}/api/nonexistent")
                assert response.status_code == 404
            
            self.test("404 Error Handling", test_404)
            
        finally:
            self.stop_server()
        
        # Print summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"✓ Passed: {self.passed}")
        print(f"✗ Failed: {self.failed}")
        print(f"Total: {self.passed + self.failed}")
        
        if self.failed == 0:
            print("\n🎉 ALL TESTS PASSED!")
            return True
        else:
            print(f"\n⚠️  {self.failed} test(s) failed")
            return False


def main():
    """Run integration tests"""
    
    # Check if we're in the right directory
    if not Path('code').exists():
        print("Error: 'code' directory not found. Run from project root.")
        return False
    
    tester = DocgenIntegrationTester()
    success = tester.run_tests()
    
    return success


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
