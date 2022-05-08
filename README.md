### Barem comun

**Linkuri utile**

- <https://repl.it/@IrinaCiocan/cautare-BFDFDFI-complet#main.py>
- <https://repl.it/@IrinaCiocan/uniform-cost-search#main.py>
- <https://repl.it/@IrinaCiocan/a-star#main.py>
- <https://replit.com/@IrinaCiocan/a-star-optimizat#main.py>
- <https://replit.com/@IrinaCiocan/ida-star#main.py>
- <https://repl.it/@IrinaCiocan/problemablocurilor#main.py> (E implementat cu BF si A*)
- <https://replit.com/@IrinaCiocan/8-puzzle#main.py>
- <https://repl.it/@IrinaCiocan/exemplu-afisare-timp-folosit> (cum calculam timpul de executie a unei secvente de cod)
- <https://repl.it/@IrinaCiocan/problema-canibalilor-si-misionarilor#main.py>
- <https://repl.it/@IrinaCiocan/exemplu-iterare-prin-folder>
- <http://irinaciocan.ro/inteligenta_artificiala/python-comprehensions.php> la secțiunea cu argumentele programului, respectiv timeout
- <http://irinaciocan.ro/inteligenta_artificiala/cum-rezolvam-o-problema.php> modul general de abordare a unei probleme

**Barem** (punctajul e dat in procentaje din punctajul maxim al temei; procentajul maxim este 100%):

1. (5%)Fișierele de input vor fi într-un folder a cărui cale va fi dată în linia de comanda. În linia de comandă se va da și calea pentru un folder de output în care programul va crea pentru fiecare fișier de input, fișierul sau fișierele cu rezultatele. Tot în linia de comandă se va da ca parametru și numărul de soluții de calculat (de exemplu, vrem primele NSOL=4 soluții returnate de fiecare algoritm). Ultimul parametru va fi timpul de timeout. Se va descrie în documentație forma în care se apelează programul, plus 1-2 exemple de apel.
2. (5%) Citirea din fisier + memorarea starii. Parsarea fișierului de input care respectă formatul cerut în enunț
3. (15%) Functia de generare a succesorilor
4. (5%) Calcularea costului pentru o mutare
5. (5%) Testarea ajungerii în starea scop (indicat ar fi printr-o funcție de testare a scopului). Atenție, acolo unde nu se precizează clar în fișierul de intrare o stare finală înseamnă că funcția de testare a scopului doar verifică niște condiții precizate în enunț. Nu se va rezolva generând toate stările finale posibile fiindca e ineficient, ci se va verifica daca o stare curentă se potrivește descrierii unei stări scop.
6. (15% = 2+5+5+3 ) 4 euristici:
    - (2%) banala
    - (5%+5%) doua euristici admisibile posibile (se va justifica la prezentare si in documentație de ce sunt admisibile)
    - (3%) o euristică neadmisibilă (se va da un exemplu prin care se demonstrează că nu e admisibilă). Atenție, euristica neadmisibilă trebuie să depindă de stare (să se calculeze în funcție de valori care descriu starea pentru care e calculată euristica).
7. (10%) crearea a 4 fisiere de input cu urmatoarele proprietati:
    1. un fisier de input care nu are solutii
    2. un fisier de input care da o stare initiala care este si finala (daca acest lucru nu e realizabil pentru problema, aleasa, veti mentiona acest lucru, explicand si motivul).
    3. un fisier de input care nu blochează pe niciun algoritm și să aibă ca soluții drumuri lungime micuță (ca să fie ușor de urmărit), să zicem de lungime maxim 20.
    4. un fisier de input care să blocheze un algoritm la timeout, dar minim un alt algoritm să dea soluție (de exemplu se blochează DF-ul dacă soluțiile sunt cât mai "în dreapta" în arborele de parcurgere)
    5. dintre ultimele doua fisiere, cel putin un fisier sa dea drumul de cost minim pentru euristicile admisibile si un drum care nu e de cost minim pentru cea euristica neadmisibila
