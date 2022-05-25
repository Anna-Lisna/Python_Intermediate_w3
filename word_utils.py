def clean_punctuation(string):
    punctuation = ['.', ',', '/', '?', '!', ':', ';', '-', '`', '[', ']', '{', '}', '"', '(', ')', '_']
    clear_string = ''

    for str in string:
        if str not in punctuation:
            clear_string += str
    return clear_string


def list_words(string):
    clear_string = clean_punctuation(string)
    return clear_string.split()


def get_longest_word(string):
    longest = ''
    for word in list_words(string):
        if len(word) > len(longest):
            longest = word
    return longest
