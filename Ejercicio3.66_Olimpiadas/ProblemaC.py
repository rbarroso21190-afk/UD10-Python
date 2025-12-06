"""C. Joc dels cavalls
Els escacs, amb milers d’anys d’antiguitat, s´on considerats un esport mental per la complexitat a la qual
poden arribar les partides: l’estrat`egia ho ´es tot per guanyar en aquest joc.
Els escacs es juguen en un tauler de 8 × 8 caselles numerades d’esquerra a dreta amb les primeres 8 lletres
de l’alfabet en maj´uscula (A-H) i de baix a dalt per n´umeros de l’1 al 8.
La pe¸ca del cavall crida especialment l’atenci´o per ser l’´unica que no es despla¸ca en l´ınia recta, sin´o en
L, aix´ı que ´es f`acil equivocar-se en moure’l. Per aquest motiu, volem fer un sistema que comprovi que els
moviments realitzats per un cavall s´on correctes.
Entrada i sortida
La primera l´ınia cont´e un nombre N que indica la quantitat de casos de prova.
El cas de prova consisteix en dues l´ınies: la primera cont´e un n´umero major o igual a 1 que indica quants
moviments du a terme el cavall. La segona cont´e una seq¨u`encia de caselles en el format A1, separades
per espais, que indiquen la seq¨u`encia de moviments. La primera casella ´es on comen¸ca el cavall.
La sortida haur`a d’indicar la validesa de la seq¨u`encia de moviments amb Valid o Invalid.
Exemple
Entrada:
3
1
A1 B3
4
C2 B4 A7 C6 E7
3
F2 G4 E5 F7
Sortida:
Valid
Invalid
Valid
Restriccions
El tauler sempre ser`a de les dimensions originals 8 × 8.
Subtasques
1. (9 punts) El cavall comen¸ca a la casella D4 i fa un sol moviment.
2. (35 punts) El cavall comen¸ca a qualsevol casella i fa un sol moviment
3. (56 punts) El cavall comen¸ca a qualsevol casella i pot fer fins a 100 moviments."""