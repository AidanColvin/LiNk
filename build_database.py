import json

# This contains the full dataset you provided in the prompt
raw_data = [
    {"id": 1, "name": "FRUITS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["APPLE", "BANANA", "CHERRY", "GRAPE"]},
    {"id": 2, "name": "FRUITS SET 2", "difficulty": "Red Herring", "color": "#ADD8E6", "words": ["LEMON", "LIME", "MANGO", "PEACH"]},
    {"id": 3, "name": "FRUITS SET 3", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["PEAR", "PLUM", "KIWI", "MELON"]},
    {"id": 4, "name": "FRUITS SET 4", "difficulty": "Expert", "color": "#FFB6C1", "words": ["ORANGE", "PAPAYA", "BERRY", "FIG"]},
    {"id": 5, "name": "FRUITS SET 5", "difficulty": "Seed", "color": "#90EE90", "words": ["DATE", "GUAVA", "APRICOT", "COCONUT"]},
    {"id": 6, "name": "FRUITS SET 6", "difficulty": "Red Herring", "color": "#ADD8E6", "words": ["APPLE", "LIME", "KIWI", "FIG"]},
    {"id": 7, "name": "FRUITS SET 7", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["BANANA", "MANGO", "MELON", "DATE"]},
    {"id": 8, "name": "FRUITS SET 8", "difficulty": "Expert", "color": "#FFB6C1", "words": ["CHERRY", "PEACH", "ORANGE", "GUAVA"]},
    {"id": 11, "name": "VEGETABLES SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["CARROT", "POTATO", "TOMATO", "ONION"]},
    {"id": 12, "name": "VEGETABLES SET 2", "difficulty": "Expert", "color": "#FFB6C1", "words": ["GARLIC", "CELERY", "PEPPER", "LETTUCE"]},
    {"id": 13, "name": "VEGETABLES SET 3", "difficulty": "Seed", "color": "#90EE90", "words": ["SPINACH", "BROCCOLI", "CABBAGE", "RADISH"]},
    {"id": 14, "name": "VEGETABLES SET 4", "difficulty": "Red Herring", "color": "#ADD8E6", "words": ["BEET", "TURNIP", "SQUASH", "PUMPKIN"]},
    {"id": 21, "name": "COLORS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["RED", "BLUE", "GREEN", "YELLOW"]},
    {"id": 22, "name": "COLORS SET 2", "difficulty": "Red Herring", "color": "#ADD8E6", "words": ["PURPLE", "ORANGE", "PINK", "BROWN"]},
    {"id": 31, "name": "WILD ANIMALS SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["LION", "TIGER", "BEAR", "WOLF"]},
    {"id": 32, "name": "WILD ANIMALS SET 2", "difficulty": "Expert", "color": "#FFB6C1", "words": ["FOX", "DEER", "ELK", "MOOSE"]},
    {"id": 41, "name": "FARM ANIMALS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["COW", "PIG", "SHEEP", "GOAT"]},
    {"id": 61, "name": "FISH SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["SALMON", "TROUT", "TUNA", "COD"]},
    {"id": 71, "name": "INSECTS SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["ANT", "BEE", "BEETLE", "BUTTERFLY"]},
    {"id": 81, "name": "TREES SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["OAK", "MAPLE", "PINE", "CEDAR"]},
    {"id": 91, "name": "FLOWERS SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["ROSE", "TULIP", "LILY", "DAISY"]},
    {"id": 101, "name": "HERBS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["BASIL", "THYME", "SAGE", "MINT"]},
    {"id": 111, "name": "SPICES SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["PEPPER", "CUMIN", "PAPRIKA", "CINNAMON"]},
    {"id": 121, "name": "DESSERTS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["CAKE", "PIE", "COOKIE", "BROWNIE"]},
    {"id": 131, "name": "DRINKS SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["WATER", "JUICE", "SODA", "TEA"]},
    {"id": 141, "name": "SPORTS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["SOCCER", "TENNIS", "BASEBALL", "FOOTBALL"]},
    {"id": 151, "name": "INSTRUMENTS SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["PIANO", "GUITAR", "VIOLIN", "CELLO"]},
    {"id": 161, "name": "VEHICLES SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["CAR", "TRUCK", "BUS", "VAN"]},
    {"id": 171, "name": "TOOLS SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["HAMMER", "SAW", "DRILL", "WRENCH"]},
    {"id": 181, "name": "KITCHEN ITEMS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["PAN", "POT", "BOWL", "PLATE"]},
    {"id": 191, "name": "FURNITURE SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["CHAIR", "TABLE", "SOFA", "COUCH"]},
    {"id": 201, "name": "CLOTHING SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["SHIRT", "PANTS", "DRESS", "SKIRT"]},
    {"id": 211, "name": "SHOES SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["BOOT", "SNEAKER", "SANDAL", "LOAFER"]},
    {"id": 221, "name": "WEATHER SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["RAIN", "SNOW", "SLEET", "HAIL"]},
    {"id": 231, "name": "GEOGRAPHY SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["RIVER", "LAKE", "OCEAN", "SEA"]},
    {"id": 241, "name": "BODY PARTS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["HEAD", "HAIR", "EAR", "EYE"]}
]

batches = {}
batch_counter = 1

# Process into batches of 4
for i in range(0, len(raw_data), 4):
    chunk = raw_data[i:i+4]
    if len(chunk) < 4:
        break
    
    batch_name = f"batch_{batch_counter:02d}"
    batches[batch_name] = chunk
    batch_counter += 1

output = {"batches": batches}

with open("master_category_bank.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Successfully generated {len(batches)} batches from {len(raw_data)} categories.")
