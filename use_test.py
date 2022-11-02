from test import Pet
from stan import Yes


def megamain():
    animals = []
    animals1 = [animals] 
    animals2 = [animals1 ,animals]
    name = str

    t = 0
    while  t<1 :
        
    
        name = input("input pet name")
        age = (input("pet age") + ':')
        pet = Pet({'name': name, 'age': age})


        a = []
        w = 0
        r = 0
        while w<1:
                                            
                
            animal_type1 = input ('type' )
            name1 = input("input pet name") 
            age1 = input("pet age") 
            cost1 = input("cost")
            yes = Yes({'name': (name1 + '32'), 'type': animal_type1, 'age': age1 })
            print(w)
            print(a)
            w = w+1
            animals1.extend(animal_type1)
            animals1.extend(name1)
            animals1.extend(age1)
            animals1.extend(cost1)
        

    

        w = 0

        animals2
        with open('readme.txt', 'a') as f:
                    f.write(str(animals1))
                    f.writelines("/  \n".format(animals))
                    animals1.clear()
                    animals.clear()
    
        
    
        print("general patient info", pet.get_name())   
        continue1 = input("would you like to Continue? or quit") 
        for letter in continue1:
            if letter in "n,N,q,Q":
                t = t +1
                
                
           

            
    
    
        
megamain()




    
