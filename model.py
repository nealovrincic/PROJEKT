import json
from rekordi import Rekordi

class Stanje:
    def __init__(self, dnevi_v_tednu, rekordi):
        self.dnevi_v_tednu = dnevi_v_tednu
        self.rekordi = rekordi
        if len(dnevi_v_tednu) == 0:       
            self.dodaj_nov_teden()


    def dodaj_nov_teden(self):
        ponedeljkove_vaje = []
        ponedeljek = Dan_v_tednu("ponedeljek", ponedeljkove_vaje)
        torkove_vaje = []
        torek = Dan_v_tednu("torek", torkove_vaje)
        sredine_vaje = []
        sreda = Dan_v_tednu("sreda", sredine_vaje)
        cetrtkove_vaje = []
        cetrtek = Dan_v_tednu("cetrtek", cetrtkove_vaje)
        petkove_vaje = []
        petek = Dan_v_tednu("petek", petkove_vaje)
        sobotine_vaje = []
        sobota = Dan_v_tednu("sobota", sobotine_vaje)
        nedeljine_vaje = []
        nedelja = Dan_v_tednu("nedelja", nedeljine_vaje)
        self.dnevi_v_tednu = [ponedeljek, torek, sreda, cetrtek, petek, sobota, nedelja]


    def v_slovar(self):
        return {
            "dnevi": [dan.v_slovar() for dan in self.dnevi_v_tednu],
            "rekordi": self.rekordi.rekordi #ker je ze slovar, ne pretvarjamo se enkrat
        }


    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje(
            [
                Dan_v_tednu.iz_slovarja(sl_dnevi_v_tednu)   
                for sl_dnevi_v_tednu in slovar["dnevi"]      
            ],
            Rekordi(slovar["rekordi"])
        )
        return stanje


    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat, indent=4, ensure_ascii=False)


    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja(slovar)


class Dan_v_tednu:
    def __init__(self, ime, vaje):
        self.ime = ime
        self.vaje = vaje


    def stevilo_neopravljenih(self):
        neopravljena = 0
        for vaja in self.vaje:
            if not vaja.opravljeno:   
                neopravljena += 1
        return neopravljena 
    

    def dodaj_vajo(self, vaja):
        self.vaje.append(vaja)


    def izbrisi_vajo(self, id_vaje):
        self.vaje.pop(id_vaje)
    

    def v_slovar(self):
        return {
            "ime": self.ime,
            "vaje": [vaja.v_slovar() for vaja in self.vaje],
        }


    @staticmethod
    def iz_slovarja(slovar):
        return Dan_v_tednu(
            slovar["ime"],
            [Vaja.iz_slovarja(sl_vaje) for sl_vaje in slovar["vaje"]],       ##################
        )


class Vaja:
    def __init__(self, ime, teza, st_ponovitev, st_setov, opravljeno=False):
        self.ime = ime
        self.teza = teza
        self.st_ponovitev = st_ponovitev
        self.st_setov = st_setov
        self.opravljeno = opravljeno
    

    def opravi(self):
        self.opravljeno = True


    def v_slovar(self):
        return {
            "ime": self.ime,
            "teza": self.teza,
            "stevilo ponovitev": self.st_ponovitev,
            "stevilo setov": self.st_setov,
            "opravljeno": self.opravljeno,
        }


    @staticmethod
    def iz_slovarja(slovar):
        return Vaja(
            slovar["ime"],
            slovar["teza"],
            slovar["stevilo ponovitev"],
            slovar["stevilo setov"],
            slovar["opravljeno"],
        )

