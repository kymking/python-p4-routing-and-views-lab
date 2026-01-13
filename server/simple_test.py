#!/usr/bin/env python3

import sys
import io
sys.path.insert(0, '.')

from app import app

def test_basic_functionality():
    """Simple test to verify Flask app functionality"""
    
    # Test index route
    response = app.test_client().get('/')
    print(f"Index route status: {response.status_code}")
    print(f"Index route response: {repr(response.data.decode())}")
    expected_index = '<h1>Python Operations with Flask Routing and Views</h1>'
    print(f"Expected: {repr(expected_index)}")
    print(f"Match: {response.data.decode() == expected_index}")
    print()
    
    # Test print route
    response = app.test_client().get('/print/hello')
    print(f"Print route status: {response.status_code}")
    print(f"Print route response: {repr(response.data.decode())}")
    expected_print = 'hello'
    print(f"Expected: {repr(expected_print)}")
    print(f"Match: {response.data.decode() == expected_print}")
    print()
    
    # Test count route
    response = app.test_client().get('/count/10')
    print(f"Count route status: {response.status_code}")
    print(f"Count route response: {repr(response.data.decode())}")
    expected_count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'
    print(f"Expected: {repr(expected_count)}")
    print(f"Match: {response.data.decode() == expected_count}")
    print()
    
    # Test math routes
    test_cases = [
        ('/math/5/+/5', '10'),
        ('/math/5/-/5', '0'),
        ('/math/5/*/5', '25'),
        ('/math/5/div/5', '1.0'),
        ('/math/5/%/5', '0')
    ]
    
    for url, expected in test_cases:
        response = app.test_client().get(url)
        print(f"Math route {url} status: {response.status_code}")
        print(f"Math route {url} response: {repr(response.data.decode())}")
        print(f"Expected: {repr(expected)}")
        print(f"Match: {response.data.decode() == expected}")
        print()

if __name__ == '__main__':
    test_basic_functionality()