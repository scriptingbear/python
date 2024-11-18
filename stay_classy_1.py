#experiment with classes, class members, instance members and static members

class Computer:
    #define class members available to all object instances
    _device_count = 0
    _voltage = 120

    #define constructor which initializes instance variables
    '''def __init__(self, maker, model, cpu, ram, cost):
        self.maker = maker
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.cost = cost
        '''
    def __init__(self, **kwargs):
        self.maker = kwargs["maker"]
        self.model = kwargs["model"]
        self.cpu = kwargs["cpu"]
        self.ram = kwargs["ram"]
        self.cost = kwargs["cost"]
        
        print("A new {0} {1} computer with a {2} GHz CPU and {3} GB ram " \
                  "costing ${4:8,.2f} has been created!".format(self.maker, self.model, self.cpu, self.ram, self.cost))
        #increment total number of computers
        Computer._device_count +=1
        print("{} computers have been created so far".format(Computer._device_count))

    @staticmethod
    def DeviceCount():
        return Computer._device_count


c1 = Computer(maker = "Dell", model = "XPS-13", cpu = 1.8, ram = 250, cost = 1295)
#print(c1.device_count)

c2 = Computer(maker = "Lenovo", model = "G550", cpu = 2.4, ram = 500, cost = 800.95)
#print(c2.device_count)
print(Computer.DeviceCount())
print(c2.DeviceCount())
