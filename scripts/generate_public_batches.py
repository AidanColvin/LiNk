"""
Generate unique 4x4 puzzle batches for the public-facing webpage.

Rules enforced:
- 4 categories per batch: Seed, Red Herring, Tricky, Expert.
- 16 unique words per batch (no duplicates across the grid).
- Words are common, >= 3 letters, and mapped to conceptual themes.
- New categories do not repeat any existing 4-word category in
  data/difficulty_matrix_bank.jsonl.
- Reads README.md on each run to reflect the current rules source.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path
from typing import Dict, Iterable, List, Set

DIFFICULTY_MATRIX = [
    {
        "level": "Level 1",
        "category_type": "Seed",
        "color": "#90EE90",
        "logic_rule": "2-word overlap",
        "effect_on_player": "The anchor group. 50% of its words are shared with more complex categories.",
    },
    {
        "level": "Level 2",
        "category_type": "Red Herring",
        "color": "#ADD8E6",
        "logic_rule": "3-word overlap",
        "effect_on_player": "The primary distractor. Targets the Seed/Tricky groups to create false sets.",
    },
    {
        "level": "Level 3",
        "category_type": "Tricky",
        "color": "#FFFFE0",
        "logic_rule": "3-word overlap",
        "effect_on_player": "High-interference. Creates a nearly complete set of 4 that is actually invalid.",
    },
    {
        "level": "Level 4",
        "category_type": "Expert",
        "color": "#FFB6C1",
        "logic_rule": "4-word overlap",
        "effect_on_player": "The hardest group. It does not exist in isolation; all 4 words fit elsewhere.",
    },
]

RULES_BLOCK = {
    "type": "categorization_rules",
    "relationship_rules": [
        "Thematic consistency: Categories must be conceptually related (e.g., Animals, Colors, Fruits).",
        "Difficulty scaling: Every board must contain exactly four categories: Seed, Red Herring, Tricky, and Expert.",
    ],
    "prohibited_categories": [
        "No grammar/linguistics: Categories based on parts of speech (nouns, verbs, adjectives) are forbidden.",
        "No spelling tricks: Categories cannot rely on spelling patterns (e.g., words starting with S).",
        "No word roots: Categories cannot be based on word roots or simple suffixes/prefixes (e.g., Cat, Cats, Catty).",
    ],
}

WORD_SELECTION_CRITERIA = {
    "type": "word_selection_criteria",
    "criteria": [
        "Length: Words must be at least 3 letters long.",
        "Complexity: Words must not exceed 3 syllables.",
        "Accessibility: Use common, recognizable words; avoid obscure, technical, or highly specialized terms.",
        "Uniqueness: Each word is unique to the grid but serves as a bridge between multiple category themes.",
    ],
}


def read_readme(path: Path) -> str:
    """Load README.md on each run to ensure rules stay current."""
    if not path.exists():
        raise FileNotFoundError(f"README not found at {path}")
    return path.read_text(encoding="utf-8")


def read_existing_categories(path: Path) -> Set[frozenset[str]]:
    """Return set of existing 4-word category signatures (uppercased)."""
    existing: Set[frozenset[str]] = set()
    if not path.exists():
        return existing
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            payload = json.loads(line)
            if payload.get("type") != "category":
                continue
            words = [word.upper() for word in payload.get("words", [])]
            if len(words) == 4:
                existing.add(frozenset(words))
    return existing


def read_theme_word_pool(path: Path) -> Dict[str, List[str]]:
    """Build a word pool per theme from the existing bank."""
    theme_words: Dict[str, Set[str]] = {}
    if not path.exists():
        raise FileNotFoundError(f"Bank not found at {path}")
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            payload = json.loads(line)
            if payload.get("type") != "category":
                continue
            theme = payload.get("theme")
            if not theme:
                continue
            word_set = theme_words.setdefault(theme, set())
            for word in payload.get("words", []):
                word_set.add(word.upper())
    return {theme: sorted(words) for theme, words in theme_words.items()}


def validate_word(word: str) -> None:
    if len(word) < 3:
        raise ValueError(f"Word too short: {word}")


def validate_category(words: Iterable[str]) -> None:
    unique = {word.upper() for word in words}
    if len(unique) != 4:
        raise ValueError(f"Category must contain 4 unique words: {words}")
    for word in unique:
        validate_word(word)


def choose_words_for_theme(
    rng: random.Random,
    theme_words: List[str],
    excluded_sets: Set[frozenset[str]],
    max_attempts: int = 200,
) -> List[str]:
    for _ in range(max_attempts):
        words = rng.sample(theme_words, 4)
        signature = frozenset(word.upper() for word in words)
        if signature in excluded_sets:
            continue
        validate_category(words)
        return [word.upper() for word in words]
    raise RuntimeError("Unable to find a unique category for theme")


def build_batches(
    rng: random.Random,
    theme_pool: Dict[str, List[str]],
    existing_category_sets: Set[frozenset[str]],
    batch_count: int,
) -> List[dict]:
    batches: List[dict] = []
    used_category_sets: Set[frozenset[str]] = set(existing_category_sets)
    used_batch_signatures: Set[frozenset[str]] = set()

    themes = list(theme_pool.keys())
    if len(themes) < 4:
        raise ValueError("Need at least four themes to build batches")

    for batch_index in range(1, batch_count + 1):
        for _ in range(500):
            chosen_themes = rng.sample(themes, 4)
            category_entries = []
            batch_words: List[str] = []
            category_sets: List[frozenset[str]] = []
            for difficulty in DIFFICULTY_MATRIX:
                theme = chosen_themes[len(category_entries)]
                words = choose_words_for_theme(
                    rng,
                    theme_pool[theme],
                    used_category_sets,
                )
                if set(words) & set(batch_words):
                    break
                category_sets.append(frozenset(words))
                batch_words.extend(words)
                category_entries.append(
                    {
                        "theme": theme,
                        "name": f"{theme} {difficulty['category_type']} {batch_index}",
                        "difficulty": difficulty["category_type"],
                        "color": difficulty["color"],
                        "logic_rule": difficulty["logic_rule"],
                        "effect_on_player": difficulty["effect_on_player"],
                        "words": words,
                    }
                )
            if len(category_entries) != 4:
                continue
            batch_signature = frozenset(batch_words)
            if batch_signature in used_batch_signatures:
                continue
            used_batch_signatures.add(batch_signature)
            for signature in category_sets:
                used_category_sets.add(signature)
            batches.append(
                {
                    "type": "batch",
                    "id": batch_index,
                    "categories": category_entries,
                }
            )
            break
        else:
            raise RuntimeError(f"Failed to build batch {batch_index}")
    return batches


def write_jsonl(path: Path, lines: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for line in lines:
            handle.write(json.dumps(line, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate unique public puzzle batches")
    parser.add_argument("--count", type=int, default=250, help="Number of batches to generate")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/public_puzzle_batches.jsonl"),
        help="Output JSONL path",
    )
    parser.add_argument(
        "--bank",
        type=Path,
        default=Path("data/difficulty_matrix_bank.jsonl"),
        help="Existing category bank to avoid duplicates",
    )
    parser.add_argument("--seed", type=int, default=42, help="RNG seed for reproducible batches")
    args = parser.parse_args()

    readme_text = read_readme(Path("README.md"))
    readme_hash = hashlib.sha256(readme_text.encode("utf-8")).hexdigest()

    existing_category_sets = read_existing_categories(args.bank)
    theme_pool = read_theme_word_pool(args.bank)

    rng = random.Random(args.seed)
    batches = build_batches(rng, theme_pool, existing_category_sets, args.count)

    output_lines = [
        {
            "type": "difficulty_matrix",
            "description": "Difficulty is determined by how many words from a category are stolen by other groups on the board.",
            "entries": DIFFICULTY_MATRIX,
        },
        {
            "type": "readme_reference",
            "path": "README.md",
            "sha256": readme_hash,
        },
        RULES_BLOCK,
        WORD_SELECTION_CRITERIA,
    ]
    output_lines.extend(batches)

    write_jsonl(args.output, output_lines)


if __name__ == "__main__":
    main()
