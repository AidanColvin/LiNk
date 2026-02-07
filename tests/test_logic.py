import unittest
import json
import os

class TestGameDataIntegrity(unittest.TestCase):
    """
    Tests the integrity of the master_category_bank.json file to ensure
    it adheres to game rules before being served to the frontend.
    """

    def setUp(self):
        """Load the JSON data before each test."""
        self.filename = 'master_category_bank.json'
        if not os.path.exists(self.filename):
            self.skipTest(f"{self.filename} not found. Run the generator script first.")
        
        with open(self.filename, 'r') as f:
            self.data = json.load(f)

    def test_json_structure(self):
        """
        Verify the JSON has the correct 'batches' root structure.
        """
        self.assertIn('batches', self.data, "JSON must contain a 'batches' key.")
        self.assertTrue(len(self.data['batches']) > 0, "Batches dictionary should not be empty.")

    def test_batch_validity(self):
        """
        Strict Rule Check:
        1. Every batch must have exactly 4 categories.
        2. Every category must have exactly 4 words.
        3. No duplicate words allowed within a single game grid (16 unique words).
        """
        for batch_id, categories in self.data['batches'].items():
            # Rule: Exactly 4 categories per game
            self.assertEqual(len(categories), 4, f"Batch {batch_id} must have exactly 4 categories.")
            
            all_words_in_batch = []
            
            for category in categories:
                # Rule: Category structure keys
                self.assertIn('name', category)
                self.assertIn('words', category)
                self.assertIn('color', category)
                
                # Rule: Exactly 4 words per category
                self.assertEqual(len(category['words']), 4, 
                                 f"Category {category['name']} in {batch_id} must have 4 words.")
                
                all_words_in_batch.extend([w.upper() for w in category['words']])

            # Rule: 16 Unique words (No duplicates in the grid)
            unique_word_count = len(set(all_words_in_batch))
            self.assertEqual(unique_word_count, 16, 
                             f"Batch {batch_id} contains duplicate words. Found {unique_word_count}/16 unique.")

    def test_difficulty_coloring(self):
        """
        Verify that every batch contains one of each difficulty level/color type
        to ensure the 'Seed', 'Red Herring', 'Tricky', 'Expert' logic is present.
        """
        expected_difficulties = {"Seed", "Red Herring", "Tricky", "Expert"}
        
        for batch_id, categories in self.data['batches'].items():
            batch_difficulties = {cat['color'] for cat in categories}
            # Check if the set of found colors matches the expected set
            self.assertTrue(expected_difficulties.issubset(batch_difficulties),
                            f"Batch {batch_id} is missing a difficulty level. Found: {batch_difficulties}")

if __name__ == '__main__':
    unittest.main()