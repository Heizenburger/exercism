def is_pangram(sentence):
    all_alphabets = "abcdefghijklmnopqrstuvwxyz"
    sentence = [char.lower() for char in sentence if char.isalpha()]
    return set(sentence) == set(all_alphabets)