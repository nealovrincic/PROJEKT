import bottle
from model import Stanje, Vaja
from rekordi import Rekordi


SIFRIRNI_KLJUC = "To je poseben šifrirni ključ"

IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(dnevi_v_tednu=[])

IME_DATOTEKE_REKORDI = "rekordi.json"
try:
    rekordi = Rekordi.preberi_iz_datoteke(IME_DATOTEKE_REKORDI)
except FileNotFoundError:
    rekordi = Rekordi({})

def ime_uporabnikove_datoteke(uporabnisko_ime):
    return f"stanja_uporabnikov/{uporabnisko_ime}.json"

def stanje_trenutnega_uporabnika():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    if uporabnisko_ime == None:
        bottle.redirect("/prijava/")
    else:
        uporabnisko_ime = uporabnisko_ime
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    try:
        stanje = Stanje.preberi_iz_datoteke(ime_datoteke)
    except FileNotFoundError:
        stanje = Stanje.preberi_iz_datoteke("primer-stanja.json")
        stanje.shrani_v_datoteko(ime_datoteke)
    return stanje

def shrani_stanje_trenutnega_uporabnika(stanje):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    stanje.shrani_v_datoteko(ime_datoteke)

@bottle.get("/registracija/")
def naslovna_stran_get():
    return bottle.template("registracija.html")

@bottle.post("/registracija/")

@bottle.get("/prijava/")
def prijava():
    return bottle.template("prijava.html")

@bottle.post("/prijava/")
def prijava_post():
    ime = bottle.request.forms.getunicode("ime")
    priimek = bottle.request.forms.getunicode("priimek")
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo = bottle.request.forms.getunicode("geslo")
    bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/", secret=SIFRIRNI_KLJUC)
    bottle.redirect("/zacetna_stran/")

@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    bottle.redirect("/naslovna_stran/")


@bottle.get("/naslovna_stran/")
def naslovna_stran_get():
    return bottle.template("naslovna_stran.html")

@bottle.get("/rekordi/")
def rekordi_get():
    return bottle.template("rekordi.html")

@bottle.get("/treningi/")
def naslovna_stran_get():
    return bottle.template("treningi.html")

@bottle.get("/zacetna_stran/")
def zacetna_stran():
    return bottle.template(
        "zacetna_stran.html"
    )

def url_dneva(id_dneva):
    return f"/dan/{id_dneva}/"

@bottle.get("/dan/<id_dneva:int>/")
def prikazi_dan(id_dneva):
    stanje = stanje_trenutnega_uporabnika()
    dan = stanje.dnevi_v_tednu[id_dneva]
    return bottle.template(
        "dan.html"
    )

@bottle.post("/opravi/<id_dneva:int>/<id_vaje:int>/")
def opravi(id_dneva, id_vaje):
    stanje = stanje_trenutnega_uporabnika()
    dan = stanje.dnevi_v_tednu[id_dneva]
    vaja = dan.vaje[id_vaje]
    vaja.opravi()
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_dneva(id_dneva))

@bottle.post("/dodaj-vajo/<id_dneva:int>/")
def dodaj_vajo(id_dneva):
    stanje = stanje_trenutnega_uporabnika()
    dan = stanje.dnevi_v_tednu[id_dneva]
    ime_vaje = bottle.request.forms.getunicode("ime vaje")
    teza = bottle.request.forms.getunicode("teža")
    st_ponovitev = bottle.request.forms.getunicode("število ponovitev")
    st_setov = bottle.request.forms.getunicode("število setov")
    vaja = Vaja(ime_vaje, teza, st_ponovitev, st_setov)
    dan.dodaj_vajo(vaja)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_dneva(id_dneva))

@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"

bottle.run(debug=True, reloader=True)

