from auth import authenticate,Admin
from catalog import RentalCatalog, Car
from storage import Storage
from utils import display_admin_menu, display_user_menu, get_car_details

def main():
    user_data = {
        "Rabat": "1234",
        "Danial": "danial2005",
        "Ayan": "2005"
    }

    username = input("Username: ")
    password = input("Password: ")

    user = authenticate(username, password, user_data)
    if user is None:
        print("Authentication failed.")
        return

    is_admin = isinstance(user, Admin)
    catalog = RentalCatalog()
    storage = Storage('cars.json', 'json')  # or Storage('cars.csv', 'csv')

    try:
        catalog.cars = storage.load()
    except FileNotFoundError:
        print("No existing catalog found, starting with an empty catalog.")

    while True:
        if is_admin:
            display_admin_menu()
        else:
            display_user_menu()

        choice = input("Choose an option: ")

        if choice == '1':
            if is_admin:
                car_id,mark, model, year, price = get_car_details()
                car = Car(car_id,mark, model,year, price)
                catalog.add_car(car)
                storage.save(catalog.cars)
            else:
                catalog.list_cars()
        elif choice == '2':
            if is_admin:
                car_id = input("Enter the id of the car to remove: ")
                car_id = int(car_id)  # Convert to int if the ID is an integer
                if catalog.remove_car(car_id):
                    print(f"Car with ID {car_id} has been removed.")
                else:
                    print(f"No car with ID {car_id} found.")
                storage.save(catalog.cars)
            else:
                mark = input("Enter the mark of the car to search: ")
                found_cars = catalog.search_car_by_mark(mark)
                if found_cars:
                    print("Cars found:")
                    for car in found_cars:
                        print(car)
                else:
                    print("No cars found with the mark '%s'." % mark)
        elif choice == '3':
            if is_admin:
                catalog.list_cars()
            else:
                car_id = input("Enter the id of the car to buy: ")
                car_id = int(car_id)  # Convert to int if the ID is an integer
                car_to_buy = catalog.search_car_by_id(car_id)
                if car_to_buy:
                    catalog.remove_car(car_id)
                    storage.save(catalog.cars)
                    print(f"You have bought car with ID {car_id}")
                else:
                    print("Car not found.")
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
