class parrot:
    species='Bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name,'\tAge:',self.age,'\n')

p1=parrot('woo',12)
p1.display()
p1=parrot('blu',8)
p1.display()