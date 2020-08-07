class Car(object):

    def __init__(self,model,color,company,speed_limit):
        self.color=color    
        self.company = company
        self.speed_limit= speed_limit
        self.model=model

    def start(self):
        print("started")

    def stop(self):
        print("stoped")

    def accelerate(self):
        print("accelerate functionalty here")
    
    def change_gear(self):
        print("gear_changed")

audi=Car("A6","blue","audi",100)
print(audi.start())
print(audi.stop())
print(audi.change_gear())
print(audi.accelerate())
