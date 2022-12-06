from wordhoard import Synonyms
from wordhoard.utilities.google_translator import Translator

def is_correct_guess(word: str, testword: str) -> bool:
    word = word.lower()
    testword = testword.lower()
    letters_to_check = ('á','é','í','ó','ö','ő','ú','ü','ű')
    letters_to_change_to = ('a','e','i','o','o','o','u','u','u')

    if  testword == word:
        return True
    else:
        letters = word
        test_letters = testword
        for letter in letters_to_check:
            if letters.count(letter,0,len(letters)) != 0:
                index = letters_to_check.index(letter)
                letters = letters.replace(letters_to_check[index], letters_to_change_to[index])
            if test_letters.count(letter,0,len(test_letters)) != 0:
                index = letters_to_check.index(letter)
                test_letters = test_letters.replace(letters_to_check[index], letters_to_change_to[index])
        if letters == testword or letters == test_letters:
            return True
        else:
            translated_word = Translator(source_language='hu', str_to_translate=word).translate_word()
            translated_testword = Translator(source_language='hu', str_to_translate=testword).translate_word()
            synonyms = Synonyms(translated_word, max_number_of_requests=24).find_synonyms()
            for synonym in synonyms:
                if synonym == translated_testword:
                    return True
    return False
