class Appliance:
    def __init__(self, name, power):
        self.__device_name = name
        self.__power_consumption = power
        self.__power_status = "OFF"
        
    def get_name(self):
        return self.__device_name
    def get_power(self):
        return self.__power_consumption
    def get_status(self):
        return self.__power_status
    def turn_on(self):
        self.__power_status = "ON"
    def turn_off(self):
        self.__power_status = "OFF"
    def display_status(self):
        pass

class SmartLight(Appliance):
    def __init__(self, name, power, brightness):
        super().__init__(name, power)
        self.__brightness = brightness
        
    def display_status(self):
        print("SmartLight Status")
        print(f"Device Name       : {self.get_name()}")
        print(f"Power Status      : {self.get_status()}")
        print(f"Power Consumption : {self.get_power()} W")
        print(f"Brightness Level  : {self.__brightness}%")

class SmartFan(Appliance):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.__speed = speed
        
    def display_status(self):
        print("SmartFan Status")
        print(f"Device Name       : {self.get_name()}")
        print(f"Power Status      : {self.get_status()}")
        print(f"Power Consumption : {self.get_power()} W")
        print(f"Fan Speed         : Level {self.__speed}")


try:
    l_name = input().strip()
    l_power = int(input().strip())
    l_bright = int(input().strip())

    f_name = input().strip()
    f_power = int(input().strip())
    f_speed = int(input().strip())

    light = SmartLight(l_name, l_power, l_bright)
    fan = SmartFan(f_name, f_power, f_speed)

    light.turn_on()
    fan.turn_on()
    devices = [light, fan]
    for i in range(len(devices)):
        devices[i].display_status()
        if i < len(devices) - 1:
            print()
except EOFError:
    pass