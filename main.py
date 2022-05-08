import copy
import heapq
import queue
import sys
import os
import time

try:
    caleFolderInput = sys.argv[1]
    caleFolderOutput = sys.argv[2]
    NSOL = int(sys.argv[3])
    timeout = int(sys.argv[4])
except:
    sys.exit('''Apel gresit!
forma apel: main.py <caleFolderInput> <caleFolderOutput> <nrSol> <timeout>''')


##############################################################################################
#                                           Clase                                            #
##############################################################################################


class NodParcurgere:
    def __init__(self, oameniRamasi, pozitieNava, nrOameniDeRapit, nrOameniRapiti, parinte, cost):
        """
        :param oameniRamasi: este de forma (xCrt, yCrt, xStart, yStart, xFinish, yFinish, seIntoarce?)
        :param pozitieNava: pozitia curenta a navei
        :param nrOameniDeRapit: cati oameni trebuie rapiti
        :param nrOameniRapiti: cati oameni au fost rapiti deja
        :param parinte: parintele din arborele de parcurgere
        :param cost: costul pana la mutarea curenta
        """
        self.oameniRamasi = oameniRamasi
        self.pozitieNava = pozitieNava
        self.nrOameniDeRapit = nrOameniDeRapit
        self.nrOameniRapiti = nrOameniRapiti
        self.parinte = parinte
        self.cost = cost

    def obtineDrum(self):
        costTotal = self.cost
        pozitiiNava = [self.pozitieNava]
        l = [repr(self)]
        nod = self
        while nod.parinte is not None:
            l.insert(0, repr(nod.parinte))
            pozitiiNava.append(nod.parinte.pozitieNava)
            nod = nod.parinte
        return l, pozitiiNava, costTotal

    def afisDrum(self):
        (l, pozitiiNava, costTotal) = self.obtineDrum()
        matriceIstoricNava = copy.deepcopy(Graph.getMatriceHarta())
        for i, j in pozitiiNava:
            matriceIstoricNava[i][j] = '@'
        drum = "\n\n".join([str(i) + '.\n' + x for i, x in enumerate(l)]) + '\n\n'
        drum += '\n'.join([''.join([car for car in linie]) for linie in matriceIstoricNava])
        drum += f'\n\nLUNGIME TOTALA DRUM: {len(l)}' \
                f'\nCOST TOTAL DRUM: {costTotal}' \
                f'\nNODURI GENERATE PANA ACUM: {noduriGen}'
        return drum

    def contineInDrum(self, pozitieNava):
        # return infoNodNou in self.obtineDrum()
        nodDrum = self
        while nodDrum is not None:
            if pozitieNava == nodDrum.pozitieNava:
                return True
            nodDrum = nodDrum.parinte

        return False

    def __repr__(self):
        matriceAfisare = copy.deepcopy(Graph.getMatriceHarta())
        for om in self.oameniRamasi:
            if matriceAfisare[om[0]][om[1]] in "<>v^o":
                matriceAfisare[om[0]][om[1]] = 'o'
            elif om[2] == om[4]:
                if om[3] < om[5]:
                    if not om[6]:
                        matriceAfisare[om[0]][om[1]] = '>'
                    else:
                        matriceAfisare[om[0]][om[1]] = '<'
                else:
                    if not om[6]:
                        matriceAfisare[om[0]][om[1]] = '<'
                    else:
                        matriceAfisare[om[0]][om[1]] = '>'
            else:
                if om[2] < om[4]:
                    if not om[6]:
                        matriceAfisare[om[0]][om[1]] = 'v'
                    else:
                        matriceAfisare[om[0]][om[1]] = '^'
                else:
                    if not om[6]:
                        matriceAfisare[om[0]][om[1]] = '^'
                    else:
                        matriceAfisare[om[0]][om[1]] = 'v'
        matriceAfisare[self.pozitieNava[0]][self.pozitieNava[1]] = '@'
        return '\n'.join([''.join([car for car in linie]) for linie in matriceAfisare]) + f'\nCost: {self.cost}'


