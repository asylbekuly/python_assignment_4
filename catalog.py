class Car:
    def __init__(self, id, mark, model, year,price):
        self.id = id
        self.mark = mark
        self.model = model
        self.year = year
        self.price = price



    def __str__(self):
        return f" {self.id} {self.mark} {self.model} {self.year} - ${self.price}"


# Encapsulation: Getters and Setters
    def set_id(self,id):
        self.id = id
    def get_id(self):
        return self.id
    def get_mark(self):
        return self.mark


    def set_mark(self, mark):
        self.mark = mark


    def get_model(self):
        return self.model


    def set_model(self, model):
        self.model = model

    def set_year(self,year):
        self.year=year

    def get_year(self):
        return self.year
    def get_price(self):
        return self.price


    def set_price(self, price):
        self.price = price


class RentalCatalog:
    def __init__(self):
        self.cars = []

    # Encapsulation: Getters and Setters
    def get_cars(self):
        return self.cars

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car_id):
        car_to_remove = None
        for car in self.cars:
            if car.get_id() == car_id:
                car_to_remove = car
                break
        if car_to_remove:
            self.cars.remove(car_to_remove)
            return True
        return False

    def search_car(self, search_term):
        search_term = search_term.lower()
        return [car for car in self.cars if search_term in car.get_mark().lower() or
                search_term in car.get_model().lower() or
                search_term in str(car.get_year()) or
                search_term in str(car.get_id())]

    def search_car_by_id(self, car_id):
        # Assuming car_id is an integer
        return next((car for car in self.cars if car.get_id() == car_id), None)
    def search_car_by_mark(self, mark):
        mark = mark.lower()
        return [car for car in self.cars if car.get_mark().lower() == mark]
    def list_cars(self):
        for car in self.cars:
            print(car)