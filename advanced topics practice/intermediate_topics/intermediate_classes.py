
class Car_Company: 
    def __init__(self, company:str= None, model: str=None, launch: str = '00:00:2024'):
        # attribute instance, attribute = variable
        # self hold refrence of perticulater instance data 
        self.company_name = company
        self.car_model = model 
        self.date_launch = launch

    def show_detail(self, company_owner_name: str='Jayveer') -> str: # -> this indicate show_detail only 
        # return string deta this help for reading code. what happen when anyone but int value nothig work 
        # normaly :str indicate ths function assum user give input string value
        return f"car company {self.company_name}, model {self.car_model}, launch data {self.date_launch} and company owner name {company_owner_name}"


# instance/object of class
car_one = Car_Company(company="Tesla", model="Model S").show_detail()
print(car_one)

# outpu :- car company Tesla, model Model S, launch data 00:00:2024 and company owner name Jayveer


# intermiates topics

class Price(Car_Company):
    def __init__(self, company, model, price):
        # Initialize the parent class
        super().__init__(company, model)
        self.car_price = price # new attribute for price

    def price_detail_model(self):
        return f'Car company {self.company_name} model of car {self.car_model} price ${self.car_price}'

# Instance/object of Price class
car_price = Price(company='tesla', model='Model S', price=100000)
print(car_price.price_detail_model())

# output :- Car company tesla model of car Model S price $100000
