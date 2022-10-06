from model import Stanje, Dan_v_tednu, Vaja

IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(dnevi_v_tednu=[])

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

def prikaz_dneva(dan):
    neopravljena = dan.stevilo_neopravljenih()
    return f"{dan.ime.upper()} ({neopravljena})"

def prikaz_vaje(vaja):
    if vaja.opravljeno:
        return f"☑︎ {vaja.ime}"
    else:
        return f"☐ {vaja.ime}"

def izberi_dan(stanje):
    print("Izberite dan:")
    return izberi_moznost(
        [
            (dan, prikaz_dneva(dan))
            for dan in stanje.dnevi_v_tednu
        ]
    )


def izberi_vajo(dan):
    print("Izberite opravilo:")
    return izberi_moznost(
        [(vaja, prikaz_vaje(vaja)) for vaja in dan.opravila]
    )

def izpisi_trenutno_stanje():
    for dan in stanje.dnevi_v_tednu:
        print (f"{dan.ime_vaje}: {dan.stevilo_neopravljenih()} neopravljenih")

def zacetni_pozdrav():
    print ("Pozdravljeni v programu za vodenje treningov in osebnih rekordov!")

def dodaj_vajo():
    dan = izberi_dan(stanje)
    print("Vnesite podatke nove vaje.")
    ime = input("Opis> ")
    teza = input("Teža> ")
    st_ponovitev = input("Število ponovitev> ")
    st_setov = input("Število setov> ")
    nova_vaja = Vaja(ime, teza, st_ponovitev, st_setov)
    dan.dodaj_vajo(nova_vaja)

def opravi_vajo():
    dan = izberi_dan(stanje)
    vaja = izberi_vajo(dan)
    vaja.opravi()

def zakljuci_izvajanje():
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    print("Nasvidenje!")
    exit()

def ponudi_moznosti():
    print("Kaj bi radi naredili?")
    izbrano_dejanje = izberi_moznost(
        [
            (dodaj_vajo, "dodal novo vajo"),
            (opravi_vajo, "opravil vajo"),
            (zakljuci_izvajanje, "odšel iz programa"),
        ]
    )
    izbrano_dejanje()

def tekstovni_vmesnik():
    zacetni_pozdrav()
    while True:
        izpisi_trenutno_stanje()
        ponudi_moznosti()