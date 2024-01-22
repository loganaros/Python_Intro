def print_upper_words(words, must_start_with):
    """Prints a list of all uppercase words"""

    for word in words:
        for letter in must_start_with:
            if word[0] == letter.casefold():
                print(word.upper())