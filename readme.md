# Álmodj velem

## Futattás:
```bash
python3 main.py
```

## Legfontosabb fejlesztési lehetőségek
- is_guess_checker-be beleépíteni az egy betűs eltérés logikákat
- Annyi kör ahány játékos van és mindenki egyszer lehet álmodó!!! -> randomRoles(), round() függvények újra gondolása -> egy listában eltárolni ki volt álmodó és az illető nem lehet már -> Addig menjenek a körök míg ez az voltak már álmodók lista olyan hosszú nem lesz, mint a játékosok listája vagy fordított logika és addig amíg nem üres a lista
- JAVÍTVA! Egyel kevesebb kártyát jelenít meg a tkinter bug fixálása
- Játékosok megadása játékmester nélkül -> minidg leül valaki megadja nevét kap egy szerepet, utána a következő ember
- JAVÍTVA! játék közben a szavak jobb és baloldalra szeparálódjanak attól függően, hogy jó-e a tipp
- Játékosok megadása tkinter felületen
- pontozás kiírása tkinter felületen
- A végén az álmodó elmondja, hogy mire emlékszik. Erre lehetne checkboxos felület pl, hogy miket tudott felidézni
- Egy kis menü tkinteren/consolon, ahol választhatsz, hogy új játék kezdete, játékosok felvitele, stb.
- Egyszerűsíteni lehetne git mappán meg a kódon (tesztelő printek kiszedése), hogy átláthatóbb legyen -> felesleges dolgokat kidobni pl.: rar. vagy mappába, fájlba szervezni az egy séma alá tartozó elemeket.

## Még menő lenne megcsinálni
- Egy timer beállítása egy körre
- Követni az utalásokat, amiket az álmodónak mondanak és vizsgálni, hogy szabályosak-e
- Több külöböző gépen játszani servert futattva
