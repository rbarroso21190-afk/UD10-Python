"""I. Capturar o no capturar?
8 0ZrZ0Z0Z
7 Z0l0Z0Z0
6 0ZrZ0Z0Z
5 Z0m0Z0Z0
4 0Z0O0Z0Z
3 Z0Z0A0Z0
2 0Z0Z0L0Z
1 Z0Z0Z0A0a b c d e f g h
Els escacs s´on un esport complex en el qual ex-
isteixen molts factors per determinar quin ju-
gador t´e avantatge en una posici´o. Un d’ells ´es
l’avantatge material, en el qual s’assigna un de-
terminat nombre de punts a cada tipus de pe¸ca.
Aleshores el jugador amb una major suma de punts
entre totes les seves peces t´e l’avantatge material.
Molts jugadors aficionats basen els seus c`alculs
en aquesta puntuaci´o a l’hora de determinar si
´es rendible capturar una pe¸ca i guanyar alguns
punts o si, al contrari, la pe¸ca pot ser recapturada
i acaben perdent punts.
Recentment, la famosa p`agina web d’escacs
chess.com ha estat treballant en els seus bots
d’escacs mensuals que seran publicats en el pr`oxim
mes de febrer. Quan falta un dia del llan¸cament,
el bot ´es capa¸c de detectar qualsevol pe¸ca enemiga
amena¸cada i determinar les peces atacants i defensores que cobreixen la seva posici´o. L’´unic problema ´es
que el darrer bot encara ´es incapa¸c de determinar si capturar la pe¸ca pot resultar profit´os per guanyar
avantatge material quan ´es el seu torn i est`a jugant amb blanques o si, al contrari, el pot fer perdre
avantatge material.
Com que la resta del teu equip de desenvolupament de la p`agina web chees.com est`a massa ocupat ara
mateix jugant a partides r`apides a 5 minuts els uns contra els altres, t’han encomanat a tu acabar el bot
per dem`a.
Entrada
L’entrada comen¸ca amb una l´ınia amb el nombre t de casos de prova que vendran a continuaci´o.
La primera l´ınia de cada cas de prova cont´e tres nombres enters n, m, k (1 ≤ n, m ≤ 5 · 105, 1 ≤ k ≤ 109)
que indiquen el valor k d’una pe¸ca negra que es troba amena¸cada, el nombre n de peces blanques que
l’ataquen i el nombre m de peces negres que la defensen.
La segona l´ınia cont´e n enters a1, a2, . . . , an (1 ≤ ai ≤ 109) amb els valors de les peces blanques que
ataquen la pe¸ca vulnerable. Les peces actuen una darrere l’altra: la primera pe¸ca blanca pot capturar i,
si ´es recapturada per una de negra, la seg¨uent blanca pot intervenir-hi, i aix´ı successivament.
La tercera l´ınia cont´e m enters b1, b2, . . . , bm (1 ≤ bi ≤ 109) amb els valors de les peces negres que defensen
la pe¸ca vulnerable. Les peces negres tamb´e actuen una darrere l’altra i segueixen la mateixa estrat`egia
que les blanques: si veuen que recapturant poden acabar perdent material, elles aturaran l’atac.
Com ´es habitual a les partides d’escacs, les blanques mouen primer i s´on les primeres que han de deter-
minar si volen capturar o no. En qualsevol moment tant les blanques com les negres poden aturar l’atac
i decidir no recapturar per evitar perdre material.
Sortida
Per a cada cas de prova, s’escriur`a una l´ınia amb un d’aquests tres missatges:
• dos signes d’exclamaci´o (!!) si capturar la pe¸ca ´es profit´os per a les blanques (´es a dir, acaben
guanyant avantatge material),
• dos signes d’interrogaci´o (??) si capturar causa una p`erdua d’avantatge material per a les blanques,
• si capturar resulta indiferent per a les blanques (no es guanya ni es perd avantatge material),
s’escriur`a !?.
Exemple
Entrada:
3
4 3 3
1 3 9 3
5 9 5
3 4 3
9 3 3
3 5 9 3
2 2 1
1 9
3 5
Sortida:
!!
??
!?
Subtasques
1. (4 punts) n = m = 1.
2. (34 punts) 1 ≤ n, m ≤ 1000.
3. (62 punts) 1 ≤ n, m ≤ 5 · 105."""