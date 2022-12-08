import requests
import xmltodict  # pip3 install xmltodict

def getSynonyms(szo: str) -> list:
    """Visszaadja egy szó szinonimait.
    >>> getSynonyms("zöldség")
    ['saláta', 'sötétség', 'ostobaság', 'hülyeség', 'butaság', 'marhaság', 'badarság', 'szamárság', 'csacsiság', 'bolondság', 'bárgyúság', 'korlátoltság', 'ökörség', 'együgyűség', 'stupiditás', 'blődség', 'sületlenség', 'rossz ötlet']
    >>> getSynonyms("cica")
    ['macska', 'kandúr', 'cirmos', 'cicus', 'cicmarek', 'cicamica', 'macskusz', 'cicuska', 'cicuka', 'macsek']
    >>> getSynonyms("slsdx")
    ['slsdx']
    >>> getSynonyms("ciica")
    ['ciica']
    >>> getSynonyms("apartman")
    ['fogadó', 'szálloda', 'hotel', 'szálló', 'motel', 'vendégfogadó', 'panzió', 'vendégház']
    >>> getSynonyms("ablak")
    ['nyílászáró']
    >>> getSynonyms("áll")
    ['található', 'elhelyezkedik', 'van', 'vár', 'nyugszik', 'várakozik', 'álldogál', 'rohad', 'vesztegel', 'ácsorog', 'malmozik', 'dekkol', 'szobrozik', 'rostokol', 'meg se moccan', 'nyugalomban van', 'nem halad', 'parkol', 'parkírozik', 'visel', 'bír', 'kibír', 'elvisel', 'tolerál', 'eltűr', 'benyel', 'tűr']

    Returns:
        list: Szinonimak listája.
    """
    link = f"https://api.poet.hu/szinonima.php?f=leon2001&j=a059763ea5256569f944d98b6d22c947&s={szo}"
    response = requests.get(link)
    content = xmltodict.parse(response.content)
    if "hiba" in list(content.keys()):
        return [szo]
    elif len(content["szinonimak"]["szocsoport"]) == 1:
        if isinstance(content["szinonimak"]["szocsoport"]["szinonima"], str): 
            return [content["szinonimak"]["szocsoport"]["szinonima"]]
        return content["szinonimak"]["szocsoport"]["szinonima"]

    synonyms = []
    for con in content["szinonimak"]["szocsoport"]:
        if isinstance(con["szinonima"], str):
            synonyms.append(con["szinonima"])
        else:
            synonyms.extend(con["szinonima"])
    return synonyms

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

def isOnlyOneLetterDiff(guess:str, word:str):
    """
    >>> isOnlyOneLetterDiff('tlma', 'alma')
    True
    >>> isOnlyOneLetterDiff('alma', 'alma')
    True
    >>> isOnlyOneLetterDiff('alka', 'alma')
    True
    >>> isOnlyOneLetterDiff('élka', 'alma')
    False
    >>> isOnlyOneLetterDiff('p', 'alma')
    False
    >>> isOnlyOneLetterDiff('tét', 'pók')
    False
    >>> isOnlyOneLetterDiff('tét', 'pék')
    False
    """
    isIn = False
    if len(guess) == len(word):
        for w in [guess[0:i:] + guess[i+1::] for i in range(len(guess))]:
            if w in [word[0:i:] + word[i+1::] for i in range(len(guess))]:
                isIn = True
    return isIn

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
        if letters == testword or letters == test_letters or isPlusOneLetter(word, testword) or isOnlyOneLetterDiff(word, testword):
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