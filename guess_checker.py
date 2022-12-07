from synonyms import getSynonyms

def isPlusOneLetter(guess:str, word:str) -> bool:
    """Megvizsgája, hogy ha egy beűvel hosszabb-e a szó és a plusz betű nélkül megegyezik-e az eredetivel
    >>> isPlusOneLetter('allma', 'alma')
    True
    >>> isPlusOneLetter('távirrányító', 'távirányító')
    True
    >>> isPlusOneLetter('szék', 'asztal')
    False
    >>> isPlusOneLetter('távirrrányító', 'távirányító')
    False
    """
    if len(guess) == len(word)+1:
        return word in [guess[0:i:] + guess[i+1::] for i in range(len(guess))]
    return False

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
            synonyms = getSynonyms(word)
            for synonym in synonyms:
                if synonym == testword:
                    return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()