class NodParcurgereEuristica:

    def __init__(self, oameniRamasi, pozitieNava, nrOameniDeRapit, nrOameniRapiti, parinte, cost, h):
        """
            :param oameniRamasi: este de forma (xCrt, yCrt, xStart, yStart, xFinish, yFinish, seIntoarce?)
            :param pozitieNava: pozitia curenta a navei
            :param nrOameniDeRapit: cati oameni trebuie rapiti
            :param nrOameniRapiti: cati oameni au fost rapiti deja
            :param parinte: parintele din arborele de parcurgere
            :param cost: costul pana la mutarea curenta
            :param h: costul estimat de la nodul curent la cel scop
        """
        self.oameniRamasi = oameniRamasi
        self.pozitieNava = pozitieNava
        self.nrOameniDeRapit = nrOameniDeRapit
        self.nrOameniRapiti = nrOameniRapiti
        self.parinte = parinte
        self.cost = cost
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.g = cost  # costul de la radacina la nodul curent
        self.h = h
        self.f = self.g + self.h

    def obtineDrum(self):
        costTotal = self.cost
        pozitiiNava = [self.pozitieNava]
        l = [repr(self)]
        nod = self
        while nod.parinte is not None:
            l.insert(0, repr(nod.parinte))
            pozitiiNava.append(nod.parinte.pozitieNava)
            nod = nod.parinte
        return l, pozitiiNava, costTotal

    def afisDrum(self):  # returneaza si lungimea drumului
        (l, pozitiiNava, costTotal) = self.obtineDrum()
        matriceIstoricNava = copy.deepcopy(Graph.getMatriceHarta())
        for i, j in pozitiiNava:
            matriceIstoricNava[i][j] = '@'
        drum = "\n\n".join([str(i) + '.\n' + x for i, x in enumerate(l)]) + '\n\n'
        drum += '\n'.join([''.join([car for car in linie]) for linie in matriceIstoricNava])
        drum += f'\n\nLUNGIME TOTALA DRUM: {len(l)}' \
                f'\nCOST TOTAL DRUM: {costTotal}' \
                f'\nNODURI GENERATE PANA ACUM: {noduriGen}'
        return drum

    def contineInDrum(self, pozitieNava, oameniRamasi):
        # return infoNodNou in self.obtineDrum()
        nodDrum = self
        while nodDrum is not None:
            if pozitieNava == nodDrum.pozitieNava and sorted(oameniRamasi) == sorted(nodDrum.oameniRamasi):
                return True
            nodDrum = nodDrum.parinte

        return False

    def __repr__(self):
        matriceAfisare = copy.deepcopy(Graph.getMatriceHarta())
        for om in self.oameniRamasi:
            if matriceAfisare[om[0]][om[1]] in "<>v^o":
                matriceAfisare[om[0]][om[1]] = 'o'
            elif om[2] == om[4]:
                if om[3] < om[5]:
                    if not om[6]:
                        matriceAfisare[om[0]][om[1]] = '>'
                    else:
                        matriceAfisare[om[0]][om[1]] = '<'
                else:
                    if not om[6]:
                        matriceAfisare[om[0]][om[1]] = '<'
                    else:
                        matriceAfisare[om[0]][om[1]] = '>'
            else:
                if om[2] < om[4]:
                    if not om[6]:
                        matriceAfisare[om[0]][om[1]] = 'v'
                    else:
                        matriceAfisare[om[0]][om[1]] = '^'
                else:
                    if not om[6]:
                        matriceAfisare[om[0]][om[1]] = '^'
                    else:
                        matriceAfisare[om[0]][om[1]] = 'v'
        matriceAfisare[self.pozitieNava[0]][self.pozitieNava[1]] = '@'
        return '\n'.join([''.join([car for car in linie]) for linie in matriceAfisare]) + f'\nCost: {self.cost}'

    # pentru PriorityQueue
    def __lt__(self, other):
        return self.f < other.f or (self.f == other.f and self.g >= other.g)

    def __eq__(self, other):
        return self.f == other.f and self.g == other.g and self.pozitieNava == other.pozitieNava and sorted(self.oameniRamasi) == sorted(other.oameniRamasi)


