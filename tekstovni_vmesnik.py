from model import Stanje, Dan_v_tednu, Vaja

stanje = Stanje([
    Dan_v_tednu(
        "ponedeljek", [
            Vaja("squat", 80, 12, 3, False),
            Vaja("deadlift", 90, 10, 4, False)
        ]
    ),
    Dan_v_tednu(
        "torek", [
            Vaja("hammer curl", 12, 8, 3, True)
        ]
    ),
    Dan_v_tednu(
        "sreda", [
            Vaja("squat", 90, 12, 3, False)
        ]
    )
])

def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")


def izberi_moznost(moznosti):
    """Uporabniku našteje možnosti ter vrne izbrano."""
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}.")

def izpisi_trenutno_stanje():
    for dan in stanje.dnevi_v_tednu:
        print (f"{dan.ime_vaje}: {dan.stevilo_neopravljenih()} neopravljenih")

def zacetni_pozdrav():
    print ("Pozdravljeni v programu za vodenje treningov in osebnih rekordov!")

def ponudi_moznosti():
    print("Kaj bi radi naredili?")
    izbrano_dejanje = izberi_moznost(
        [
            (dodaj_vajo, "dodal novo opravilo"),
            (opravi_vajo, "opravil opravilo"),
            (zakljuci_izvajanje, "odšel iz programa"),
        ]
    )
    izbrano_dejanje()

def tekstovni_vmesnik():
    zacetni_pozdrav()
    while True:
        izpisi_trenutno_stanje()
        ponudi_moznosti()