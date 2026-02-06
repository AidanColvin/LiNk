"""
Logic engine for the Connections Game.

This module provides the ConnectionsEngine class, which handles the 
selection of word categories from a JSON bank while enforcing specific 
overlap rules (Expert, Tricky, and Seed) to create red herrings.
"""

import json
import random
from typing import List, Dict, Optional, Set


class ConnectionsEngine:
    """
    Manages category selection and puzzle assembly logic.

    Attributes:
        bank (List[Dict]): The full list of categories loaded from the JSON.
    """

    def __init__(self, json_path: str = "master_category_bank.json"):
        """
        Initializes the engine and loads the category data.

        Args:
            json_path: Path to the JSON file containing word categories.
        """
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
                # Supports both 'categories' list and 'batches' dictionary structures
                if 'categories' in data:
                    self.bank = data['categories']
                elif 'batches' in data:
                    self.bank = []
                    for batch in data['batches'].values():
                        self.bank.extend(batch)
                else:
                    self.bank = []
        except (FileNotFoundError, json.JSONDecodeError):
            self.bank = []

    def _get_overlap(self, list_a: List[str], list_b: List[str]) -> int:
        """Calculates the number of shared words between two lists."""
        return len(set(list_a).intersection(set(list_b)))

    def _get_valid_experts(self) -> List[Dict]:
        """
        Identifies categories suitable for the 'Expert' role.
        
        A category is a valid Expert if every word in it exists in at least
        one other category in the bank, ensuring decoys exist for all 4 words.
        """
        return [
            cat for cat in self.bank if all(
                any(word in other['words'] for other in self.bank if other != cat)
                for word in cat['words']
            )
        ]

    def _backtrack(self, current_puzzle: List[Dict], board_words: List[str], 
                   excluded: Set[str], depth: int) -> Optional[List[Dict]]:
        """
        Recursive search to find a valid 4-category puzzle chain.

        Args:
            current_puzzle: Categories selected so far.
            board_words: Flattened list of all words currently in the puzzle.
            excluded: Set of names of categories already used.
            depth: The current step (1=Tricky, 2=Hard/Herring, 3=Seed).

        Returns:
            A list of 4 categories or None if no valid chain is found.
        """
        if len(current_puzzle) == 4:
            return current_puzzle

        # Define the target overlap based on your logic:
        # Step 1 (Tricky): 3 words, Step 2 (Herring): 3 words, Step 3 (Seed): 2 words
        target = 3 if depth < 3 else 2
        
        candidates = [c for c in self.bank if c['name'] not in excluded]
        random.shuffle(candidates)

        for candidate in candidates:
            if self._get_overlap(candidate['words'], board_words) == target:
                result = self._backtrack(
                    current_puzzle + [candidate],
                    board_words + candidate['words'],
                    excluded | {candidate['name']},
                    depth + 1
                )
                if result:
                    return result
        return None

    def get_new_puzzle(self) -> List[Dict]:
        """
        Generates a 4-category puzzle based on strict overlap rules.

        Returns:
            A list of 4 dictionaries, each representing a category.

        Raises:
            ValueError: If the bank is empty or no valid puzzle can be formed.
        """
        if not self.bank:
            raise ValueError("Category bank is empty or missing.")

        expert_pool = self._get_valid_experts()
        random.shuffle(expert_pool)

        # Try to build a strict chain starting from an Expert category
        for expert in expert_pool:
            puzzle = self._backtrack(
                [expert], 
                list(expert['words']), 
                {expert['name']}, 
                1
            )
            if puzzle:
                return puzzle

        # Fallback Case: If strict rules cannot be met, return 4 random categories
        # This prevents the game from crashing if the JSON bank is small.
        if len(self.bank) >= 4:
            return random.sample(self.bank, 4)
            
        return self.bank