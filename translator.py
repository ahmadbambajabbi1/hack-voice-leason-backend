import csv
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from config import Config

# load custom vocabulary for fine-tuning mapping
vocab_map = {}
with open('vocab.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for eng, local, desc in reader:
        vocab_map[eng] = local

# load local fine-tuned model
tokenizer = AutoTokenizer.from_pretrained(Config.LLM_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(Config.LLM_PATH)

def translate(text):
    # apply vocab substitutions first
    for eng, local in vocab_map.items():
        text = text.replace(eng, local)
    inputs = tokenizer(text, return_tensors='pt')
    out = model.generate(**inputs)
    return tokenizer.decode(out[0], skip_special_tokens=True) 