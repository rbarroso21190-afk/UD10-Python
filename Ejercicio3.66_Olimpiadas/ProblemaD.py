"""D. Errors en matem`atiques
El nostre professor de matem`atiques t´e una manera particular de corregir els exercicis que han de tenir
un resultat num`eric. En lloc de puntuar la teva soluci´o, el que fa ´es anotar quants errors has com`es
segons la difer`encia entre els d´ıgits de la soluci´o correcta i la resposta donada. L’´unic que t´e en compte
´es que els d´ıgits de la soluci´o han d’apar`eixer a la resposta; per cada xifra que no hi aparegui ´es un punt
de penalitzaci´o, mentre que per cada xifra que sobri s´on 5 punts de penalitzaci´o.
Per exemple, si la soluci´o a un problema ´es 1224 i la resposta donada ´es 51205, la penalitzaci´o ´es 17: 2
punts perqu`e hi falten dues xifres (un 2 i un 4) i 15 punts perqu`e hi sobren tres xifres (dos 5 i un 0).
Ajuda el professor a comptar la penalitzaci´o de cada resposta.
Entrada i sortida
L’entrada consisteix en el nombre de problemes que ha de corregir el professor.
Cada cas de prova consisteix en quatre l´ınies: la primera l´ınia cont´e la longitud de la soluci´o; la segona, ´es
la soluci´o del problema de matem`atiques; la tercera l´ınia cont´e la longitud de la resposta de l’estudiant;
i la quarta l´ınia ´es la resposta de l’estudiant. Ni la soluci´o ni la resposta superen les 100 xifres.
La sortida consisteix en la penalitzaci´o de l’estudiant.
Exemple
Entrada:
3
4
1224
5
51205
4
1234
4
2341
4
1234
1
1
Sortida:
17
0
3
Restriccions
Les solucions i les respostes contindran ´unicament d´ıgits num`erics.
Subtasques
1. (6 punts) El programa funciona amb entrades de solucions i respostes de longitud 1.
2. (16 punts) El programa funciona amb entrades de solucions i respostes de longitud fins a 2 xifres.
3. (78 punts) El programa funciona amb entrades de solucions i respostes de longitud fins a 100 xifres."""