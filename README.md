# CATEGORIES: Overlap Logic Edition

This project is a Python-based word puzzle game designed to challenge deduction through a sophisticated **Overlap Logic Engine**. Unlike standard trivia, these puzzles are built on "Chains of Interference," where words logically belong to multiple categories simultaneously.

---

## 🧩 Difficulty Matrix & Overlap Logic

Difficulty is determined by how many words from a category are "stolen" by other groups on the board.

| Difficulty | Category Type | Color | Logic Rule | Effect on Player |
| --- | --- | --- | --- | --- |
| **Level 1** | **Seed** | `#90EE90` | 2-word overlap | The "anchor" group. 50% of its words are shared with more complex categories. |
| **Level 2** | **Red Herring** | `#ADD8E6` | 3-word overlap | The primary distractor. Targets the Seed/Tricky groups to create false sets. |
| **Level 3** | **Tricky** | `#FFFFE0` | 3-word overlap | High-interference. Creates a "nearly complete" set of 4 that is actually invalid. |
| **Level 4** | **Expert** | `#FFB6C1` | 4-word overlap | The hardest group. It does not exist in isolation; all 4 words fit elsewhere. |

---

## 📋 Categorization Rules

To maintain the quality and logic of the game, all puzzles must adhere to the following strict guidelines:

### Relationship Rules

* **Thematic Consistency:** Categories must be conceptually related (e.g., "Animals," "Colors," "Fruits").
* **Difficulty Scaling:** Every board must contain exactly four categories: Seed, Red Herring, Tricky, and Expert.

### Prohibited Categories

* **No Grammar/Linguistics:** Categories based on parts of speech (Nouns, Verbs, Adjectives) are strictly forbidden.
* **No Spelling Tricks:** Categories cannot rely on spelling patterns (e.g., "Words starting with S").
* **No Word Roots:** Categories cannot be based on word roots or simple suffixes/prefixes (e.g., "Cat," "Cats," "Catty").

---

## ✍️ Word Selection Criteria

* **Length:** Words must be at least **3 letters** long.
* **Complexity:** Words must not exceed **3 syllables**.
* **Accessibility:** Use common, recognizable words. Avoid obscure, technical, or highly specialized terms.
* **Uniqueness:** Each word is unique to the grid but serves as a "bridge" between multiple category themes.

---

## ⚙️ Function Flow

The engine assembles the board using a specific four-step generation process:

1. **Import Bank:** Loads the `master_category_bank.json`.
2. **Select Seed:** Picks the first category to set the board's baseline theme.
3. **Calculate Overlap:** * Finds a **Red Herring** sharing 3 words with the Seed/Tricky group.
* Finds a **Tricky** group sharing 3 words with the total board.


4. **Finalize Expert:** Identifies a category where all 4 words overlap across the other three themes, making it solvable only by elimination.

---

## 🎮 Interface & Controls

* **The Grid:** A 4x4 layout of 16 boxes.
* **Interaction:** * **Select:** Click a box to highlight it (adds to selection list).
* **Deselect:** Click again to remove from selection.
* **Submit:** Press the **Submit** button or the **Return** key.


* **Feedback System:**
* **3 Correct:** Displays "One off."
* **2 Correct:** Displays "2 off."
* **Otherwise:** Displays "Try again."


* **Utility:** * **Shuffle:** Randomizes the grid without clearing selections.
* **Reset:** Wipes progress and generates a new puzzle.



---

## 📂 Master Category Bank

**Example Chain of Interference:**

* **Seed (FRUIT):** Apple, **DATE**, **LIME**, Kiwi
* **Red Herring (CALENDAR):** **DATE**, Month, Year, Week
* **Tricky (COLORS):** **LIME**, Orange, Rose, **SILVER**
* **Expert (METALS):** **SILVER**, Gold, Iron, Tin

