"""B. Tit´ı em va preguntar, Amor o Amol?
El cantant Bad Bunny vol treure el seu pr`oxim `album. No obstant aix`o, s’enfronta a un problema peculiar:
cada vegada que intenta escriure les seves can¸cons amb l’ordinador, les tecles R i L fallen, i intercanvien
misteriosament les seves funcions.
Bad Bunny no podia permetre’s deixar els seus versos en aquest estat; en cas contrari, els seus fans podrien
deixar de ser-li fidel i comen¸carien a seguir altres artistes, fins i tot de g`eneres musicals completament
diferents. No obstant aix`o, despr´es de llegir els desastrosos versos de les seves can¸cons detingudament, es
va adonar d’una cosa inesperada: l’´unica paraula amb l’error que mantenia una rima perfecta i aconseguia
transmetre amb claredat l’emoci´o desitjada era Amor, que apareixia escrita com a Amol. Per aix`o, ha
decidit que Amor i qualsevol altra paraula que la contengui com ara enamorar, amorf o Zamora han de
romandre amb l’error.
A m´es, a Bad Bunny a vegades li agrada alternar maj´uscules i min´uscules en les lletres de les seves
can¸cons, com en l’exemple seg¨uent:
VurR donaL AmoL i fERiCiTat
i el vers corregit seria:
VulL donaR AmoL i fELiCiTat
Ajuda el cantant Bad Bunny a corregir la lletra de les seves can¸cons perqu`e pugui interpretar-les correc-
tament.
Entrada i sortida
L’entrada consisteix en el nombre de casos de prova N , que ´es la quantitat de frases a corregir. A
continuaci´o, cada cas de prova consisteix en una l´ınia de car`acters alfab`etics amb espais. Per simplificar,
no hi apareixen car`acters amb accents ni car`acters especials.
La sortida consisteix en la frase d’entrada corregida i amb la mateixa longitud de car`acters.
Exemple
Entrada:
4
enamolalme
peL a Res envejoses pau i amoL
jo Nomes em DeiXO polTal DeR teu somLiuLe
Ra teva LiaRRa es RA miRRoL medecinA
Sortida:
enamolarme
peR a Les envejoses pau i amoL
jo Nomes em DeiXO porTar DeL teu somRiuRe
La teva RiaLLa es LA miLLoR medecinA
Restriccions
El nombre m`axim de car`acters en una l´ınia ´es 80.
Subtasques
1. (4 punts) Les frases no contenen errors, per la qual cosa no es fan canvis, tot en min´uscules.
2. (13 punts) Totes les L err`onies es corregeixen a R, tot en min´uscules.
3. (13 punts) Totes les R err`onies es corregeixen a L, tot en min´uscules.
4. (35 punts) Les frases contenen errors en totes dues lletres (L i R) intercanviades, tot en min´uscules,
i es corregeixen excepte per a les paraules que contenen Amor.
5. (35 punts) Les frases contenen errors en totes dues lletres (L i R) intercanviades. Les paraules estan
en una combinaci´o de maj´uscules i min´uscules. El programa ha de corregir els errors i la sortida
ha de mantenir el mateix format que l’entrada (espais, maj´uscules i min´uscules)."""