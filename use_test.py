
import test

from test import test_func1 #Only import the function directly into current namespace

 #Exception (NameError)

from test import *



def megamain():
    print(test_func1)

    animals1 = []
    name = str
    animals = [animals1]   
    while True:

        class Pet:
            
            def __init__(self, options):
                self._name = options
                self._animal_type = options
                self._age = options

            def set_name(self, new_name):
                self._name = new_name

            def set_animal_type(self, new_type):
                self._animal_type = new_type

            def set_age(self, new_age):
                self._age = new_age

            def get_name(self):
                return self._name

            def get_animal_type(self):
                return self._animal_type

            def get_age(self):
                return self._age

        animal_type = input("input pet type")
        name = input("input pet name")
        age = input("pet age")

        pet = Pet({'name': name, 'type': animal_type, 'age': age})

        animals.append(animal_type)
        print (animals1)
        a = []
        w = 0
        r = 0

        while w<3:
                                            
            class Yes:
                
                def __init__(self1, options1):
                    self1._name1 = options1
                    self1._animal1_type1 = options1
                    self1._age1 = options1
                    self1._cost1 = options1

                def set_name(self1, new_name1):
                    self1._name1 = new_name1

                def set_animal_type(self1, new_type1):
                    self1._animal_type1 = new_type1

                def set_age(self1, new_age1):
                    self1._age1 = new_age1
                    
                def set_cost(self1,new_price1):
                    self1._new1=new_price1

                def get_name(self1):
                    return self1._name1

                def get_animal_type(self1):
                    return self1._animal_type1

                def get_age(self1):
                    return self1._age1

                def get_cost(self1):
                    return self1._cost1        

            animal_type1 = input("input pet type")
            name1 = input("input pet name")
            age1 = input("pet age")
            cost1 = input("cost")

            yes = Yes({'name': name1, 'type': animal_type1, 'age': age1 })

            print(w)
            print(a)
            w = w+1

            animals1.extend(animal_type1)

        searchname = input('search name, or quit')  
        if searchname == name:
            print(animals)
            continue1 = input("would you like to Continue?") 
            if continue1 == "quit":
                        quit("quit")

        if searchname == ("quit","Quit"):
                        quit("quit")
            
        w = 0
            #import from another file
        print(myvar)
        test.test_func()
        
megamain()
    