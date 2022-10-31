from test import Pet
from stan import Yes

def megamain():
    animals = []
    animals1 = [animals] 
    animals2 = [animals1 ,animals]
    name = str
      
    while True:

        

        animal_type = input("input pet type")
        name = input("input pet name")
        age = (input("pet age") + ':')

        pet = Pet({'name': name, 'type': animal_type, 'age': age})

        animals.append(animal_type)
        print (animals1)
        a = []
        w = 0
        r = 0

        while w<3:
                                            
                   

            animal_type1 = input ('type' + ("input pet type"))
            name1 = input("input pet name") + '2'
            age1 = input("pet age") + '5'
            cost1 = input("cost") + '9'

            yes = Yes({'name': (name1 + '32'), 'type': animal_type1, 'age': age1 })

            print(w)
            print(a)
            w = w+1

            animals1.extend(animal_type1)
            animals1.extend(name1)
            animals1.extend(age1)
        
        searchname = input('search name, or quit')  
        if searchname == name:
            print(animals)
            continue1 = input("would you like to Continue? or quit") 
                         
        w = 0
        animals2
        with open('readme.txt', 'w') as f:
                for line in animals1:
                    f.writelines(line)
            
        for letter in continue1:
                if letter in "n,N,q,Q":
                    quit("quittting")
                     #import from another file
                         
megamain()
