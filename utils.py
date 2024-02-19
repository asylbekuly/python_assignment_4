def display_admin_menu():
    print("1. Add car")
    print("2. Remove car")
    print("3. List all cars")
    print("4. Exit")
def display_user_menu():
    print("1. List all cars")
    print("2. Search for a car")
    print("3. Buy a car")
    print("4. Exit")

def get_car_details():
    car_id = input("Enter the car id: ")
    car_id = int(car_id)
    mark = input("Enter the car Mark: ")
    model = input("Enter the model of the car: ")
    year = input("Enter the year of the car: ")
    price = float(input("Enter the price: "))
    return car_id,mark, model,year, price
