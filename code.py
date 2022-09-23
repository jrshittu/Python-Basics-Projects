
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_persons(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)
    
people = ["Tee", "Atom", "Gee", "Mee"]
    
for person in people:
    success = flight.add_persons(person)
    if success:
        print(person, "successfully onboard")
    else:
        print("No more space for", person)
            