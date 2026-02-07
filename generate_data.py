import json
import random

# --- THE MASTER KNOWLEDGE BANK ---
# Add more categories here to expand the game!
master_bank = [
    {"name": "FRUIT", "words": ["APPLE", "DATE", "LIME", "KIWI"]},
    {"name": "CALENDAR", "words": ["DATE", "MONTH", "YEAR", "WEEK"]},
    {"name": "COLORS", "words": ["LIME", "ORANGE", "ROSE", "SILVER"]},
    {"name": "METALS", "words": ["SILVER", "GOLD", "IRON", "TIN"]},
    {"name": "DOG SOUNDS", "words": ["BARK", "WOOF", "YELP", "HOWL"]},
    {"name": "TREE PARTS", "words": ["BARK", "LEAF", "ROOT", "BRANCH"]},
    {"name": "BUSINESS", "words": ["SALES", "LEGAL", "ADMIN", "SECTOR"]},
    {"name": "GARDENING", "words": ["SOW", "SEED", "BLOOM", "GARDEN"]},
    {"name": "WRITING", "words": ["PEN", "PENCIL", "MARKER", "CRAYON"]},
    {"name": "OFFICE", "words": ["STAPLE", "CLIP", "FOLDER", "BINDER"]},
    {"name": "KEYBOARD", "words": ["SHIFT", "ENTER", "CONTROL", "ESCAPE"]},
    {"name": "FABRIC", "words": ["FOLD", "CREASE", "BEND", "PLEAT"]},
    {"name": "PLANETS", "words": ["MARS", "VENUS", "EARTH", "SATURN"]},
    {"name": "CANDY", "words": ["MARS", "TWIX", "SNICKERS", "SMARTIES"]},
    {"name": "SMART PEOPLE", "words": ["SMARTIES", "GENIUS", "BRAIN", "WIZ"]},
    {"name": "WIZARD", "words": ["WIZ", "MAGE", "WITCH", "SORCERER"]}
]

# Shuffle the bank to make random combinations
random.shuffle(master_bank)

batches = {}
batch_counter = 1

# Group into games of 4 categories
for i in range(0, len(master_bank), 4):
    chunk = master_bank[i:i+4]
    if len(chunk) < 4: break
    
    # Assign difficulties arbitrarily for the game logic
    difficulties = ["Seed", "Red Herring", "Tricky", "Expert"]
    game_set = []
    for idx, cat in enumerate(chunk):
        game_set.append({
            "id": idx + (batch_counter * 100),
            "name": cat["name"],
            "words": cat["words"],
            "color": difficulties[idx]
        })
    batches[f"batch_{batch_counter:02d}"] = game_set
    batch_counter += 1

# Write to JSON
with open('master_category_bank.json', 'w') as f:
    json.dump({"batches": batches}, f, indent=2)

print(f"Generated {len(batches)} puzzles in master_category_bank.json")
