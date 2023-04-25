class Samochod:

    def __init__(self, marka, model, rok_prod, przebieg):
        self.marka = marka
        self.model = model
        self.rok_prod = rok_prod
        self.przebieg = przebieg

    def __str__(self):
       return f"Opis pojazdu: {self.marka} {self.model}, rok prod: {self.rok_prod}, przebieg: {self.przebieg} km."

    def __lt__(self, other):
        return ((self.przebieg) < (other.przebieg))

    __repr__ = __str__


sam1 = Samochod("Peugeot", "5008", 2018, 15000)
sam2 = Samochod("Audi", "A4", 2020, 10000)
sam3 = Samochod("Renault", "Clio", 2014, 35000)

car_list = [sam1, sam2, sam3]

print(car_list)
print(sam1 < sam2)
print(sam2 < sam1)
print(sam1 < sam3)

list.sort(car_list)
print(car_list)

