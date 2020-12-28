class Moeder:
    def voel_aan(self):
        print("Dat komt goed, ik voel het")
    def praat(self):
        print("Ik ga me daar niet over uitspreken, maar naar het schijnt ...")

class Vader:
    def redeneer(self):
        print("Ik redeneer gewoon rechtdoor")
    def praat(self):
        print("Ja, nee of iets anders")

class VadersKind(Vader,Moeder):
    def __init__(self, naam):
        self.naam = naam

class MoedersKind(Moeder, Vader):
    def __init__(self, naam):
        self.naam = naam

arno = VadersKind("Arno")
print(arno.naam)
arno.voel_aan()
arno.redeneer()
arno.praat()

print()

celine = MoedersKind("Celine")
print(celine.naam)
celine.voel_aan()
celine.redeneer()
celine.praat()

"""
Output

Arno
Dat komt goed, ik voel het
Ik redeneer gewoon rechtdoor
Ja, nee of iets anders

Celine
Dat komt goed, ik voel het
Ik redeneer gewoon rechtdoor
Ik ga me daar niet over uitspreken, maar naar het schijnt ...
"""



