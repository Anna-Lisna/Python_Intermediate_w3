from word_utils import clean_punctuation, list_words, get_longest_word

string = 'Namespaces? - are one honking great idea -- let\'s do more of those!'

print(clean_punctuation(string))
print(list_words(string))
print(get_longest_word(string))
