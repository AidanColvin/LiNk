import json
import os

def run_diagnostic():
    file_path = 'categories.json'
    
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found!")
        return

    with open(file_path, 'r') as f:
        data = json.load(f)

    batches = data.get("batches", {})
    all_errors = []

    print(f"--- Starting Validation on {data['meta']['total_categories']} Categories ---")

    for batch_name, categories in batches.items():
        batch_words = []
        
        for cat in categories:
            # Check 1: Exactly 4 words
            if len(cat['words']) != 4:
                all_errors.append(f"Batch {batch_name}: Category '{cat['name']}' must have 4 words.")

            # Check 2: Difficulty/Color consistency
            valid_diffs = ["Seed", "Red Herring", "Tricky", "Expert"]
            if cat['difficulty'] not in valid_diffs:
                all_errors.append(f"Batch {batch_name}: Category '{cat['name']}' has invalid difficulty.")

            batch_words.extend(cat['words'])

        # Check 3: Duplicates within a single batch (The "Connections" rule)
        # Note: Connections games usually have 16 unique words per game board.
        seen = set()
        dupes = [x for x in batch_words if x in seen or seen.add(x)]
        if dupes:
            all_errors.append(f"Batch {batch_name}: Duplicate words found: {set(dupes)}")

    if not all_errors:
        print("✅ All Tests Passed! Data is structurally sound and ready for expansion.")
    else:
        print("❌ Validation Failed:")
        for error in all_errors:
            print(f" - {error}")

if __name__ == "__main__":
    run_diagnostic()