import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


#Removes all special characters, capital letters, and spaces between items.
def clean_text(text):
    text = text.casefold()
    valid_chars = string.ascii_letters + string.whitespace + string.digits
    cleaned_text = ""
    for char in text:
        if char in valid_chars:
            cleaned_text += char

    text = cleaned_text
    text = text.replace("\n", " ")
    text = text.lower()
    return text


def print_word_freq(filename):
    """Read in `file` and print out the frequency of words in that file."""
    with open("emancipation_proclamation.txt") as file:
        text = file.read()
    text = clean_text(text)
    words = []


    #Checks whether or not the word is in STOP WORDS or contains spaces, if it does, ignores them.
    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS:
            words.append(word)
    total_count = {}
    
    #Ascertains the total number of times a word was used and keeps it's number.
    for char in words:
        total_count[char] = total_count.get(char, 0) + 1

    word_freq = sorted(total_count.items(), key=lambda x: x[1], reverse=True)

    ordered_dict = dict(word_freq)

    for key, value in ordered_dict.items():
        print(key, " | ", value, " þ " * value)


print_word_freq("emancipation_proclamation.txt")
