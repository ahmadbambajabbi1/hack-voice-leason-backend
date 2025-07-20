import csv
import re
import logging
from config import Config

# Setup logging
logging.basicConfig(level=logging.INFO)

# --- Load custom vocabulary mappings ----------------
def load_vocab(vocab_path='vocab.csv'):
    vocab_map = {}
    try:
        with open(vocab_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for eng, local, _ in reader:
                vocab_map[eng.strip().lower()] = local.strip()
    except Exception as e:
        logging.warning(f"Could not load vocab.csv: {e}")
    return vocab_map

vocab_map = load_vocab()
# Sort keys by descending length to match longest phrases first
sorted_phrases = sorted(vocab_map.keys(), key=len, reverse=True)

# --- Translation logic (mapping only) ----------------
def translate(text: str) -> str:
    """
    Translate `text` using exact-match mapping from vocab.csv.
    Any English phrase not in the CSV remains unchanged.
    """
    def replace_match(match):
        key = match.group(0).lower()
        return vocab_map.get(key, match.group(0))

    translated = text
    for phrase in sorted_phrases:
        # Use regex to replace whole phrase, case-insensitive
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        translated = pattern.sub(lambda m: replace_match(m), translated)

    return translated
