'''
Obiective sesiune: Programare Orientata pe Obiecte
Sa intelegem ce este programarea orientata pe obiecte
Sa stim ce este o clasa si un obiect
Sa stim ce sunt atributele/fild-urile si metodele
Sa putem sa instantiem un obiect
Sa aflam ce este un constructor
Sa vedem cum se folosesc atributele si metodele dintr-o clasa
'''

#clasa- reprezinta un set de atribite si metode(functii) care definesc un element real
#atributele unei clase - descriu cum ar trebui sa arate entitatea_ ce proprietati va avea
#metodele unei clase - descriu ce ar trebui sa faca entitatea _cum ar trebui sa se comporte
#self - este instanta clasei, ajuta clasa sa aiba acces la atributele clasei


class Car: #definim clasa

    #definim atributele/fild-urile clasei
    make = "Dacia"
    model = None
    year = 2022
    color = None

    #definim metode
    def accelerate(self):
        print("Vruum!")


car1 = Car() # initializam obiectul de tip Car
car2 = Car() #car2 este instanta clasei

#dupa . avem acces la atribute si metodele
car1.model = "Duster" #putem suprascrie valori
car1.accelerate()



class Cafea: #definim clasa Cafea

    def __init__(self, tip, intensitate, aroma, cantitate): #definim constructorul clasei
        self.tip = tip
        self.intensitate = intensitate
        self.aroma = aroma
        self.cantitate = cantitate

    def prepara(self): #definim metoda prepara() metoda fara param
        print(f"Prepar cafea {self.tip} cu intensitatea {self.intensitate} și aroma {self.aroma}.")

    def adauga_lapte(self, cantitate_lapte): #definim adauga_lapte() metoda cu param
        print(f"Am adăugat {cantitate_lapte}ml de lapte la cafeaua {self.tip}.")
        spuma_lapte(cantitate_lapte) #aici apelez functia spuma_lapte() creata in afara clasei

    def adauga_zahar(self, cantitate_zahar):#definim adauga_zahar() metoda cu param
        print(f"Am adăugat {cantitate_zahar}g de zahăr la cafeaua {self.tip}.")

    def schimba_aroma(self, noua_aroma):#definim metoda schimba_aroma() metoda cu param
        print(f"Am schimbat aroma cafelei {self.tip} cu {noua_aroma}.")



#diferenta dintre functii si metode este data de faptul ca functiile sunt independente, iar metodele sunt create in interiorul clasei

def spuma_lapte(cantitate_lapte): #definim functia spuma_lapte() care va avea un param
    print(f"Am făcut spumă de lapte cu {cantitate_lapte}ml.")

#obiect - este reprez reala a unui tipar de clasa si se mai numeste si o instanta a clasei

cafea_espresso = Cafea("Espresso", "tare", "intensa", 30)  #am creat obiectul folosindu-ma de class Cafea
cafea_cu_lapte = Cafea("Cafea cu lapte", "tare", "vanilie", 120) #am creat obiectul folosindu-ma de class Cafea
cafea_simpla1 = Cafea("Cafea simpla", "normala", "caramel sarat", 250)
cafea_simpla2 = Cafea(tip="Cafea simpla", intensitate="normala", aroma="caramel sarat", cantitate=250)
cafea_simpla3 = Cafea(tip="Cafea simpla", intensitate="normala", aroma="cioco", cantitate=120)
cafea_simpla4 = Cafea("Cafea simpla", "normala", "vanilie", 300)


aroma = "carmel"
cafea_cu_lapte.schimba_aroma(aroma) #apelez pe obiectul creat cafea_cu_lapte  metoda schimba_aroma(), care va avea ca atribut "caramel saral",
cafea_cu_lapte.adauga_lapte(50)
cafea_cu_lapte.prepara()

cafea_espresso.prepara() #apelez metoda prepara() din clasa Cafea pe obiectul creat
cafea_espresso.adauga_lapte(20) #apelez metoda adauga_lapte() din clasa Cafea pe obiectul creat si voi da valoare pt argumentul functiei apelate
cafea_espresso.adauga_zahar(10) #apelez metoda adauga_zahar() din clasa Cafea pe obiectul creat si voi da valoare pt argumentul functiei apelate
cafea_espresso.schimba_aroma("ciocolată")
cafea_simpla1.adauga_lapte(20)
cafea_simpla1.prepara()


#Constructor - este elementul care este folosit pentru construirea obiectului. Atunci cand se face instantierea unui obiect, sistemul se foloseste de un constructor
#Constructor - explicit =>> este ca o metoda care poarte numele de _init_ si se foloseste cand vrem sa controlam felul in care se populeaza atributele unui obiect
                             #daca avem un constructor cu param, instantierea obiectului este oblicatoriu sa se faca cu argumente
#Constructor - implicit -> daca nu definim niciun constructor explicit, nu inseamna ca nu se va folosi un constructor. In cazul asta se va apela constructorul inclus in suita python



#exemplu - anunt de vanzare apartement
class AnuntVanzareApartament:
    def __init__(self, titlu, descriere, pret, suprafata, numar_camere, adresa):
        self.titlu = titlu
        self.descriere = descriere
        self.pret = pret
        self.suprafata = suprafata
        self.numar_camere = numar_camere
        self.adresa = adresa

    def afiseaza_detalii(self):
        print(f"Titlu anunț: {self.titlu}")
        print(f"Descriere: {self.descriere}")
        print(f"Preț: {self.pret} euro")
        print(f"Suprafață: {self.suprafata} mp")
        print(f"Număr camere: {self.numar_camere}")
        print(f"Adresă: {self.adresa}")

    def actualizeaza_pret(self, nou_pret):
        self.pret = nou_pret
        print(f"Prețul apartamentului a fost actualizat la {self.pret} euro.")

# vom instantiat clasa AnuntVanzareApartament, adica vom crea obiecte cu ajutorul clasei AnuntVanzareApartament
anunt_apartament_2 = AnuntVanzareApartament(
    titlu="Apartament cu vedere la parc",
    descriere="Apartament cu 2 camere situat în zona centrală.",
    pret=75000,
    suprafata=70,
    numar_camere=2,
    adresa="Str. Libertății, nr. 10, București"
)
anunt_apartament_3 = AnuntVanzareApartament(
    titlu="Apartament cu vedere la mare",
    descriere="Apartament cu 3 camere situat pe faleza",
    pret=150000,
    suprafata=105,
    numar_camere=3,
    adresa="Mamaia"
)
print("---" * 15)
anunt_apartament_2.afiseaza_detalii()
print("---" * 15)
anunt_apartament_2.actualizeaza_pret(72000)
print("---" * 15)
anunt_apartament_2.afiseaza_detalii()
print("---" * 15)
# anunt_apartament_3.afiseaza_detalii()
#
pret_apartament = anunt_apartament_2.pret
print(pret_apartament)
print(anunt_apartament_2.pret)







print("---"*100)

class Complex:

    def __init__(self, real, imag):
        self.r = real
        self.i = imag

z = Complex(3.0, -4.5)
print(z)

# IT ACTUALLY WORKS
