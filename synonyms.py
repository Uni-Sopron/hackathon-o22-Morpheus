import requests
import xmltodict # pip3 install xmltodict

def getSynonyms(szo:str) -> list:
    """Visszaadja egy szó szinonimait.
    
    Returns:
        list: Szinonimak listája.
    """
    link = f"https://api.poet.hu/szinonima.php?f=leon2001&j=a059763ea5256569f944d98b6d22c947&s={szo}"
    response = requests.get(link)
    content = xmltodict.parse(response.content)
    if 'hiba' in list(content.keys()):
        return [szo]
    return content["szinonimak"]["szocsoport"]["szinonima"]

#print(getSynonyms("cica"))