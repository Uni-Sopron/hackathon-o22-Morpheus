from wordhoard import Synonyms
from wordhoard.utilities.google_translator import Translator

def is_correct_guess(word: str, testword: str) -> bool:
    word = word.lower
    testword = testword.lower
    letters_to_check = ('á','é','í','ó','ö','ő','ú','ü','ű')
    letters_to_change_to = ('a','e','i','o','o','o','u','u','u')

    if  testword == word:
        return True
    else:
        letters = word
        for letter in letters_to_check:
            if letters.count(letter) != 0:
                letters[letters.index[letter]] = letters_to_change_to[letters_to_check.index[letter]]
        if letters == testword:
            return True
        else:
            translated_word = Translator(source_language='hu', str_to_translate=word).translate_word()
            synonyms = Synonyms(translated_word).find_synonyms()
            reverse_translations = []
            for synonym in synonyms:
                reverse_translated_word = Translator(source_language='hu', str_to_translate=synonym).reverse_translate()
                reverse_translations.append(reverse_translated_word)
            for synonym in reverse_translations:
                if synonym == testword:
                    return True
    return False