class Flight():
    def __init__(self, space):
        self.space = space
        self.passengers = []
        
    def add_persons(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.space - len(self.passengers)
    
flight = Flight(3)
peers = ["Tera", "Kita", "Feran", "Tictak"]

for peer in peers:
    onboard = flight.add_persons(peer)
    if onboard:
        print(peer, "is onboard successfully")
    else:
        print("No more space to accomodate", peer)