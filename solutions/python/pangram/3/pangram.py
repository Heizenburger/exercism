"""Module provides a function to determine if a sentence is a pangram."""

def is_pangram(sentence):
    all_alphabets = set("abcdefghijklmnopqrstuvwxyz")
    return all_alphabets.issubset(sentence.lower())