from lipuke import Lipuke
from ehdokas import Ehdokas
from vaalilogger import VaaliLogger


def lue_lipukkeet(
    syöte: list[str], logger: VaaliLogger
) -> tuple[str, int, list[Ehdokas], list[Lipuke]]:
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

    logger.lisää_rivi(f"Ehdokkaita on {ehdokasmäärä}")
    logger.lisää_rivi(f"Valitaan {paikkamäärä} ehdokasta")

    lipukkeet = []
    while (rivi := next(iteraattori)) != "0":
        osat = rivi.split()[1:-1]
        ids = [int(x) for x in osat]
        lipukkeet.append(Lipuke(ids))

    i = 1
    ehdokkaat = []
    while i <= ehdokasmäärä:
        nimi = next(iteraattori)[1:-1]
        ehdokkaat.append(Ehdokas(nimi, i))
        i += 1

    vaalin_nimi = next(iteraattori)[1:-1]

    return (vaalin_nimi, paikkamäärä, ehdokkaat, lipukkeet)
