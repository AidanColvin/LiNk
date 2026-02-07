import json

# 1. THE CATEGORY DATA
raw_data = [
    {"id": 1, "name": "FRUITS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["APPLE", "BANANA", "CHERRY", "GRAPE"]},
    {"id": 2, "name": "FRUITS SET 2", "difficulty": "Red Herring", "color": "#ADD8E6", "words": ["LEMON", "LIME", "MANGO", "PEACH"]},
    {"id": 3, "name": "FRUITS SET 3", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["PEAR", "PLUM", "KIWI", "MELON"]},
    {"id": 4, "name": "FRUITS SET 4", "difficulty": "Expert", "color": "#FFB6C1", "words": ["ORANGE", "PAPAYA", "BERRY", "FIG"]},
    {"id": 5, "name": "VEGETABLES SET 1", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["CARROT", "POTATO", "TOMATO", "ONION"]},
    {"id": 6, "name": "VEGETABLES SET 2", "difficulty": "Expert", "color": "#FFB6C1", "words": ["GARLIC", "CELERY", "PEPPER", "LETTUCE"]},
    {"id": 7, "name": "VEGETABLES SET 3", "difficulty": "Seed", "color": "#90EE90", "words": ["SPINACH", "BROCCOLI", "CABBAGE", "RADISH"]},
    {"id": 8, "name": "VEGETABLES SET 4", "difficulty": "Red Herring", "color": "#ADD8E6", "words": ["BEET", "TURNIP", "SQUASH", "PUMPKIN"]},
    {"id": 9, "name": "COLORS SET 1", "difficulty": "Seed", "color": "#90EE90", "words": ["RED", "BLUE", "GREEN", "YELLOW"]},
    {"id": 10, "name": "COLORS SET 2", "difficulty": "Red Herring", "color": "#ADD8E6", "words": ["PURPLE", "ORANGE", "PINK", "BROWN"]},
    {"id": 11, "name": "COLORS SET 3", "difficulty": "Tricky", "color": "#FFFFE0", "words": ["BLACK", "WHITE", "GRAY", "VIOLET"]},
    {"id": 12, "name": "COLORS SET 4", "difficulty": "Expert", "color": "#FFB6C1", "words": ["INDIGO", "CYAN", "MAGENTA", "TEAL"]}
]

# 2. THE DICTIONARY (Real definitions for the first few sets)
dictionary = {
    "APPLE": {"phon": "/ˈæp.əl/", "def": "A round fruit with red or green skin."},
    "BANANA": {"phon": "/bəˈnæn.ə/", "def": "A long curved fruit with yellow skin."},
    "CHERRY": {"phon": "/ˈtʃer.i/", "def": "A small, round, soft red or black fruit."},
    "GRAPE": {"phon": "/ɡreɪp/", "def": "A berry growing in clusters on a vine."},
    "LEMON": {"phon": "/ˈlem.ən/", "def": "A yellow, oval citrus fruit with thick skin."},
    "LIME": {"phon": "/laɪm/", "def": "A green, oval citrus fruit with acidic juice."},
    "MANGO": {"phon": "/ˈmæŋ.ɡəʊ/", "def": "An oval tropical fruit with yellow-red skin."},
    "PEACH": {"phon": "/piːtʃ/", "def": "A round fruit with juicy yellow flesh and downy skin."},
    "CARROT": {"phon": "/ˈkær.ət/", "def": "A long pointed orange root vegetable."},
    "POTATO": {"phon": "/pəˈteɪ.təʊ/", "def": "A starchy plant tuber that is cooked and eaten."},
    "TOMATO": {"phon": "/təˈmɑː.təʊ/", "def": "A glossy red, pulpy edible fruit eaten as a vegetable."},
    "ONION": {"phon": "/ˈʌn.jən/", "def": "A vegetable with a strong smell and flavor."}
}

# Auto-fill missing words with placeholders so the button always works
all_words = set()
for cat in raw_data:
    for w in cat["words"]:
        all_words.add(w)

for w in all_words:
    if w not in dictionary:
        dictionary[w] = {"phon":f"/{w.lower()}/", "def": "Definition currently unavailable."}

# 3. BUILD BATCHES
batches = {}
batch_counter = 1

for i in range(0, len(raw_data), 4):
    chunk = raw_data[i:i+4]
    if len(chunk) < 4: break
    
    batch_name = f"batch_{batch_counter:02d}"
    batches[batch_name] = chunk
    batch_counter += 1

# 4. SAVE OUTPUT
output = {
    "batches": batches,
    "dictionary": dictionary
}

with open("master_category_bank.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"✅ Generated {len(batches)} batches.")
print(f"✅ Generated dictionary for {len(dictionary)} words.")
