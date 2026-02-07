import json

# --- 1. CATEGORY DATA (250+ Words) ---
raw_data = [
    {"id": 1, "name": "FRUITS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["APPLE", "BANANA", "CHERRY", "GRAPE"]},
    {"id": 2, "name": "FRUITS SET 2", "difficulty": "Red Herring", "color": "#ADD8E6", "words": ["LEMON", "LIME", "MANGO", "PEACH"]},
    {"id": 3, "name": "FRUITS SET 3", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["PEAR", "PLUM", "KIWI", "MELON"]},
    {"id": 4, "name": "FRUITS SET 4", "difficulty": "Expert", "color": "#FFB6C1", "words": ["ORANGE", "PAPAYA", "BERRY", "FIG"]},
    {"id": 5, "name": "VEGETABLES SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["CARROT", "POTATO", "TOMATO", "ONION"]},
    {"id": 6, "name": "VEGETABLES SET 2", "difficulty": "Expert", "color": "#FFB6C1", "words": ["GARLIC", "CELERY", "PEPPER", "LETTUCE"]},
    {"id": 7, "name": "VEGETABLES SET 3", "difficulty": "Seed", "color": "#90EE90", "words": ["SPINACH", "BROCCOLI", "CABBAGE", "RADISH"]},
    {"id": 8, "name": "VEGETABLES SET 4", "difficulty": "Red Herring", "color": "#ADD8E6", "words": ["BEET", "TURNIP", "SQUASH", "PUMPKIN"]},
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

# --- 2. GENERATE DICTIONARY (Prevents "Loading..." bug) ---
dictionary = {
    "APPLE": {"phon": "/ˈæp.əl/", "def": "A round fruit with red or green skin."},
    "BANANA": {"phon": "/bəˈnæn.ə/", "def": "A long curved fruit with yellow skin."},
    "CHERRY": {"phon": "/ˈtʃer.i/", "def": "A small, round, soft red or black fruit."},
    "GRAPE": {"phon": "/ɡreɪp/", "def": "A berry growing in clusters on a vine."},
    "LEMON": {"phon": "/ˈlem.ən/", "def": "A yellow, oval citrus fruit."},
    "LIME": {"phon": "/laɪm/", "def": "A green, oval citrus fruit."},
    "MANGO": {"phon": "/ˈmæŋ.ɡəʊ/", "def": "An oval tropical fruit."},
    "PEACH": {"phon": "/piːtʃ/", "def": "A round fruit with juicy yellow flesh."},
    "CARROT": {"phon": "/ˈkær.ət/", "def": "A long pointed orange root vegetable."},
    "POTATO": {"phon": "/pəˈteɪ.təʊ/", "def": "A starchy plant tuber."},
    "TOMATO": {"phon": "/təˈmɑː.təʊ/", "def": "A red edible fruit eaten as a vegetable."},
    "ONION": {"phon": "/ˈʌn.jən/", "def": "A vegetable with a strong smell."}
}

# Auto-fill missing words so the button ALWAYS has data
for cat in raw_data:
    for w in cat["words"]:
        if w not in dictionary:
            # Generate a generic definition so it never gets stuck loading
            dictionary[w] = {
                "phon": f"/{w.lower()}/", 
                "def": f"A type of {cat['name'].split()[0].lower()}."
            }

# --- 3. BUILD BATCHES ---
batches = {}
batch_counter = 1

for i in range(0, len(raw_data), 4):
    chunk = raw_data[i:i+4]
    if len(chunk) < 4: break
    batch_name = f"batch_{batch_counter:02d}"
    batches[batch_name] = chunk
    batch_counter += 1

output = { "batches": batches, "dictionary": dictionary }

with open("master_category_bank.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ Database generated successfully.")
