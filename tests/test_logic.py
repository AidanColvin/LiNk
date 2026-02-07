import unittest
import json
import os

class TestGameDataIntegrity(unittest.TestCase):
    def setUp(self):
        self.filename = 'master_category_bank.json'
        if not os.path.exists(self.filename):
            self.skipTest(f"{self.filename} not found.")
        with open(self.filename, 'r') as f:
            self.data = json.load(f)

    def test_json_structure(self):
        self.assertIn('batches', self.data)
        self.assertTrue(len(self.data['batches']) > 0)

    def test_batch_rules(self):
        for batch_id, categories in self.data['batches'].items():
            self.assertEqual(len(categories), 4, f"Batch {batch_id} must have 4 categories")
            all_words = []
            for cat in categories:
                self.assertEqual(len(cat['words']), 4)
                all_words.extend(cat['words'])
            self.assertEqual(len(set(all_words)), 16, "Grid must have 16 unique words")
