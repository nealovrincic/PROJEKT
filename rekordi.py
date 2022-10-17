import json

class Rekordi:
    def __init__(self, rekordi):
        self.rekordi = rekordi
        if len(rekordi) == 0:
            self.rekordi["squat"] = 0
            self.rekordi["deadlift"] = 0
            self.rekordi["bench press"] = 0


    def dodaj_rekord(self, ime_vaje, teza):
        if ime_vaje in self.rekordi and int(teza) > int(self.rekordi[ime_vaje]):
            self.rekordi[ime_vaje] = teza
        

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            json.dump(self.rekordi, dat, indent=4, ensure_ascii=False)


    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Rekordi(slovar)