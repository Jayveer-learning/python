# You have Learning mind set before learning.

### Basic tips 

* So if you want master basic, intermidiate level and advanced level of classes you have to know only how class works. No need to know every things just you have basic knowledge keywords like what is init, what is self, attribute, attribute instance, instance/object Inheritance this keywords and topics methos are more than enogth for every one. 

* At this end no one work in one language so after working another language its have good chance you forget all advanced topics and methos so focus only basic and fundamental of any topics.

* Learn according to need ok. 


# Basic of Class

* Class is blueprint and instance make class functional this defination is not correct but as same time not wrong. 

* Don't focus on definations because we have lots of definations of google. focus on pratice and projects.

* Learn by doing best way to learn any thing

<br>

> Code explanations

``` python 
class Car_Company:
    # init -> initialize the class when new instance created according to attribute.
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

```

<br>

> this is basic structure or blueprint of class now this time is dive into deep in class 
<br>

### Basic definations of keywords that we use in this code

* __init__() -> is an constructer method that initilize the class when new instance/object created. 

* super() -> is used to class parent method and attribute in child class with __init__() same init initialize inherited attributes. 

* self -> is just a first parameter of class instant we can write another name like none etc. first parameter hold refrence of attribute. means help of self we can access any attribute instance inside class in any method.
> ex
``` python 
# example of first parameter 
    class none:
        def __init__(anything, otherattribute):
            pass
```

* meta -> Metaclass create Classes and Classes creates objects means instance of metaclass is classes and instance of class is object. (no need to know about this because this is advanced level topic ok i don't no why i am writing this but this is not important you can learn after master basic and intermiated level of classes.)
<br>
___
<br>

# Intermidate topics

### What is Inheritance

* Inheritance is a fundamental concept of OOP. Inheritance allow to create inherite perent methods and attribute in child class is also called (base class = parent, derived class = child) and inheritance is very important topics because help of this we can use parent code like methods, attributes, so its promotes code reuse, modularity, and a hierarchical class structure.

* Inheritance allow to create an class that inherite all methods and attributes from parent class 


### How many type of Inheritance in python

1. Single Inheritance: A child class inherits from one parentclass.

2. Multiple Inheritance: A child class inherits from more thanone parent class.

3. Multilevel Inheritance: A class is derived from a classwhich is also derived from another class.

4. Hierarchical Inheritance: Multiple classes inherit from asingle parent class.

5. Hybrid Inheritance: A combination of more than one type ofinheritance.
___
<br>


### Single Inheritance 

> code 

``` python
# Base/parent class

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


# Derived/child class 
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

```

In this code you Inherite from single parent and use basic of class and inheritance topic. 

#### Some rules 

right way and wrong way inilialize attributes 
> code 

``` python 
# right way 
super().__init__(company, model, launch)

# wrong way 
super().__init__(model, launch ,company)
# in this code model have company refrece because in parent class first attribute is company so when init initialize the instance/object so first value is company but in child firts attribute is model so this is don't give any error but give unexpected output. 

# wrong 
# model = company
# launch = model 
# company = launch 

# right 
# company = company 
# model = model 
# launch = launch 

```

include derived attribute in child class init method so child class initialize the instance/objects according attribute. 
> code 
``` python 

class Price(Car_Company):
    def __init__(self, company, model, price):
        # Initialize the parent class
        super().__init__(company, model)
        self.car_price = price # new attribute for price

# first pass derives attributes then new attributes ok in child __init__() method is basic rull if you can't pass first derived attributes.if you don't follow this rule it's not mean give any error but this is basic practice so you have follow.

```