class Graph:  # graful problemei
    matriceHarta = None

    def __init__(self, oameni, matriceHarta, navaInit, oameniDeRapit):
        """
        :param oameni -> segmentele de deplasare
        :param matriceHarta -> matricea cu strazile si cladirile
        :param navaInit -> coordonatele de la care pleaca nava
        :param oameniDeRapit -> numarul k de oameni care trebuie rapiti
        """
        self.oameni = oameni
        self.matriceHarta = matriceHarta
        self.navaInit = navaInit
        self.oameniDeRapit = oameniDeRapit

    @staticmethod
    def getMatriceHarta():
        return matriceHarta

    # va genera succesorii sub forma de noduri in arborele de parcurgere
    def genereazaSuccesori(self, nodCurent):
        listaSuccesori = []

        # fac o copie a oamenilor ramasi pentru a le calcula pozitiile noi
        oameniRamasi_nodCurent = [[x1, y1, x2, y2, x3, y3, seIntoarce] for [x1, y1, x2, y2, x3, y3, seIntoarce] in
                                  nodCurent.oameniRamasi]

        # mai intai obtin pozitiile noi ale oamenilor ramasi
        for om in oameniRamasi_nodCurent:
            if om[2] == om[4]:
                if om[3] < om[5]:
                    if om[1] == om[5] and not om[6]:  # om[6] este false daca omul inca nu s-a intors
                        om[6] = True
                    elif om[1] == om[3] and om[6]:  # omul se va intoarce pe sensul default
                        om[6] = False
                    elif not om[6]:
                        om[1] += 1
                    else:
                        om[1] -= 1
                else:
                    if om[1] == om[5] and not om[6]:
                        om[6] = True
                    elif om[1] == om[3] and om[6]:
                        om[6] = False
                    elif not om[6]:
                        om[1] -= 1
                    else:
                        om[1] += 1
            else:
                if om[2] < om[4]:
                    if om[0] == om[4] and not om[6]:
                        om[6] = True
                    elif om[0] == om[2] and om[6]:
                        om[6] = False
                    elif not om[6]:
                        om[0] += 1
                    else:
                        om[0] -= 1
                else:
                    if om[0] == om[4] and not om[6]:
                        om[6] = True
                    elif om[0] == om[2] and om[6]:
                        om[6] = False
                    elif not om[6]:
                        om[0] -= 1
                    else:
                        om[0] += 1
        # acum pentru fiecare directie verific daca nu iese din harta si daca nava nu e vazuta de oameni
        nrOameniPePozitie = [[0 for i in range(len(Graph.getMatriceHarta()[0]))] for j in
                             range(len(Graph.getMatriceHarta()))]
        for om in oameniRamasi_nodCurent:
            nrOameniPePozitie[om[0]][om[1]] += 1
        d_x = [0, -1, 0, 1]
        d_y = [-1, 0, 1, 0]

        for i in range(4):
            pozNava = list(nodCurent.pozitieNava)
            pozNava[0] += d_x[i]
            pozNava[1] += d_y[i]

            if pozNava[0] not in range(len(Graph.getMatriceHarta())) or pozNava[1] not in range(
                    len(Graph.getMatriceHarta()[0])):
                continue

            if nodCurent.contineInDrum(pozNava):
                continue

            pozitieValida = True

            for om in oameniRamasi_nodCurent:
                if om[2] == om[4]:
                    if pozNava[0] != om[0]:
                        continue
                    elif om[3] < om[5]:
                        if not om[6] and pozNava[1] > om[1]:
                            for j in range(om[1] + 1, pozNava[1]):
                                if Graph.getMatriceHarta()[om[0]][j] == '#' or nrOameniPePozitie[om[0]][j] > 0:
                                    continue
                            pozitieValida = False
                            break
                        elif om[6] and pozNava[1] < om[1]:
                            for j in range(pozNava[1] + 1, om[1]):
                                if Graph.getMatriceHarta()[om[0]][j] == '#' or nrOameniPePozitie[om[0]][j] > 0:
                                    continue
                            pozitieValida = False
                            break
                    elif om[3] > om[5]:
                        if not om[6] and pozNava[1] < om[1]:
                            for j in range(pozNava[1] + 1, om[1]):
                                if Graph.getMatriceHarta()[om[0]][j] == '#' or nrOameniPePozitie[om[0]][j] > 0:
                                    continue
                            pozitieValida = False
                            break
                        elif om[6] and pozNava[1] > om[1]:
                            for j in range(pozNava[1] + 1, om[1]):
                                if Graph.getMatriceHarta()[om[0]][j] == '#' or nrOameniPePozitie[om[0]][j] > 0:
                                    continue
                            pozitieValida = False
                            break
                else:
                    if pozNava[1] != om[1]:
                        continue
                    elif om[2] < om[4]:
                        if not om[6] and pozNava[0] > om[0]:
                            for j in range(om[0] + 1, pozNava[0]):
                                if Graph.getMatriceHarta()[j][om[1]] == '#' or nrOameniPePozitie[j][om[1]] > 0:
                                    continue
                            pozitieValida = False
                            break
                        elif om[6] and pozNava[0] < om[0]:
                            for j in range(pozNava[0] + 1, om[0]):
                                if Graph.getMatriceHarta()[j][om[1]] == '#' or nrOameniPePozitie[j][om[1]] > 0:
                                    continue
                            pozitieValida = False
                            break
                    elif om[2] > om[4]:
                        if not om[6] and pozNava[0] < om[0]:
                            for j in range(pozNava[0] + 1, om[0]):
                                if Graph.getMatriceHarta()[j][om[1]] == '#' or nrOameniPePozitie[j][om[1]] > 0:
                                    continue
                            pozitieValida = False
                            break
                        elif om[6] and pozNava[0] > om[0]:
                            for j in range(om[0] + 1, pozNava[0]):
                                if Graph.getMatriceHarta()[j][om[1]] == '#' or nrOameniPePozitie[j][om[1]] > 0:
                                    continue
                            pozitieValida = False
                            break

            if not pozitieValida:
                continue

            # elimin oamenii care se afla pe pozitia navei
            oameniRamasi = [om for om in oameniRamasi_nodCurent if (om[0] != pozNava[0] or om[1] != pozNava[1])]
            oameniCapturati = nrOameniPePozitie[pozNava[0]][pozNava[1]]

            if Graph.getMatriceHarta()[pozNava[0]][pozNava[1]] == '#':
                cost = nodCurent.cost + 1 + 2 * len(oameniRamasi)
            else:
                cost = nodCurent.cost + 1 + len(oameniRamasi)

            listaSuccesori.append(NodParcurgere(oameniRamasi, pozNava, nodCurent.nrOameniDeRapit,
                                                nodCurent.nrOameniRapiti + oameniCapturati, nodCurent, cost))
        return listaSuccesori

    def genereazaSuccesoriEuristica(self, nodCurent, tip_euristica):
        listaSuccesori = []

        # fac o copie a oamenilor ramasi pentru a le calcula pozitiile noi
        oameniRamasi_nodCurent = [[x1, y1, x2, y2, x3, y3, seIntoarce] for [x1, y1, x2, y2, x3, y3, seIntoarce] in
                                  nodCurent.oameniRamasi]

        # mai intai obtin pozitiile noi ale oamenilor ramasi
        for om in oameniRamasi_nodCurent:
            if om[2] == om[4]:
                if om[3] < om[5]:
                    if om[1] == om[5] and not om[6]:  # om[6] este false daca omul inca nu s-a intors
                        om[6] = True
                    elif om[1] == om[3] and om[6]:  # omul se va intoarce pe sensul default
                        om[6] = False
                    elif not om[6]:
                        om[1] += 1
                    else:
                        om[1] -= 1
                else:
                    if om[1] == om[5] and not om[6]:
                        om[6] = True
                    elif om[1] == om[3] and om[6]:
                        om[6] = False
                    elif not om[6]:
                        om[1] -= 1
                    else:
                        om[1] += 1
            else:
                if om[2] < om[4]:
                    if om[0] == om[4] and not om[6]:
                        om[6] = True
                    elif om[0] == om[2] and om[6]:
                        om[6] = False
                    elif not om[6]:
                        om[0] += 1
                    else:
                        om[0] -= 1
                else:
                    if om[0] == om[4] and not om[6]:
                        om[6] = True
                    elif om[0] == om[2] and om[6]:
                        om[6] = False
                    elif not om[6]:
                        om[0] -= 1
                    else:
                        om[0] += 1
        # acum pentru fiecare directie verific daca nu iese din harta si daca nava nu e vazuta de oameni
        nrOameniPePozitie = [[0 for i in range(len(Graph.getMatriceHarta()[0]))] for j in
                             range(len(Graph.getMatriceHarta()))]
        for om in oameniRamasi_nodCurent:
            nrOameniPePozitie[om[0]][om[1]] += 1
        d_x = [0, -1, 0, 1]
        d_y = [-1, 0, 1, 0]

        for i in range(4):
            pozNava = list(nodCurent.pozitieNava)
            pozNava[0] += d_x[i]
            pozNava[1] += d_y[i]

            if pozNava[0] not in range(len(Graph.getMatriceHarta())) or pozNava[1] not in range(
                    len(Graph.getMatriceHarta()[0])):
                continue


            pozitieValida = True

            for om in oameniRamasi_nodCurent:
                if om[2] == om[4]:
                    if pozNava[0] != om[0]:
                        continue
                    elif om[3] < om[5]:
                        if not om[6] and pozNava[1] > om[1]:
                            for j in range(om[1] + 1, pozNava[1]):
                                if Graph.getMatriceHarta()[om[0]][j] == '#' or nrOameniPePozitie[om[0]][j] > 0:
                                    continue
                            pozitieValida = False
                            break
                        elif om[6] and pozNava[1] < om[1]:
                            for j in range(pozNava[1] + 1, om[1]):
                                if Graph.getMatriceHarta()[om[0]][j] == '#' or nrOameniPePozitie[om[0]][j] > 0:
                                    continue
                            pozitieValida = False
                            break
                    elif om[3] > om[5]:
                        if not om[6] and pozNava[1] < om[1]:
                            for j in range(pozNava[1] + 1, om[1]):
                                if Graph.getMatriceHarta()[om[0]][j] == '#' or nrOameniPePozitie[om[0]][j] > 0:
                                    continue
                            pozitieValida = False
                            break
                        elif om[6] and pozNava[1] > om[1]:
                            for j in range(pozNava[1] + 1, om[1]):
                                if Graph.getMatriceHarta()[om[0]][j] == '#' or nrOameniPePozitie[om[0]][j] > 0:
                                    continue
                            pozitieValida = False
                            break
                else:
                    if pozNava[1] != om[1]:
                        continue
                    elif om[2] < om[4]:
                        if not om[6] and pozNava[0] > om[0]:
                            for j in range(om[0] + 1, pozNava[0]):
                                if Graph.getMatriceHarta()[j][om[1]] == '#' or nrOameniPePozitie[j][om[1]] > 0:
                                    continue
                            pozitieValida = False
                            break
                        elif om[6] and pozNava[0] < om[0]:
                            for j in range(pozNava[0] + 1, om[0]):
                                if Graph.getMatriceHarta()[j][om[1]] == '#' or nrOameniPePozitie[j][om[1]] > 0:
                                    continue
                            pozitieValida = False
                            break
                    elif om[2] > om[4]:
                        if not om[6] and pozNava[0] < om[0]:
                            for j in range(pozNava[0] + 1, om[0]):
                                if Graph.getMatriceHarta()[j][om[1]] == '#' or nrOameniPePozitie[j][om[1]] > 0:
                                    continue
                            pozitieValida = False
                            break
                        elif om[6] and pozNava[0] > om[0]:
                            for j in range(om[0] + 1, pozNava[0]):
                                if Graph.getMatriceHarta()[j][om[1]] == '#' or nrOameniPePozitie[j][om[1]] > 0:
                                    continue
                            pozitieValida = False
                            break

            if not pozitieValida:
                continue


            # elimin oamenii care se afla pe pozitia navei
            oameniRamasi = [om for om in oameniRamasi_nodCurent if (om[0] != pozNava[0] or om[1] != pozNava[1])]
            if nodCurent.contineInDrum(pozNava, oameniRamasi):
                continue
            oameniCapturati = nrOameniPePozitie[pozNava[0]][pozNava[1]]

            if Graph.getMatriceHarta()[pozNava[0]][pozNava[1]] == '#':
                cost = nodCurent.cost + 1 + 2 * len(oameniRamasi)
            else:
                cost = nodCurent.cost + 1 + len(oameniRamasi)

            listaSuccesori.append(NodParcurgereEuristica(oameniRamasi, pozNava, nodCurent.nrOameniDeRapit,
                                                nodCurent.nrOameniRapiti + oameniCapturati, nodCurent, cost,
                                                         self.calculeaza_h(pozNava, oameniRamasi, nodCurent.nrOameniDeRapit,
                                                nodCurent.nrOameniRapiti + oameniCapturati, cost, tip_euristica)))
        return listaSuccesori

    def calculeaza_h(self, pozNouaNava, oameniRamasi, nrOameniDeRapit, nrOameniRapiti, costMutare, tip_euristica):
        if tip_euristica == 'euristica banala':
            if nrOameniRapiti < nrOameniDeRapit:
                return 1
            return 0
        elif tip_euristica == 'euristica admisibila 1':
            dist = min([abs(pozNouaNava[0] - om[0]) + abs(pozNouaNava[1] - om[1]) for om in oameniRamasi])
            return dist * len(oameniRamasi) // 2

        elif tip_euristica == 'euristica admisibila 2':
            dist = sorted([abs(pozNouaNava[0] - om[0]) + abs(pozNouaNava[1] - om[1]) for om in oameniRamasi])[:min(nrOameniDeRapit - nrOameniRapiti, len(oameniRamasi))]
            try:
                return int(dist[-1] - 1 + len(oameniRamasi) / nrOameniDeRapit) * len(oameniRamasi) // 2
            except:   # nu mai sunt oameni de rapit
                return 0
        else:
            try:
                dist = max([abs(pozNouaNava[0] - om[0]) + abs(pozNouaNava[1] - om[1]) for om in oameniRamasi])
            except:
                dist = 0
            return dist * 2 * len(oameniRamasi)

    def testeaza_scop(self, nodCurent):
        if nodCurent.cost == 0:  # pentru cazul in care nodul initial se afla deja deasupra numarului necesar de oameni
            navaX = nodCurent.pozitieNava[0]
            navaY = nodCurent.pozitieNava[1]
            if len([om for om in nodCurent.oameniRamasi if
                    om[0] == navaX and om[1] == navaY]) == nodCurent.nrOameniDeRapit:
                return True
        elif nodCurent.nrOameniRapiti >= nodCurent.nrOameniDeRapit:
            return True
        return False


