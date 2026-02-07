import unittest
from app import app
import re

class TestBridgeAndServer(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_server_routes(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertEqual(self.client.get('/master_category_bank.json').status_code, 200)

    def test_html_fetch_link(self):
        with open('index.html', 'r') as f:
            html = f.read()
        match = re.search(r"fetch\(['\"](.*?)['\"]\)", html)
        if not match: self.fail("No fetch() call found in HTML")
        
        fetched = match.group(1)
        # Python serves 'master_category_bank.json'
        self.assertEqual(fetched, 'master_category_bank.json', 
            f"HTML fetches '{fetched}' but server provides 'master_category_bank.json'")
