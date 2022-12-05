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

if __name__ == "__main__":
    import doctest
    doctest.testmod()