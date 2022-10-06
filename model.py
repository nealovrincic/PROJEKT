class Stanje:
    def __init__(self, dnevi_v_tednu):
        self.dnevi_v_tednu = dnevi_v_tednu


class Dan_v_tednu:
    def __init__(self, ime_vaje, vaje):
        self.ime_vaje = ime_vaje
        self.vaje = vaje

    def stevilo_neopravljenih(self):
        neopravljena = 0
        for vaja in self.vaje:
            if not vaja.opravljeno:
                neopravljena += 1
        return neopravljena 
    
    def dodaj_vajo(self, vaja):
        self.vaje.append(vaja)

class Vaja:
    def __init__(self, ime, teza, st_ponovitev, st_setov, opravljeno=False):
        self.ime = ime
        self.teza = teza
        self.st_ponovitev = st_ponovitev
        self.st_setov = st_setov
        self.opravljeno = opravljeno
    
    def opravi(self):
        self.opravljeno = True

    