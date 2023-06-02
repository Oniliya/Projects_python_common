class Tyre:
    def __init__(self, weather: str, brand: str):
        self.weather = weather
        self.brand = brand

    def __repr__(self):
        return f'{"Летняя" if self.weather == "summer" else "Зимняя"} резина марки {self.brand}'    


class Wheel:
    def __init__(self, size: int, brand: str, weather_t: int, brand_t: str = ''):
        self.size = size
        self.brand = brand
        
        self.tyre = Tyre (weather_t, brand_t if brand_t else brand)


class Car:
    def __init__(self, mark: str, color: str, year: int, size_w: int = 17, brand_w: str = 'FireStone'):
        self.mark= mark
        self.color = color
        self.year = year
        self.weels = [Wheel(size_w, brand_w, 'summer'), 
                      Wheel(size_w, brand_w, 'summer'), 
                      Wheel(size_w, brand_w, 'summer'), 
                      Wheel(size_w, brand_w, 'winter') ]
   
    def __str__(self):
        return f'car of mark {self.mark} color {self.color} year {self.year}'



    def horn(self):
        print(f'car {self.mark} makes "bi-bib-biiii"')

my_car = Car('Mazda', 'black', 2019)

new_car = Car('Tesla', 'white', 2023, 20, 'Белшина')


my_car.horn()
new_car.horn()

print(my_car.mark)
print(new_car.mark)

my_car.weels[1].brand='Запаска'
my_car.weels[1].size=14

print(my_car.weels[0].brand)
print(new_car.weels[0].brand)


for wheell in my_car.weels:
    print(wheell.size, wheell.brand, wheell.tyre)

print(my_car)