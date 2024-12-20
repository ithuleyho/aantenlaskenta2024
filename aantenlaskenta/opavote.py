from aantenlaskenta.lipuke import Lipuke
from aantenlaskenta.ehdokas import Ehdokas
from aantenlaskenta.vaalilogger import vaalilogger


def lue_lipukkeet(syöte: list[str]) -> tuple[str, int, list[Ehdokas], list[Lipuke], int]:
    """
    Ottaa parametrina opavoten generoiman datan rivitettynä.
    Palauttaa (vaalin nimi, paikkojen määrä, ehdokkaat, lipukkeet)

    ```
    with open("vaali.txt") as f:
        vaali, paikat, ehdokkaat, lipukkeet = lue_lipukkeet(f.readlines())
    ```
    """
    iteraattori = iter(map(str.strip, syöte))

    eka_rivi = next(iteraattori).split()
    if len(eka_rivi) != 2:
        raise Exception("Ensimmäisellä rivillä pitää olla tasan kaksi lukua")

    ehdokasmäärä, paikkamäärä = [int(x) for x in eka_rivi]

    vaalilogger.lisää_rivi(f"Ehdokkaita on {ehdokasmäärä}")
    vaalilogger.lisää_rivi(f"Valitaan {paikkamäärä} ehdokasta")

    lipukkeet = []
    hylätyt_äänet = 0
    while (rivi := next(iteraattori)) != "0":
        osat = rivi.split()[1:-1]
        ids = [int(x) for x in osat]
        if len(ids) == 0:
            hylätyt_äänet += 1
            continue

        lipukkeet.append(Lipuke(ids))

    i = 1
    ehdokkaat = []
    while i <= ehdokasmäärä:
        nimi = next(iteraattori)[1:-1]
        ehdokkaat.append(Ehdokas(nimi, i))
        i += 1

    vaalin_nimi = next(iteraattori)[1:-1]

    return (vaalin_nimi, paikkamäärä, ehdokkaat, lipukkeet, hylätyt_äänet)
