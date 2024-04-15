# 10. Feladat

## Leírás:

Készítsen  scriptet,  amely  futtatási  könyvtárában  és azok  alkönyvtáraiban  végignézi  az  összes  c
kiterjesztésű  C nyelvű  forráskódot,  és  kilistázza  azon  függvények  neveit (mindet  csak  egyszer),  amelyek
benne vannak egy előre megadott szótárállományban.

## A program tesztelése

A programot tesztelni úgy lehet, hogy ebben a mappában futtatjuk.

## A program futtatásának mikéntje

Miután a programot abba a mappába tettük, ahol a forrásfájlok vannak, a következő paranccsal tudjuk futtatni:

```bash
python ./main.py
```

## Függőségek telepítésének módja (pl. apt-get, pip)

Mint az előző pontban látszik a program futtatásához pythonra van szükség, így azt amennyiben nincs telepítve a gépünkre, az alábbi paranccsal telepíthetjük:

```bash
sudo apt-get install python
```

Emellett a kód maga csupán az `os` és a `re` modulokat használja, melyek alapértelmezetten telepítve vannak a pythonnal.

## Függőségek megbízhatósága (megfelelő támogatás, elég idős csomag, stb.)

Mivel a program a python alapmoduljait használja, így azok megbízhatóak.
A modulok megjelenésére nem találtam pontos időpontot, de az biztos, hogy a 2010-ben megjelent
python 2.7-ben már benne voltak.



