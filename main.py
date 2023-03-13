import csv
import datetime

class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Classic Pizza"
        self.cost = 10.0

class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
        self.cost = 12.0

class TurkishPizza(Pizza):
    def __init__(self):
        self.description = "Turkish Pizza"
        self.cost = 15.0

class SadePizza(Pizza):
    def __init__(self):
        self.description = "Sade Pizza"
        self.cost = 8.0

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

class Zeytin(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 1.0
        self.description = "Zeytinli"

class Mantarlar(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 1.5
        self.description = "Mantarlı"

class KeciPeyniri(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 2.0
        self.description = "Keci Peynirli"

class Et(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 3.0
        self.description = "Kırmızı etli"

class Sogan(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 1.0
        self.description = "Soğanlı"

class Misir(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 1.5
        self.description = "Mısırlı"
class Customer:
    def __init__(self, name, surname, tc, credit_card):
        self.name = name
        self.surname = surname
        self.tc = tc
        self.credit_card = credit_card

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_tc(self):
        return self.tc

    def get_credit_card(self):
        return self.credit_card

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_tc(self, tc):
        self.tc = tc

    def set_credit_card(self, credit_card):
        self.credit_card = credit_card

    def __str__(self):
        return f"{self.name} {self.surname} - TC:{self.tc} - Credit Card: {self.credit_card}"


def print_menu():
    print("Lütfen Bir Pizza Tabanı Seçiniz:")
    print("1: Klasik")
    print("2: Margarita")
    print("3: TürkPizza")
    print("4: Sade Pizza")
    print("ve seçeceğiniz sos:")
    print("11: Zeytin")
    print("12: Mantarlar")
    print("13: Keçi Peyniri")
    print("14: Et")
    print("15: Soğan")
    print("16: Mısır")
    print("Teşekkür ederiz!")

    with open("menu.txt", "w") as f:
        f.write("Lütfen Bir Pizza Tabanı Seçiniz:\n")
        f.write("- Klasik\n")
        f.write("- Margherita\n")
        f.write("- TürkPizza\n")
        f.write("- Sade\n")
        f.write("\nve seçeceğiniz sos:\n")
        f.write("- Zeytin\n")
        f.write("- Mantarlar\n")
        f.write("- Keçi Peyniri\n")
        f.write("- Et\n")
        f.write("- Soğan\n")
        f.write("- Mısır\n")


def get_customer_info():
    name = input("Adınız: ")
    surname = input("Soyadınız: ")
    tc = input("TC Kimlik Numaranız: ")
    credit_card = input("Kredi Kartı Numaranız: ")
    return Customer(name, surname, tc, credit_card)

def main():
    print_menu()
    pizza_choice = input("Pizza tabanınızı seçiniz: ")
    pizza = None
    if pizza_choice == "1":
        pizza = ClassicPizza()
    elif pizza_choice == "2":
        pizza = MargheritaPizza()
    elif pizza_choice == "3":
        pizza = TurkishPizza()
    elif pizza_choice == "4":
        pizza = SadePizza()
    else:
        print("Geçersiz pizza seçimi.")

    if pizza is not None:
        topping_choices = []
        while True:
            topping_choice = input("Sos seçiniz veya bitirmek için 'q' giriniz: ")
            if topping_choice == "q":
                break
            elif topping_choice == "11":
                pizza = Zeytin(pizza)
            elif topping_choice == "12":
                pizza = Mantarlar(pizza)
            elif topping_choice == "13":
                pizza = KeciPeyniri(pizza)
            elif topping_choice == "14":
                pizza = Et(pizza)
            elif topping_choice == "15":
                pizza = Sogan(pizza)
            elif topping_choice == "16":
                pizza = Misir(pizza)
            else:
                print("Geçersiz sos seçimi.")
            topping_choices.append(topping_choice)

        print("Pizza özeti:")
        print(pizza.get_description())
        print("Toplam maliyet: $%.2f" % pizza.get_cost())

        
        customer = get_customer_info()
        print("Müşteri bilgileri:")
        print(customer)

      
        with open('orders.csv', mode='a', newline='') as orders_file:
            writer = csv.writer(orders_file)
            now = datetime.datetime.now()
            date_string = now.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([date_string, customer.get_name(), customer.get_surname(), customer.get_tc(), customer.get_credit_card(), pizza.get_description(), ", ".join(topping_choices), pizza.get_cost()])

if __name__ == '__main__':
    main()