def breadth_first(gr: Graph, nrSolutiiCautate, file):
    global noduriGen
    global timp
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    oameni = [[x1, y1, x1, y1, x2, y2, False] for [x1, y1, x2, y2] in gr.oameni]
    # optimizare - am folosit queue in loc de lista
    q = queue.Queue()
    nodInitial = NodParcurgere(oameni, gr.navaInit, gr.oameniDeRapit, 0, None, 0)

    if gr.testeaza_scop(nodInitial):
        file.write(f"\nSolutie BF la {time.time() - timp:.4f} secunde:\n")
        file.write(nodInitial.afisDrum())
        file.write("\n\n----------------\n\n")
        return 0

    q.put(nodInitial)

    while not q.empty():
        if time.time() - timp > timeout:
            return -1
        nodCurent = q.get(0)
        lSuccesori = gr.genereazaSuccesori(nodCurent)
        noduriGen += len(lSuccesori)

        if time.time() - timp > timeout:
            return -1

        for succ in lSuccesori:
            q.put(succ)
            if gr.testeaza_scop(succ):
                file.write(f"\nSolutie BF la {time.time() - timp:.4f} secunde:\n")
                file.write(succ.afisDrum())
                file.write("\n\n----------------\n\n")
                nrSolutiiCautate -= 1
                if nrSolutiiCautate == 0:
                    return 0


