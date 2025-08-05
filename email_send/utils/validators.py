import re

DIGIT_WORDS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def spoken_to_email(spoken):
    replacements = {
        " at ": " @ ",
        " dot ": " . ",
        " underscore ": " _ ",
        " dash ": " - ",
        " plus ": " + "
    }

    # Normalize case
    spoken = spoken.lower()

    # Replace common spoken symbols
    for word, symbol in replacements.items():
        spoken = spoken.replace(word, symbol)

    # Convert digit words to numbers
    for word, digit in DIGIT_WORDS.items():
        spoken = re.sub(rf"\b{word}\b", digit, spoken)

    # Remove all whitespace
    spoken = re.sub(r"\s+", "", spoken)

    # If '@' is missing, assume Gmail
    if '@' not in spoken:
        spoken += "@gmail.com"

    return spoken

def is_valid_email(email):
    # Basic format check
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email) is not None