8. (15%) Pentru cele NSOL drumuri(soluții) returnate de fiecare algoritm (unde NSOL e numarul de soluții dat în linia de comandă) se va afișa:
    - numărul de ordine al fiecărui nod din drum
    - lungimea drumului
    - costului drumului
    - timpul de găsire a unei soluții (**atenție**, pentru soluțiile de la a doua încolo timpul se consideră tot de la începutul execuției algoritmului și nu de la ultima soluție)
    - numărul maxim de noduri existente la un moment dat în memorie
    - numărul total de noduri calculate (totalul de succesori generati; atenție la DFI și IDA* se adună pentru fiecare iteratie chiar dacă se repetă generarea arborelui, nodurile se vor contoriza de fiecare dată afișându-se totalul pe toate iterațiile
    - între două soluții de va scrie un separator, sau soluțiile se vor scrie în fișiere diferite.

    Obținerea soluțiilor se va face cu ajutorul fiecăruia dintre algoritmii studiați:

    - **Pentru studenții de la seria CTI problema se va rula cu algoritmii: BF, DF, DFI, UCS, A* (varianta care dă toate drumurile), A* optimizat (cu listele open și closed, care dă doar drumul de cost minim), IDA*.**
    - **Pentru studenții din seriile Mate-Info și Informatică, problema se va rula cu algoritmii: BF, DF, DFI, A* (varianta care dă toate drumurile), A* optimizat (cu listele open și closed, care dă doar drumul de cost minim), IDA*.**Pentru toate variantele de A* (cel care oferă toate drumurile, cel optimizat pentru o singură soluție, și IDA*) se va rezolva problema cu fiecare dintre euristici. Fiecare din algoritmi va fi rulat cu timeout, si se va opri daca depășește acel timeout (necesar în special pentru fișierul fără soluții unde ajunge să facă tot arborele, sau pentru DF în cazul soluțiilor aflate foarte în dreapta în arborele de parcurgere).
9. (5%) Afisarea in fisierele de output in formatul cerut
10. (5%+5%) Validări și optimizari. Veți implementa elementele de mai jos care se potrivesc cu varianta de temă alocată vouă:
    - Validare: verificarea corectitudinii datelor de intrare
    - Validare: găsirea unui mod de a realiza din starea initială că problema nu are soluții. Validările și optimizările se vor descrie pe scurt în documentație.
    - Optimizare: găsirea unui mod de reprezentare a stării, cât mai eficient
    - Optimizare: găsirea unor condiții din care sa reiasă că o stare nu are cum sa contina in subarborele de succesori o stare finala deci nu mai merita expandata (nu are cum să se ajungă prin starea respectivă la o stare scop).
    - Optimizare: implementarea eficientă a algoritmilor cu care se rulează programul, folosind eventual module care oferă structuri de date performante.
11. (5%) Comentarii pentru clasele și funcțiile adăugate de voi în program (dacă folosiți scheletul de cod dat la laborator, nu e nevoie sa comentați și clasele existente). Comentariile pentru funcții trebuie să respecte un stil consacrat prin care se precizează tipul și rolurile parametrilor, căt și valoarea returnată (de exemplu, [reStructured text](https://www.python.org/dev/peps/pep-0287/) sau *[Google python docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)*).
12. (5%) Documentație cuprinzând explicarea euristicilor folosite. În cazul euristicilor admisibile, se va dovedi că sunt admisibile. În cazul euristicii neadmisibile, se va găsi un exemplu de stare dintr-un drum dat, pentru care h-ul estimat este mai mare decât h-ul real. Se va crea un tabel în documentație cuprinzând informațiile afișate pentru fiecare algoritm (lungimea și costul drumului, numărul maxim de noduri existente la un moment dat în memorie, numărul total de noduri). Pentru variantele de A* vor fi mai multe coloane în tabelul din documentație: câte o coloană pentru fiecare euristică. Tabelul va conține datele pentru minim 2 fișiere de input, printre care și fișierul de input care dă drum diferit pentru euristica neadmisibilă. În caz că nu se găsește cu euristica neadmisibilă un prim drum care să nu fie de cost minim, se acceptă și cazul în care cu euristica neadmisibilă se obțin drumurile în altă ordine decât crescătoare după cost, adică diferența să se vadă abia la drumul cu numărul K, K>1). Se va realiza sub tabel o comparație între algoritmi și soluțiile returnate, pe baza datelor din tabel, precizând și care algoritm e mai eficient în funcție de situație. Se vor indica pe baza tabelului ce dezavantaje are fiecare algoritm.
### Extratereștrii sunt printre noi

#### Context

O navă extraterestră dorește să răpească niște oameni pentru a culege informații despre specia noastră și ne cere ajutorul pentru găsirea unui algoritm. Oamenii sunt dispuși într-un oraș dreptunghiular precum harta de mai jos. Locurile de mers (străzile) sunt marcate cu simbolul "." și locurile ocupate de clădiri sunt marcate cu "#".

* * * * *

`...######........##

............####...\
..####..#.###......\
..#####..#.........\
.........##..#####.\
###.#..............\
###.#####....#####.\
..###............#.\
.......#######...#.\
`

Fiecare om se plimbă în treburile sale zilnice doar pe un segment (îl vom nota cu AB) (dus-întors) care se află pe linie și sau coloană și cuprinde doar spații libere. Pentru fiecare om se vor da punctele A și B ale segmentului, un punct fiind definit prin linia și coloana pe care se află. "Segmentul" trebuie să treacă doar prin spații libere, nu prin clădiri.

Nava extraterestră nu se poate deplasa dacă ajunge în raza vizuală a altui om, fiindcă altfel omenirea va afla despre existența extratereștrilor și extratereștrii nu vor mai putea să ne studieze în pace.

#### Stări și tranziții.

O stare reprezintă locațiile și direcția oamenilor și poziția navei la un moment dat. O tranziție e o deplasare a navei și a oamenilor. Mutările se fac în următoarea ordine: se mută toți oamenii care au mai rămas pe hartă) pe direcția curentă de deplasare în ordinea în care au fost definiți în fișier. Dacă un om a ajuns în capătul segmentului de deplasare, își schimbă direcția. Schimbarea de direcție durează cât o mutare, cu alte cuvinte, când omul ajunge în capăt la următoarea schimbare de stare, nu face un pas în altă celulă ci doar "își întoarce privirea". Abia la următorul moment de timp va păși în noua direcție.

După ce au fost poziționați oamenii, se mută nava (mutarea navei e obligatorie; dacă nu se poate conform condițiilor problemei, înseamnă că nu e o stare validă), deci se va ține cont de orientarea (și privirea) oamenilor după mutarea lor. Deoarece după ce a trecut nava printr-un loc oamenii devin mai vigilenți și instalează camere de luat vederi, nava nu are voie să revină într-o locație în care a mai fost, fiindca asta ar ajuta la confirmarea existenței ei. De asemenea, nava nu se poate deplasa în raza vizuală a unui om. Ca să fie în raza sa vizuală, nava trebuie să fie pe linia sau coloana de deplasare a omului, în direcția sa de deplasare și fără să existe obstacole sau alți oameni **între** ei (nava se poate afla și pe clădire și tot să fie vizibilă dacă e pe o căsuță din margine atâta timp cât respectă condiția zisă anterior).

Pentru ca nava să răpească un om trebuie să se poziționeze exact pe căsuța în care se află acesta.

În traseele lor, se poate întâmpla ca doi sau mai mulți oameni să se întâlnească în aceeași celulă. In acel moment oamenii se pun pe vorbit și nu se mai uită pe direcția de mers, deci nava poate trece neobservată (la următoarea mutare, oamenii care "vorbeau" în aceeași celulă, își continuă traseul ca și până atunci). Dacă nava ajunge într-o celulă cu mai mulți oameni, îi răpește pe toți.

#### Cost

Costul se calculează astfel:

-   la fiecare mutare a navei în spațiul liber(stradă) costul este dat de 1+(numărul de oameni de pe hartă).
-   O mutare într-o celulă cu obstacol are costul egal cu 1+(de 2 ori numarul de oameni de pe hartă)

#### Stare finală.

Nava își termină misiunea după ce răpește K oameni.

#### Fisierul de intrare

Programul citește din fișier:

-   poziția inițială a navei dată ca o pereche de numere reprezentând linia și coloana.
-   numărul K de oameni de răpit
-   harta
-   cuvântul "oameni" care apare imediat după hartă și indică faptul că începe enumerarea oamenilor
-   pentru fiecare om va exista câte o linie cu 4 numere, reprezentând linia și coloana poziției de start, linia și coloana celuilalt capăt al segmentului de deplasare. Se va verifica faptul că segmentul e corect (nu are în interior decât spații libere si e orientat doar pe linie sau coloană. De asemenea, nu e voie ca segmentele să aibă capete comune (vor fi doar celule distincte)

Se va verifica de asemenea ca poziția inițială a navei să nu fie în raza vizuală a vreunui om.

Exemplu de fișier de intrare:

* * * * *

`2 2

5\
...######........##\
............####...\
..####..#.###......\
..#####..#.........\
.........##..#####.\
###.#..............\
###.#####....#####.\
..###............#.\
.......#######...#.\
oameni\
1 0 1 7\
8 14 8 16\
7 9 5 9\
7 16 7 10\
4 0 4 8\
6 3 5 3\
4 6 4 1\
1 18 1 17\
3 18 7 18\
5 16 5 18\
0 0 0 3\
1 7 5 7\
8 0 8 5\
5 6 5 12\
`

#### Fișier output.

În fișierul de output se va afișa pentru fiecare nod din drumul soluție, starea curentă a hărții în formatul cerut mai jos, poziția fiecărui om care mai e pe hartă, costul total al mutărilor navei de până atunci (inclusiv ultima mutare), o matrice care arată pozițiile în care a mai fost nava (va fi harta orașului, fără oameni, iar pozițiile anterioare ale navei vor fi marcate cu "@"), numărul de oameni capturați.

Afișarea starii curente a hărții se va face cu următoarele notații:

-   Simbolul "." pentru loc liber (celulă de stradă, fără om în acea locație)
-   Simbolul "#" pentru celulă ocupată de clădire, în cazul în care nava nu e în acea celulă
-   Simbolurile "<" pentru om orientat spre stânga, ">" pentru om orientat spre dreapta, "^" pentru om orientat în sus, "v" pentru om orientat în jos.
-   Simbolul "o" pentru un grup de doi sau mai mulți oameni care s-au întâlnit în aceeași celulă
-   Simbolul "@" pentru navă - acest simbol are prioritate față de simbolurile de mai sus (dacă nava e într-o celulă, întotdeauna se va afișa în poziția corespunzătoare ei simbolul navei

De exemplu, pentru datele de intrare de mai sus, harta inițială din fișierul de ieșire ar fi:

* * * * *

`v..######........##

>......v....####..<\
..@###..#.###......\
..#####..#........v\
>.....<..##..#####.\
###.#.>.........>..\
###^#####....#####.\
..###....^......<#.\
>......#######>..#.`

Nava, de exemplu, nu ar putea să o ia în sus pentru că ar fi văzută de omul de pe linia 1 (care era în poziția 1,0 și avansează acum în 1,1). Un exemplu bun de succesor ar fi următorul, când nava a coborât cu o poziție.

* * * * *

`...######........##

v>..........####.<.\
..####.v#.###......\
..@####..#.........\
.>...<...##..#####v\
###^#..>.........>.\
###.#####^...#####.\
..###..........<.#.\
.>.....#######.>.#.`

Un nou succesor ar putea fi un pas la dreapta, deoarece omulețul de pe coloana respectivă a ajuns în capătul segmentul și se va întoarce așa cum se vede mai jos, și stim că întâi se calculează mutările oamenilor și apoi ale navei. De asemenea observați pe linia 5, coloana 18 întâlnirea celor 2 oameni care e simbolizată prin litera *o*.

* * * * *

`...######........##

..>.........####.>.\
v.####..#.###......\
..#@###v.#.........\
..>.<....##..#####.\
###v#...>^........o\
###.#####....#####.\
..###.........<..#.\
..>....#######..>#.`

Cei doi oameni de pe linia 4 care sunt față în față la următorul pas se vor întâlni în aceeași căsuță, deci nava poate coborî și să îi răpească pe amândoi cu o singură mutare. Omul din dreapta navei nu vede nava fiindcă nu e orientat spre ea; idem cel de pe coloană în jos.

* * * * *

`...######........##

...>........####..>\
..####..#.###......\
v.#####..#.........\
...@...v.##..#####.\
###.#....o........<\
###v#####....#####v\
..###........<...#.\
...>...#######..<#.`

Harta căsuțelor parcurse de navă, pentru starea de mai sus este:

* * * * *

`...######........##

............####...\
..@###..#.###......\
..@@###..#.........\
...@.....##..#####.\
###.#..............\
###.#####....#####.\
..###............#.\
.......#######...#.`
