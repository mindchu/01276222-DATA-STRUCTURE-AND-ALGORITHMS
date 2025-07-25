class Parking:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

def check_car(a_park, b_park, num_car):
    while a_park.isEmpty() == False:
        temp = a_park.pop()
        b_park.push(temp)
        if num_car == temp:
            return True
    return False

def return_car(a_park, b_park):
    while b_park.isEmpty() == False:
        a_park.push(b_park.pop())

def check_park(max_car, soi_car, operations):
    a_park = Parking([int(car) for car in soi_car.split(",")])
    b_park = Parking()
    operation, num_car = operations.split()
    num_car = int(num_car)
    if operation == "arrive":
        if a_park.size() >= max_car:
            print(f"car {num_car} cannot arrive : Soi Full")
        elif check_car(a_park, b_park, num_car):
            print(f"car {num_car} already in soi")
        else:
            print(f"car {num_car} arrive! : Add Car {num_car}")
            return_car(a_park, b_park)
            a_park.push(num_car)
            return a_park.items
    elif operation == "depart":
        if check_car(a_park, b_park, num_car) == False:
            print(f"car {num_car} cannot depart : Dont Have Car {num_car}")
        else:
            b_park.pop()
            print(f"car {num_car} depart ! : Car {num_car} was remove")
    return_car(a_park, b_park)
    return a_park.items

print("******** Parking Lot ********")
max_car, soi_car, operations = [arg.strip() for arg in input("Enter max of car / car in soi / operation : ").split("/")]
max_car = int(max_car)
print(check_park(max_car, soi_car, operations))