from spellchecker import SpellChecker

spell = SpellChecker(language='es')

def spelling_word(phrase):
    words = phrase.split()

    correct_pharse = [spell.correction(word) for word in words]

    return " ".join(correct_pharse)

print(spelling_word('Me guzta tu ermana'))