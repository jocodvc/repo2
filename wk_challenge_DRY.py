# de variables
landen_lijst = []
punten_lijst = []
doelsaldo_lijst = []
aantal_wedstrijden_lijst = []
wedstrijden_lijst = []

# constante voor aantal landen in groep.
AANTAL_LANDEN = 4 # minimaal 3 landen.

# vraag 1
for x in range(1, AANTAL_LANDEN + 1):
    landen_lijst.append(input(f"Voer land {x} in:"))

# wedstrijden regelen.
# maak een list van tuples
for y in range(AANTAL_LANDEN):
    punten_lijst.append(0)
    doelsaldo_lijst.append(0)
    aantal_wedstrijden_lijst.append(0)
    for z in range(y + 1, AANTAL_LANDEN):
        wedstrijden_lijst.append((landen_lijst[y], landen_lijst[z]))

# even een testje voor de lijst met wedstrijden.
print(wedstrijden_lijst)

# Ok, dan kunnen we nu alle wedstrijden uitvragen en de score bepalen.
for wedstrijd in wedstrijden_lijst:
    i_a = landen_lijst.index(wedstrijd[0])
    i_b = landen_lijst.index(wedstrijd[1])
    aantal_wedstrijden_lijst[i_a] += 1
    aantal_wedstrijden_lijst[i_b] += 1

    print(f"Wedstrijd {landen_lijst[i_a]} tegen {landen_lijst[i_b]}")
    doelpunten_la = int(input(f"Hoeveel doelpunten voor: {landen_lijst[i_a]}"))
    doelpunten_lb = int(input(f"Hoeveel doelpunten voor: {landen_lijst[i_b]}"))

    if doelpunten_la > doelpunten_lb:
        punten_lijst[i_a] += 3
        doelsaldo_lijst[i_a] += doelpunten_la - doelpunten_lb
        doelsaldo_lijst[i_b] += doelpunten_lb - doelpunten_la
    elif doelpunten_la == doelpunten_lb:
        punten_lijst[i_a] += 1
        punten_lijst[i_b] += 1
        # doelsaldo niet relevant want evenveel voor als tegen
    else:
        punten_lijst[i_b] += 3
        doelsaldo_lijst[i_a] += doelpunten_la - doelpunten_lb
        doelsaldo_lijst[i_b] += doelpunten_lb - doelpunten_la

    print(f"Wedstrijd {landen_lijst[i_a]} - {landen_lijst[i_b]} eindigde in: {doelpunten_la} - {doelpunten_lb}")
    print("Overzicht groep A")
    for idx, land in enumerate(landen_lijst):
        print(f"{land} ({aantal_wedstrijden_lijst[idx]}): punten {punten_lijst[idx]};  doelsaldo:  {doelsaldo_lijst[idx]}")