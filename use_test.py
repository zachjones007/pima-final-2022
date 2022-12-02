from test import p
from stan import Yes

global animals, animals1 , animals2
def megamain():
    animals = []
    animals1 = [animals] 
    animals2 = [animals1 ,animals]
    name = str

    t = 0
    while  t<1 :
        
        

        p.set_age(float(input("Enter the age: ")))
        p.set_name(input("Enter the name: "))
        @property
        def get_age(self):
            return self._age + animals2
      
   
        @property
        def get_name(self):
            return self._name + animals2

        
        
            

        
        

        a = []
        w = 0
        r = 0
        while w<1:
                                            
                
            animal_type1 = input ('surgey type' )
            name1 = input("input surgeon name") 
            age1 = input("procedure date") 
            cost1 = input("cost")
            y = Yes({'procedure name': (name1 ), 'cost': animal_type1, 'date': age1 })
            print(w)
            print(a)
            w = w+1
            # setter shoud
           
            animals.extend(cost1 + age1 + name1 + animal_type1)
            

    

        w = 0

        animals2
        with open('readme.txt', 'a') as f:
                    f.write(str(animals1))
                    f.writelines("/  \n".format(animals))
                    animals1.clear()
                    animals.clear()
    
        
    
       # print("the pets age is: ",p.get_age())
        print("the pets name is: ",y.get_name())    
        continue1 = input("would you like to Continue? or quit") 
        for letter in continue1:
            if letter in "n,N,q,Q":
                t = t +1
                
                
           

            
    
    
        
megamain()




    
