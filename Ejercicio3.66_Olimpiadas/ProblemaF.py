"""F. El laberint
Segons la mitologia grega, D`edal va construir un laberint per amagar-hi el minotaure. El nostre benvolgut
arque`oleg i explorador Indiana Jones est`a investigant aquest mite. Per a la seva sorpresa, el mite ´es real,
existeix un laberint.
Afortunadament, el minotaure no ´es real, per`o el laberint en si mateix ´es un parany. Les parets cauen i
camins que abans eren transitables ara ja no ho s´on. El laberint s’est`a enfonsant!
Ajuda n’Indiana a trobar el cam´ı m´es curt cap a la sortida del laberint. Si ´es que realment pot escapar-ne...
Entrada
La primera l´ınia cont´e un n´umero N que indica la quantitat de casos de prova.
Cada cas de prova t´e una l´ınia inicial amb dos n´umeros H i W, que indiquen l’altura i l’amplada del
laberint, respectivament.
A continuaci´o es descriu el laberint en H l´ınies, cadascuna de W car`acters. Els possibles car`acters s´on:
• X indica que hi ha una paret (no es pot travessar).
• S (start) indica la posici´o inicial de l’explorador.
• F (finish) la posici´o de la sortida.
• Un punt (.) indica que ´es una zona transitable.
Sortida
La soluci´o de cada cas de prova ha d’imprimir-se en una l´ınia diferent, que ha de ser o b´e un n´umero que
indica la quantitat m´ınima de passes que ha de fer l’explorador per aconseguir sortir del laberint, o b´e el
text IMPOSSIBLE SORTIR si no es pot trobar cap cam´ı cap a la sortida.
Exemple
Entrada:
3
3 5
XXXXX
XS.FX
XXXXX
7 7
XXXXXXX
X.....X
X.X.X.X
X.XF..X
XSXXX.X
X.....X
XXXXXXX
3 7
XXXXXXX
XS.X.FX
XXXXXXX
Sortida:
2
7
IMPOSSIBLE SORTIR
Restriccions
• H i W sempre s´on major o iguals que 3 i menor o iguals que 100.
• Les vores dels laberints sempre seran X.
• Tots els laberints tenen una ´unica S i F.
Subtasques
1. (11 punts) Els laberints tenen un ´unic cam´ı possible cap a la sortida, amb H i W menor o iguals
que 10.
2. (37 punts) Els laberints poden tenir diversos camins cap a la sortida o no tenir-ne cap, amb H i W
menor o iguals que 10.
3. (52 punts) Els laberints no tenen restriccions addicionals"""