def depth_first(gr: Graph, nrSolutiiCautate, file):
    # vom simula o stiva prin relatia de parinte a nodului curent
    oameni = [[x1, y1, x1, y1, x2, y2, False] for [x1, y1, x2, y2] in gr.oameni]
    nodInitial = NodParcurgere(oameni, gr.navaInit, gr.oameniDeRapit, 0, None, 0)
    if gr.testeaza_scop(nodInitial):
        file.write(f"\nSolutie DF la {time.time() - timp:.4f} secunde:\n")
        file.write(nodInitial.afisDrum())
        file.write("\n\n----------------\n\n")
        return 0
    return df(NodParcurgere(oameni, gr.navaInit, gr.oameniDeRapit, 0, None, 0), nrSolutiiCautate, file)


def df(nodCurent, nrSolutiiCautate, file):
    global noduriGen
    global timp

    if time.time() - timp > timeout:
        return -1
    if gr.testeaza_scop(nodCurent):
        file.write(f"\nSolutie DF la {time.time() - timp:.4f} secunde:\n")
        file.write(nodCurent.afisDrum())
        file.write("\n\n----------------\n\n")
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return 0
    lSuccesori = gr.genereazaSuccesori(nodCurent)
    noduriGen += len(lSuccesori)

    if time.time() - timp > timeout:
        return -1

    for sc in lSuccesori:
        if nrSolutiiCautate != 0:
            nrSolutiiCautate = df(sc, nrSolutiiCautate, file)

    return nrSolutiiCautate


def depth_first_iterativ(gr: Graph, nrSolutiiCautate, file):
    oameni = [[x1, y1, x1, y1, x2, y2, False] for [x1, y1, x2, y2] in gr.oameni]
    nodInitial = NodParcurgere(oameni, gr.navaInit, gr.oameniDeRapit, 0, None, 0)
    if gr.testeaza_scop(nodInitial):
        file.write(f"\nSolutie DFI la {time.time() - timp:.4f} secunde:\n")
        file.write(nodInitial.afisDrum())
        file.write("\n\n----------------\n\n")
        return 0
    for i in range(1, len(gr.getMatriceHarta()) * len(gr.getMatriceHarta()[0])):
        if nrSolutiiCautate in [0, -1]:
            return nrSolutiiCautate
        nrSolutiiCautate = dfi(nodInitial, i, nrSolutiiCautate, file)


