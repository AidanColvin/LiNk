import unittest
import sys
import os
import json
import re

# Add 'src' to path so we can import app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_route(self):
        """Test if root URL serves index.html"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CATEGORIES', response.data)

    def test_data_route(self):
        """Test if /data/ route serves the JSON correctly"""
        response = self.client.get('/data/master_category_bank.json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')

    def test_html_bridge(self):
        """
        Verify that index.html fetches the EXACT route served by Flask.
        """
        with open('index.html', 'r') as f:
            html_content = f.read()
        
        # Look for fetch('...')
        match = re.search(r"fetch\(['\"](.*?)['\"]\)", html_content)
        if not match:
            self.fail("No fetch() call found in index.html")
            
        fetched_url = match.group(1)
        expected_url = 'data/master_category_bank.json'
        
        self.assertEqual(fetched_url, expected_url, 
            f"HTML fetches '{fetched_url}' but Flask expects '{expected_url}'")

if __name__ == '__main__':
    unittest.main()
