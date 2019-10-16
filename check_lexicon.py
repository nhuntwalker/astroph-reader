import csv
import re

BASE_WORDS = '/usr/share/dict/words'
WORD_MAP = './word_map.csv'
SYMBOLS = './special_symbols.csv'

def check_lexicon(text: str) -> None:
    """Check which words aren't recognized by the machine's dictionary."""
    words = text.lower().split(' ')
    unknowns = []

    with open(BASE_WORDS) as ref_file:
        all_words = ref_file.readlines()
        word_ref = [word.lower().strip() for word in all_words]
    
    unknowns = [word for word in words if word not in word_ref]

    print(f"These are the words that aren't recognized: { unknowns }")


def remove_latex_fmt(text: str) -> str:
    """Remove latex symbols that don't have meaning for reading."""
    format_codes = [r'\\bf ', '~', '\$', r'\\it']
    for code in format_codes:
        text = re.sub(code, '', text)

    return text


def replace_special_symbols(text: str) -> str:
    """Replace special symbols with readable words."""
    with open(SYMBOLS) as csvfile:
        symbol_mappings = csv.reader(csvfile, delimiter=",")
        for mapping in symbol_mappings:
            text = re.sub(mapping[0], f" {mapping[1]} ", text)
    return text
    

def make_readable(text: str) -> str:
    """Make the text meaningfully readable by a machine."""
    words = replace_special_symbols(text).lower().split(' ')

    with open(WORD_MAP) as csvfile:
        known_mappings = csv.reader(csvfile, delimiter=',')
        mappings = {row[0]: row[1] for row in known_mappings}
    
    for idx, word in enumerate(words):
        if word in mappings:
            words[idx] = mappings[word]
    
    return ' '.join(words)