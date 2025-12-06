"""H. Paraules encadenades
En Biel i en Xesc solien jugar al joc de les paraules encadenades sempre que podien. Hi varen jugar tant
que es tornaren bon´ıssims jugant i ara les seves partides duren hores i hores, moltes vegades acaben sense
que cap dels dos guanyi per culpa d’una interrupci´o externa. A ning´u li agrada un joc en el qual no hi
ha guanyadors i, per solucionar aquest problema, han decidit canviar les normes del joc.
Normalment, el joc consisteix en jugadors que, per torns, diuen paraules reals, de manera que nom´es
es poden dir paraules que comencin per la lletra amb qu`e acabava la paraula anterior. Per exemple, si
el primer jugador escull pare, el segon jugador podria escollir elefant, per`o no animal. No es poden fer
servir paraules que ja s’han emprat i perd el primer jugador que ´es incapa¸c de continuar el joc. El primer
jugador pot triar la paraula que vulgui en el seu primer torn.
Com en Biel i en Xesc pr`acticament s’han apr`es de mem`oria el diccionari de tant jugar, han decidit
limitar les paraules que poden emprar, i utilitzar qualsevol llista de paraules que trobin, sense importar
el significat de les paraules. Per exemple, si estan en un restaurant, podrien jugar emprant les paraules
de la carta, o si estan en un aeroport, podrien limitar les paraules als noms dels distints dels vols.
En aquesta variant del joc, no t´e avantatge el jugador que conegui m´es paraules, la t´e el jugador que
esculli paraules de la millor manera possible.
Com hi ha moltes menys paraules, les partides sempre acaben amb un guanyador. En Biel i en Xesc
s’han adonat que, si es coneix la llista de paraules, es pot determinar quin jugador guanyar`a la partida
si tots dos fan els millors moviments possibles. Per exemple, si la llista de paraules ´es {aigua, aura},
sempre guanyar`a el segon jugador, sense importar les decisions que faci el primer jugador.
En Biel i en Xesc t’han demanat que escriguis un programa que sigui capa¸c de determinar el guanyador
d’una partida, donada la seva llista de paraules. Aix´ı es poden riure l’un de l’altre quan qualc´u perdi
una partida que hauria d’haver guanyat.
Entrada i sortida
L’entrada comen¸ca amb un nombre N que representa el nombre de partides que s’han d’analitzar.
A continuaci´o apareixen N casos de prova. Un cas de prova comen¸ca per una l´ınia amb un nombre X
major que 0, que representa el nombre de paraules de la llista de paraules del cas de prova. A la l´ınia
seg¨uent hi apareixen les X paraules, separades per espais i escrites en lletres min´uscules de l’alfabet angl`es
(sense accents ni ’˜n’ o ’¸c’).
Per a cada cas de prova s’ha d’imprimir el nom del jugador que pot garantir la seva vict`oria. Si ´es el
primer jugador, s’ha d’imprimir Biel, si ´es el segon, Xesc. Les respostes han d’estar en l´ınies diferents.
Exemple
Entrada:
5
2
sebas sopes
1
tomatiga
2
pilota aigua
3
menjar eminem riure
2
pluja emerit
Sortida:
Xesc
Biel
Biel
Biel
Biel
Restriccions
La longitud m`axima de les paraules ´es de 10 car`acters.
Subtasques
1. (1 punt) Funciona per casos amb llistes de paraules d’1 sola paraula (X = 1).
2. (6 punts) Funciona per casos amb llistes de paraules de 2 o menys paraules (X ≤ 2).
3. (17 punts) Funciona per casos amb llistes de paraules de 4 o menys paraules (X ≤ 1).
4. (76 punts) Funciona per casos amb llistes de paraules de 20 o menys paraules (X ≤ 20)."""