import unittest
from app import app
from bs4 import BeautifulSoup
import re

class TestBridgeAndServer(unittest.TestCase):
    """
    Tests the 'Bridge' between Frontend (HTML) and Backend (Flask).
    """

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_flask_serves_homepage(self):
        """Test if the root URL '/' returns the index.html file."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)

    def test_flask_serves_json(self):
        """Test if the Flask app actually serves the JSON file at the expected route."""
        response = self.client.get('/master_category_bank.json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')

    def test_html_fetch_link_validity(self):
        """
        CRITICAL TEST: Parses index.html to find the JavaScript fetch() call.
        It verifies that the HTML is fetching the exact file name served by Python.
        """
        # 1. Get the HTML content
        with open('index.html', 'r') as f:
            html_content = f.read()

        # 2. Extract the fetch URL using Regex
        # Looking for: fetch('some_filename.json')
        match = re.search(r"fetch\(['\"](.*?)['\"]\)", html_content)
        
        if not match:
            self.fail("Could not find a fetch() call in the HTML JavaScript.")
            
        fetched_filename = match.group(1)
        
        # 3. Define what Python is actually serving
        served_filename = 'master_category_bank.json'

        # 4. Assert they match
        self.assertEqual(
            fetched_filename, 
            served_filename, 
            f"\n[BROKEN BRIDGE DETECTED]\nHTML is trying to fetch '{fetched_filename}'\n"
            f"But Python is serving '{served_filename}'\n"
            f"FIX: Change line 288 in index.html to fetch('{served_filename}')"
        )

if __name__ == '__main__':
    unittest.main()