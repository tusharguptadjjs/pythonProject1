class ElectronicGadget:
    def __init__(self,battery,size,type):
        self.battery = battery
        self.size = size
        self.type = type

    def PrintDetails(self):
        return f"battery is {self.battery},size is {self.size},type is {self.type}"

class PocketyGadget(ElectronicGadget):
    def __init__(self,battery,size,type,price):
        super().__init__(battery,size,type)
        self.price = price
    def PrintDetail(self):
        return f"battery is {self.battery},size is {self.size},type is {self.type}, price is {self.price}"


class Phone(PocketyGadget):
    def __init__(self,battery,size,type,price,Storage):
        super().__init__(battery,size,type,price)
        self.Storage=Storage
    def Printbill(self):
       return f"battery is {self.battery},size is {self.size},type is {self.type}, price is {self.price} , Storage is {self.Storage}"

p=Phone(5000,5,"phone",10000,"64 gb")
det = p.Printbill()
print(det)

