"""E. Les p`agines del diccionari
N’Abra¸cabassiots ha apr`es avui a l’escola a fer servir el diccionari. Li han explicat com estan ordenades
les paraules. Tamb´e li han ensenyat que en un diccionari estan escrites a les cantonades superiors de cada
p`agina la primera i la darrera paraula que apareixen en aquella p`agina, per aix´ı poder trobar qualsevol
paraula molt m´es r`apidament.
N’Abra¸cabassiots est`a encantat amb aquest descobriment i ha decidit posar en pr`actica aquesta t`ecnica
amb la seva amiga Miralunars amb un nou i divertit joc: na Miralunars dir`a una paraula a l’atzar i
n’Abra¸cabassiots ha d’endevinar a quina p`agina del diccionari es troba, consultant nom´es les paraules de
la cantonada de cada p`agina.
Entrada i sortida
Aquest ´es un problema interactiu. Has de refrescar la sortida cada vegada que imprimeixis dades
(cout << endl o cout << flush en C++, System.out.flush() en Java, stdout.flush() en Python).
L’entrada comen¸ca amb una l´ınia amb un nombre enter N que indica el nombre de p`agines que t´e el
diccionari, un nombre enter M amb el nombre m`axim de consultes que es poden fer i una cadena de
car`acters amb la paraula que ha de trobar n’Abra¸cabassiots.
Per fer una consulta sobre la p`agina n del diccionari (1 ≤ n ≤ N ), el programa escriur`a una l´ınia a la
sortida est`andard amb el format ? n i llegir`a una l´ınia de l’entrada est`andard amb dues cadenes de
car`acters separades per un espai, que representen la primera i la darrera paraula que apareixen en aquella
p`agina, respectivament.
Per donar una resposta amb el nombre de p`agina r on es troba la paraula que cercam, s’escriur`a una
l´ınia amb el format ! r. Aquesta interacci´o no compta com una de les M consultes que es poden fer
amb la m`aquina.
Exemple
Entrada:
3 3 diccionari
java python
abella jas
Sortida:
? 2
? 1
! 1
Restriccions
Totes les paraules s´on en min´uscules i tenen, com a molt, 20 car`acters. Nom´es es fa servir l’alfabet angl`es,
per tant, no hi apareixeran car`acters com la ‘˜n’, ‘¸c’ o vocals amb accents.
Es garanteix que la paraula a cercar no es troba entre la darrera paraula d’una p`agina i la primera paraula
de la p`agina seg¨uent, ´es a dir, sempre es trobar`a dins una p`agina del diccionari.
Subtasques
1. (7 punts) 1 ≤ N = M ≤ 10.
2. (33 punts) 1 ≤ N = M ≤ 1000.
3. (60 punts) 1 ≤ N ≤ 105; M = 100."""