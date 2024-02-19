import json
import csv
from catalog import Car

class Storage:
    def __init__(self, filename, filetype='json'):
        self.filename = filename
        self.filetype = filetype

    def save(self, data):
        if self.filetype == 'json':
            with open(self.filename, 'w') as file:
                # Use getters to access encapsulated data
                json.dump([{'id': car.get_id(), 'mark': car.get_mark(), 'model': car.get_model(), 'year': car.get_year(), 'price': car.get_price()} for car in data], file)
        elif self.filetype == 'csv':
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'mark', 'model', 'year', 'price'])
                # Use getters to access encapsulated data
                for car in data:
                    writer.writerow([car.get_id(), car.get_mark(), car.get_model(), car.get_year(),car.get_price()])

    def load(self):
        try:
            if self.filetype == 'json':
                with open(self.filename, 'r') as file:
                    return [Car(**car) for car in json.load(file)]
            elif self.filetype == 'csv':
                with open(self.filename, 'r') as file:
                    reader = csv.DictReader(file)
                    return [Car(int(row['id']), row['mark'], row['model'], int(row['year']), float(row['price'])) for row in reader]
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist.")
            return []
        except ValueError:
            print(f"Invalid data format in {self.filename}.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
