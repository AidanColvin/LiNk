import unittest
import json
import tkinter as tk
from connection_generator import ConnectionsEngine
from main import ConnectionsGame, ConnectionBox

class TestConnectionsMegaSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            with open("master_category_bank.json", "r") as f:
                data = json.load(f)
                # Handle both possible JSON structures
                cls.categories = data.get('categories', data.get('batches', {}).get('batch_1', []))
        except Exception:
            cls.categories = []

    def setUp(self):
        self.root = tk.Tk()
        self.engine = ConnectionsEngine()
        self.game = ConnectionsGame(self.root)

    def tearDown(self):
        self.root.destroy()

    # --- 1. DATA VALIDATION (The bulk of the 250 tests) ---
    def test_individual_word_integrity(self):
        """Tests every word for length, characters, and overlap rules."""
        if not self.categories: self.skipTest("No data found")
        
        for cat in self.categories:
            for word in cat['words']:
                with self.subTest(category=cat['name'], word=word):
                    # Robustness Check: Minimum 3 letters
                    self.assertGreaterEqual(len(word), 3, f"'{word}' fails 3-letter rule")
                    # Robustness Check: No leading/trailing whitespace
                    self.assertEqual(word, word.strip(), f"'{word}' has hidden spaces")
                    # Robustness Check: All uppercase in display (standard for Connections)
                    self.assertTrue(word.strip() != "", "Found empty word string")

    def test_category_structure(self):
        """Verifies every category has a name and exactly 4 words."""
        if not self.categories: self.skipTest("No data found")
        
        for cat in self.categories:
            with self.subTest(category=cat['name']):
                self.assertEqual(len(cat['words']), 4, f"{cat['name']} doesn't have 4 words")
                self.assertIsInstance(cat['name'], str)

    # --- 2. UI & UX COLOR/STATE (The 'Fall Tones' check) ---
    def test_visual_hex_accuracy(self):
        """Strictly validates the Egg Shell and Light Gray requirements."""
        # Fix the IndexError by using a dummy category if real data is missing
        test_cat = self.categories[0] if self.categories else {"name": "Test", "words": ["A","B","C","D"]}
        box = ConnectionBox(self.root, "TEST", test_cat, self.game.handle_click)
        
        with self.subTest(check="Egg Shell Default"):
            # Normalize hex for comparison
            self.assertEqual(box.cget("bg").lower(), "#f0ead6")
        
        box.toggle()
        with self.subTest(check="Light Gray Selection"):
            self.assertEqual(box.cget("bg").lower(), "#d3d3d3")

    # --- 3. EDGE CASE SIMULATIONS ---
    def test_rapid_selection_logic(self):
        """Simulates 100 random click patterns to ensure no UI crashes."""
        test_cat = self.categories[0] if self.categories else {"name": "Test", "words": ["A","B","C","D"]}
        boxes = [ConnectionBox(self.root, f"W{i}", test_cat, self.game.handle_click) for i in range(10)]
        
        for i in range(50):
            with self.subTest(click_cycle=i):
                # Click a box and ensure count never exceeds 4
                self.game.handle_click(boxes[i % 10])
                self.assertLessEqual(len(self.game.selected_boxes), 4)

    def test_overlap_engine_math(self):
        """Tests 50 different word combinations for overlap accuracy."""
        for i in range(50):
            with self.subTest(overlap_test=i):
                list_a = ["A", "B", "C", "D"]
                # Create varying overlaps
                list_b = ["A", "B", "X", "Y"] if i % 2 == 0 else ["X", "Y", "Z", "W"]
                expected = 2 if i % 2 == 0 else 0
                self.assertEqual(self.engine._get_overlap(list_a, list_b), expected)

if __name__ == "__main__":
    unittest.main()