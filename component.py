from utils import Complex, Point

Resister = 0
Capacitor = 1
Inductor = 2
VoltageSource = 3
CurrentSource = 4
ComponentType = ["None", "Resistor", "Inductor", "Capacitor"]


class Component(object):
    omega = -1.0

    def __init__(self, name="", ctype="None", r=-1, l=-1, c=-1, x=0, y=0):
        self.name = name
        self.type = ctype
        self.point = Point(x, y)

        self.resistance = r
        self.inductance = l
        self.capacitance = c

        self.impedance = Complex(0, 0)

    def set_point(self, x=None, y=None):
        self.point.reset(x, y)

    def get_value(self):
        if self.type == "Resistance":
            self.impedance = Complex(self.resistance, 0)
        elif self.type == "Inductor":
            self.impedance = Complex(0, Component.omega*self.inductance)
        elif self.type == "Capacitor":
            self.impedance = Complex(0, -1/(Component.omega*self.capacitance))
        else:
            print("Not Identified")


class Resistor(Component):
    def __init__(self, name="", value=0):
        super().__init__(name=name, ctype="Resistor", r=value)
        print("Create An Resistor")


class Capacitor(Component):
    def __init__(self, name="", value=0):
        super().__init__(name=name, ctype="Capacitor", c=value)
        print("Create An Capacitor")


class Inductor(Component):
    def __init__(self, name="", value=0):
        super().__init__(name=name, ctype="Inductor", l=value)
        print("Create An Inductor")
