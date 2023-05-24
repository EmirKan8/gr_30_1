class Phone:
    def __init__(self):
        self.__sim_cards_list = []

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def call(self, sim_card_number, call_to_number):
        for sim_card in self.__sim_cards_list:
            if sim_card_number == sim_card["number"]:
                print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card['operator']}")
                break


class SmartPhone(Computer, Phone):
    def use_gps(self, location):
        print(f"Прокладывается маршрут до {location} с помощью GPS")


    def __str__(self):
        return f"CPU: {self.get_cpu()}, Memory: {self.get_memory()}, Sim Cards List: {self.get_sim_cards_list()}"


    def __eq__(self, other):
        if isinstance(other, Computer):
            return self.get_memory() == other.get_memory()
        return False


    def __ne__(self, other):
        if isinstance(other, Computer):
            return self.get_memory() != other.get_memory()
        return False


    def __lt__(self, other):
        if isinstance(other, Computer):
            return self.get_memory() < other.get_memory()
        return False


    def __le__(self, other):
        if isinstance(other, Computer):
            return self.get_memory() <= other.get_memory()
        return False


    def __gt__(self, other):
        if isinstance(other, Computer):
            return self.get_memory() > other.get_memory()
        return False


    def __ge__(self, other):
        if isinstance(other, Computer):
            return self.get_memory() >= other.get_memory()
        return False


computer = Computer("Intel Core i7", 8)
phone = Phone()
smartphone1 = SmartPhone("Qualcomm Snapdragon", 6)
smartphone2 = SmartPhone("Apple A14 Bionic", 12)

phone.set_sim_cards_list([{"number": 1, "operator": "Beeline"}, {"number": 2, "operator": "MegaCom"}])
smartphone1.set_sim_cards_list([{"number": 1, "operator": "Beeline"}, {"number": 2, "operator": "MegaCom"}])
smartphone2.set_sim_cards_list([{"number": 1, "operator": "O!"}, {"number": 2, "operator": "MegaFon"}])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

computer.set_memory(16)
print(computer.get_memory())

phone.call(1, "+996 555 123 456")
smartphone1.use_gps("Bishkek")
smartphone2.make_computations()

print(computer == smartphone1)
print(computer != smartphone2)
print(smartphone1 < smartphone2)
print(smartphone2 <= computer)
print(smartphone1 > computer)
print(smartphone2 >= smartphone1)
