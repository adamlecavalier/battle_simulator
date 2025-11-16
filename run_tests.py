#!/usr/bin/env python3
"""
Test runner script for the battle simulator
Run all tests with: python3 run_tests.py
Run specific test file: python3 run_tests.py test_character
"""
import unittest
import sys

def run_all_tests():
    """Discover and run all tests in the current directory"""
    loader = unittest.TestLoader()
    start_dir = '.'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on test results
    return 0 if result.wasSuccessful() else 1

def run_specific_test(test_module):
    """Run a specific test module"""
    loader = unittest.TestLoader()
    
    # Add .py extension if not present
    if not test_module.endswith('.py'):
        test_module = test_module + '.py'
    
    try:
        suite = loader.loadTestsFromName(test_module.replace('.py', ''))
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        return 0 if result.wasSuccessful() else 1
    except Exception as e:
        print(f"Error loading test module '{test_module}': {e}")
        return 1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Run specific test file
        exit_code = run_specific_test(sys.argv[1])
    else:
        # Run all tests
        exit_code = run_all_tests()
    
    sys.exit(exit_code)
