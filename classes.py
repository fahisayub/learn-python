class Flight():
    def __init__(self,x):
        self.capacity=x
        self.passengers=[]
    def add_passenger(self,name):
        if not self.check_capacity():
            return False
        self.passengers.append(name)
        return True
    def check_capacity(self):
        return self.capacity - len(self.passengers)

airindia= Flight(3)
queue=['Fahiz','Arun','George','Aman']
for name in queue:
    if airindia.add_passenger(name):
        print(f'seat booked for {name} successfully')
    else:
        print('no available seats')