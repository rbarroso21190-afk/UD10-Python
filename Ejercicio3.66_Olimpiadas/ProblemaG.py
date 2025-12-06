"""G. La ruta m´es eficient
N’Armando Guerra Segura, estudiant d’Enginyeria Inform`atica a la UIB, arriba sovint tard a la seva classe
d’An`alisi de Dades a les 8:30 a causa de problemes de tr`ansit. Per solucionar-ho, ha decidit desenvolupar
una aplicaci´o m`obil basada en una API de la DGT de Mallorca, que proporciona informaci´o sobre rutes,
velocitat permesa, dist`ancia i retard pel tr`ansit. L’aplicaci´o calcula la millor ruta perqu`e n’Armando
arribi a classe al m´es a prop possible de les 8:30 i evitar tamb´e arribar massa prest per no haver d’esperar
innecess`ariament.
Entrada i sortida
L’entrada del problema cont´e una primera l´ınia amb el nombre de casos a analitzar. Despr´es, per a cada
cas de prova:
1. Hora de sortida en format hh:mm (24 hores), compresa en el rang de 06:00 a 08:20.
2. Nombre de rutes N (0 ≤ N ≤ 1, 000).
3. Per a cada ruta, una l´ınia amb els atributs seg¨uents separats per espais:
• StrCodi: codi de la carretera (cadena de car`acters).
• tempsN ormal: temps normal en minuts per arribar des de casa seva a la Universitat per
aquesta carretera (enter).
• timeDelay: retard en minuts a causa del tr`ansit (enter).
La sortida per a cada cas de prova ha de ser o b´e el codi de la carretera de la ruta que permeti n’Armando
arribar al m´es a prop possible de les 8:30, o b´e, si cap ruta li permet arribar a temps, el text NO ARRIBA.
Exemple
Entrada:
2
06:00 4
MA-01 35 45
MA-11 45 75
MA-19 60 85
MA-30 55 93
08:20 2
MA-01 75 3
MA-10 40 1
Sortida:
MA-30
NO ARRIBA
Restriccions
Els atributs compleixen les condicions seg¨uents: StrCodi ∈ String, tempsN ormal, timeDelay ∈ Natural.
Subtasques
1. (10 punts) Pot comprovar 200 carreteres.
2. (15 punts) Pot comprovar 400 carreteres.
3. (75 punts) Pot comprovar 1000 carreteres."""