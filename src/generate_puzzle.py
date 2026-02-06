import json
import random

# --- YOUR DATA GOES HERE ---
# Add as many categories as you want. The script will handle the math.
raw_categories = [
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
    {"name": "FABRIC", "words": ["FOLD", "CREASE", "BEND", "PLEAT"]}
]

# --- AUTO-BATCHING ENGINE ---
batches = {}
batch_counter = 1

# Shuffle raw data so games are different every time you generate
random.shuffle(raw_categories)

# Process in chunks of 4
for i in range(0, len(raw_categories), 4):
    chunk = raw_categories[i:i+4]
    
    # If we have less than 4 left (e.g., only 2 categories remaining), stop.
    # You need 4 categories to make a valid game.
    if len(chunk) < 4:
        break
        
    # Assign difficulty colors (Arbitrary for now, just to make it work)
    difficulties = ["Seed", "Red Herring", "Tricky", "Expert"]
    
    game_set = []
    for idx, cat in enumerate(chunk):
        game_set.append({
            "id": idx + (batch_counter * 100), # Unique ID
            "name": cat["name"],
            "words": cat["words"],
            "color": difficulties[idx]
        })
    
    batch_name = f"batch_{batch_counter:02d}"
    batches[batch_name] = game_set
    batch_counter += 1

# Export
output = {"batches": batches}
with open('master_category_bank.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"Success! Generated {len(batches)} playable games in master_category_bank.json")