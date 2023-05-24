class Mirlan:
    people = True
    pi = 3.141592
    def __init__(self, name, age, surname):
        self.age = age
        self.surname = surname
        self.name  = name


class Islam(Mirlan):
    def __init__(self, name, surname):
        super.__init__(name, surname)

    def run(self):
        print(f"меня зовут {self.name}")