def dfi(nodCurent, adancime, nrSolutiiCautate, file):
    global noduriGen
    global timp

    if time.time() - timp > timeout:
        return -1

    if adancime == 1 and gr.testeaza_scop(nodCurent):
        file.write(f"\nSolutie DFI la {time.time() - timp:.4f} secunde:\n")
        file.write(nodCurent.afisDrum())
        file.write("\n\n----------------\n\n")

        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return nrSolutiiCautate
    if adancime > 1:
        lSuccesori = gr.genereazaSuccesori(nodCurent)
        noduriGen += len(lSuccesori)

        if time.time() - timp > timeout:
            return -1

        for sc in lSuccesori:
            if nrSolutiiCautate != 0:
                nrSolutiiCautate = dfi(sc, adancime - 1, nrSolutiiCautate, file)
    return nrSolutiiCautate


def a_star(gr: Graph, nrSolutiiCautate, euristica, file):
    global noduriGen
    global timp
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    oameni = [[x1, y1, x1, y1, x2, y2, False] for [x1, y1, x2, y2] in gr.oameni]
    q = queue.PriorityQueue()
    nodInitial = NodParcurgereEuristica(oameni, gr.navaInit, gr.oameniDeRapit, 0, None, 0, gr.calculeaza_h(gr.navaInit, oameni, gr.oameniDeRapit, 0, 0, euristica))

    if gr.testeaza_scop(nodInitial):
        file.write(f"\nSolutie A* {euristica} la {time.time() - timp:.4f} secunde:\n")
        file.write(nodInitial.afisDrum())
        file.write("\n\n----------------\n\n")
        return 0

    q.put(nodInitial)

    while not q.empty():

        if time.time() - timp > timeout:
            return -1

        nodCurent = q.get()
        if gr.testeaza_scop(nodCurent):
            file.write(f"\nSolutie A* {euristica} la {time.time() - timp:.4f} secunde:\n")
            file.write(nodCurent.afisDrum())
            file.write("\n\n----------------\n\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return 0
        lSuccesori = gr.genereazaSuccesoriEuristica(nodCurent, euristica)
        noduriGen += len(lSuccesori)

        if time.time() - timp > timeout:
            return -1

        for s in lSuccesori:
            q.put(s)


def a_star_optimizat(gr: Graph, euristica, file):
    global noduriGen
    global timp

    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    oameni = [[x1, y1, x1, y1, x2, y2, False] for [x1, y1, x2, y2] in gr.oameni]
    nodInitial = NodParcurgereEuristica(oameni, gr.navaInit, gr.oameniDeRapit, 0, None, 0,
                                        gr.calculeaza_h(gr.navaInit, oameni, gr.oameniDeRapit, 0, 0, euristica))

    if gr.testeaza_scop(nodInitial):
        file.write(f"\nSolutie A* optimizat {euristica} la {time.time() - timp:.4f} secunde:\n")
        file.write(nodInitial.afisDrum())
        file.write("\n\n----------------\n\n")
        return 0

    l_open = [nodInitial]

    l_closed = []
    while len(l_open) > 0:

        if time.time() - timp > timeout:
            return -1

        nodCurent = l_open.pop(0)
        l_closed.append(nodCurent)
        if gr.testeaza_scop(nodCurent):
            file.write(f"\nSolutie A* optimizat {euristica} la {time.time() - timp:.4f} secunde:\n")
            file.write(nodCurent.afisDrum())
            file.write("\n\n----------------\n\n")
            return 0
        lSuccesori = gr.genereazaSuccesoriEuristica(nodCurent, euristica)
        noduriGen += len(lSuccesori)
        for s in lSuccesori:
            gasitC = False
            for nodC in l_open:
                if s.pozitieNava == nodC.pozitieNava and sorted(s.oameniRamasi) == sorted(nodC.oameniRamasi):
                    gasitC = True
                    if s.f >= nodC.f:
                        lSuccesori.remove(s)
                    else:  # s.f<nodC.f
                        l_open.remove(nodC)
                    break
            if not gasitC:
                for nodC in l_closed:
                    if s.pozitieNava == nodC.pozitieNava and sorted(s.oameniRamasi) == sorted(nodC.oameniRamasi):
                        if s.f >= nodC.f:
                            lSuccesori.remove(s)
                        else:  # s.f<nodC.f
                            l_closed.remove(nodC)
                        break
        for s in lSuccesori:
            i = 0
            gasit_loc = False
            for i in range(len(l_open)):
                if l_open[i].f > s.f or (l_open[i].f == s.f and l_open[i].g <= s.g):
                    gasit_loc = True
                    break
            if gasit_loc:
                l_open.insert(i, s)
            else:
                l_open.append(s)


def ida_star(gr: Graph, nrSolutiiCautate, euristica, file):
    global timp

    oameni = [[x1, y1, x1, y1, x2, y2, False] for [x1, y1, x2, y2] in gr.oameni]
    nodStart = NodParcurgereEuristica(oameni, gr.navaInit, gr.oameniDeRapit, 0, None, 0, gr.calculeaza_h(gr.navaInit, oameni, gr.oameniDeRapit, 0, 0, euristica))

    if gr.testeaza_scop(nodStart):
        file.write(f"\nSolutie IDA* {euristica} la {time.time() - timp:.4f} secunde:\n")
        file.write(nodStart.afisDrum())
        file.write("\n\n----------------\n\n")
        return 0

    limita = nodStart.f
    while time.time() - timp < timeout:
        nrSolutiiCautate, rez = construieste_drum(gr, nodStart, limita, nrSolutiiCautate, euristica, file)
        if rez == "gata":
            return 0
        if rez == float('inf'):
            return 0
        limita = rez
    return -1


def construieste_drum(gr, nodCurent, limita, nrSolutiiCautate, euristica, file):
    global noduriGen

    if nodCurent.f > limita:
        return nrSolutiiCautate, nodCurent.f
    if gr.testeaza_scop(nodCurent) and nodCurent.f == limita:
        file.write(f"\nSolutie IDA* {euristica} la {time.time() - timp:.4f} secunde:\n")
        file.write(nodCurent.afisDrum())
        file.write("\n\n----------------\n\n")
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return 0, "gata"
    lSuccesori = gr.genereazaSuccesoriEuristica(nodCurent, euristica)
    noduriGen += len(lSuccesori)
    minim = float('inf')
    for s in lSuccesori:
        nrSolutiiCautate, rez = construieste_drum(gr, s, limita, nrSolutiiCautate, euristica, file)
        if rez == "gata":
            return 0, "gata"
        if rez < minim:
            minim = rez
    return nrSolutiiCautate, minim


##############################################################################################
#                    Citire din fisiere, validare si rulare algoritmi                        #
##############################################################################################

folderInput = os.listdir(caleFolderInput)

if not os.path.exists(caleFolderOutput):
    os.mkdir(caleFolderOutput)

for fisier in folderInput:
    f = open(caleFolderInput + '/' + fisier)
    continutInput = f.read().split('oameni')
    pozitieInitialaNava = tuple(int(x) for x in continutInput[0].split('\n')[0].split(' '))
    nrOameniDeRapit = int(continutInput[0].split('\n')[1])
    matriceHarta = [[caracter for caracter in linie] for linie in continutInput[0].split('\n')[2:]][:-1]
    nrLiniiHarta = len(matriceHarta)
    nrColoaneHarta = len(matriceHarta[0])
    oameni = [[int(x) for x in om.split()] for om in continutInput[1].split('\n')][1:]
    inputValid = True
    f.close()

    if pozitieInitialaNava[0] not in range(nrLiniiHarta) or pozitieInitialaNava[1] not in range(nrColoaneHarta):
        f = open(caleFolderOutput + '/output' + fisier, 'w')
        f.write('Nava este in afara hartii')
        f.close()
        continue


    def verificare_segment(om):
        """Functia cu care verific daca segmentele sunt corecte

        Argument:
                om (lista de int-uri): lista coordonatelor start/finish
        Returneaza:
                bool: True daca segmentul e corect, False altfel"""

        # verificare segment orientat pe linie/coloana si nu are capete comune
        if (om[0] == om[2]) != (om[1] == om[3]):
            if om[0] not in range(0, nrLiniiHarta) \
                    or om[1] not in range(0, nrColoaneHarta) \
                    or om[2] not in range(0, nrLiniiHarta) \
                    or om[3] not in range(0, nrColoaneHarta):
                return False

            if om[0] == om[2]:
                linie = om[0]
                deLaColoana = min(om[1], om[3])
                panaLaColoana = max(om[1], om[3])
                if len(set(matriceHarta[linie][deLaColoana:panaLaColoana + 1])) == 1:
                    return True
            else:
                coloana = om[1]
                deLaLinia = min(om[0], om[2])
                panaLaLinia = max(om[0], om[2])
                if len(set([row[coloana] for row in matriceHarta[deLaLinia:panaLaLinia + 1]])) == 1:
                    return True
        return False


    for index, om in enumerate(oameni):
        if not verificare_segment(om):
            f = open(caleFolderOutput + '/output_' + fisier, 'w')
            f.write(f'Segmentul de deplasare {index} este incorect!')
            f.close()
            inputValid = False
            break

    if not inputValid:
        continue

    # verificare ca poziția inițială a navei să nu fie în raza vizuală a vreunui om
    nrOameniPePozitie = dict()
    for om in oameni:
        if (om[0], om[1]) not in nrOameniPePozitie:
            nrOameniPePozitie[(om[0], om[1])] = 1
        else:
            nrOameniPePozitie[(om[0], om[1])] += 1

    for index, om in enumerate(oameni):
        if om[0] == pozitieInitialaNava[0] and om[1] == pozitieInitialaNava[1]:
            continue
        if om[0] == om[2]:  # omul se deplaseaza pe linie
            if om[1] < om[3]:  # omul se deplaseaza spre dreapta
                if pozitieInitialaNava[0] != om[0] or pozitieInitialaNava[1] < om[1]:  # nava nu este in directia/sensul de mers
                    continue
                cevaIntre = False
                for i in range(om[1] + 1, pozitieInitialaNava[1]):
                    if matriceHarta[om[0]][i] == '#' or nrOameniPePozitie[(om[0], i)] > 0:
                        cevaIntre = True
                        break
                if not cevaIntre:
                    inputValid = False
                    f = open(caleFolderOutput + '/output_' + fisier, 'w')
                    f.write(f'Omul {index} vede deja nava!')
                    f.close()
                    break
            else:  # omeul se deplaseaza spre stanga
                if pozitieInitialaNava[0] != om[0] or pozitieInitialaNava[1] > om[1]:
                    continue
                cevaIntre = False
                for i in range(om[1] - 1, pozitieInitialaNava[1], -1):
                    if matriceHarta[om[0]][i] == '#' or nrOameniPePozitie[(om[0], i)] > 0:
                        cevaIntre = True
                        break
                if not cevaIntre:
                    inputValid = False
                    f = open(caleFolderOutput + '/output_' + fisier, 'w')
                    f.write(f'Omul {index} vede deja nava!')
                    f.close()
                    break
        else:  # omul se deplaseaza pe coloana
            if om[0] < om[2]:  # omul se deplaseaza in jos
                if pozitieInitialaNava[1] != om[1] or pozitieInitialaNava[0] < om[0]:
                    continue
                cevaIntre = False
                for i in range(om[0] + 1, pozitieInitialaNava[0]):
                    if matriceHarta[i][om[1]] == '#' or nrOameniPePozitie[(i, om[1])] > 0:
                        cevaIntre = True
                        break
                if not cevaIntre:
                    inputValid = False
                    f = open(caleFolderOutput + '/output_' + fisier, 'w')
                    f.write(f'Omul {index} vede deja nava!')
                    f.close()
                    break
            else:  # omul se deplaseaza in sus
                if pozitieInitialaNava[1] != om[1] or pozitieInitialaNava[0] > om[0]:
                    continue
                cevaIntre = False
                for i in range(om[0] - 1, pozitieInitialaNava[0], -1):
                    if matriceHarta[i][om[1]] == '#' or nrOameniPePozitie[(i, om[1])] > 0:
                        cevaIntre = True
                        break
                if not cevaIntre:
                    inputValid = False
                    f = open(caleFolderOutput + '/output_' + fisier, 'w')
                    f.write(f'Omul {index} vede deja nava!')
                    f.close()
                    break

    if not inputValid:
        continue

    # if fisier == 'input4.txt':
    #     continue

    f = open(caleFolderOutput + '/output_' + fisier, 'w')
    gr = Graph(oameni, matriceHarta, pozitieInitialaNava, nrOameniDeRapit)
    print(f'\n##################### Timpi fisier {fisier} #####################')

    # BF
    timp = time.time()
    noduriGen = 1
    rez = breadth_first(gr, NSOL, f)
    f.write(f'NODURI GENERATE IN TOTAL PENTRU BF: {noduriGen}\n\n----------------\n\n')
    print(f'Timp BF: {time.time() - timp if rez == 0 else " nu a terminat executia"}')

    # DF
    timp = time.time()
    noduriGen = 1
    rez = depth_first(gr, NSOL, f)
    f.write(f'NODURI GENERATE IN TOTAL PENTRU DF: {noduriGen}\n\n----------------\n\n')
    print(f'Timp DF: {time.time() - timp if rez == 0 else " nu a terminat executia"}')

    #  DFI
    timp = time.time()
    noduriGen = 1
    rez = depth_first_iterativ(gr, NSOL, f)
    f.write(f'NODURI GENERATE IN TOTAL PENTRU DFI: {noduriGen}\n\n----------------\n\n')
    print(f'Timp DFI: {time.time() - timp if rez == 0 else " nu a terminat executia"}')

    # A*
    euristici = ['euristica banala', 'euristica admisibila 1', 'euristica admisibila 2', 'euristica neadmisibila']
    for euristica in euristici:
        noduriGen = 1
        timp = time.time()
        rez = a_star(gr, NSOL, euristica, f)
        f.write(f'NODURI GENERATE IN TOTAL PENTRU A* {euristica}: {noduriGen}\n\n----------------\n\n')
        print(f'Timp A* {euristica}: {time.time() - timp if rez == 0 else " nu a terminat executia"}')

    # A* optimizat
    euristici = ['euristica banala', 'euristica admisibila 1', 'euristica admisibila 2', 'euristica neadmisibila']
    for euristica in euristici:
        noduriGen = 1
        timp = time.time()
        rez = a_star_optimizat(gr, euristica, f)
        f.write(f'NODURI GENERATE IN TOTAL PENTRU A* optimizat {euristica}: {noduriGen}\n\n----------------\n\n')
        print(f'Timp A* optimizat {euristica}: {time.time() - timp if rez == 0 else " nu a terminat executia"}')

    # IDA*
    euristici = ['euristica banala', 'euristica admisibila 1', 'euristica admisibila 2', 'euristica neadmisibila']
    for euristica in euristici:
        noduriGen = 1
        timp = time.time()
        rez = ida_star(gr, NSOL, euristica, f)
        f.write(f'NODURI GENERATE IN TOTAL PENTRU IDA* {euristica}: {noduriGen}\n\n----------------\n\n')
        print(f'Timp IDA* {euristica}: {time.time() - timp if rez == 0 else " nu a terminat executia"}')

    f.close()
