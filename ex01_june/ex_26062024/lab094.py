class Person:

    #Attributes
    name=None
    id=None
    age=None
    phone_number=None
    #Behaviour
    def talk(self): #no arg no return
        print('I can talk')
    def another(self):
        print('I am a method')
    def sleep(self,name):  #1 arg with no return
        print('I am a method')
        print('Sleep',name)
    def sleep2(self,name):  #1arg with return
        print('I am a method!!')
        return None
    def walk(self):
        print('I am walking')

    def walk_return(self):  #no arg with return
        return 'I am walking'

#Create object of the person class
#objectRef=object-->class name()

vaishnavi=Person()
vaishnavi.name='Vaishnavi Giri'
vaishnavi.id=8042
vaishnavi.age=29
vaishnavi.phone_number=915090000
print(vaishnavi.name,vaishnavi.id,vaishnavi.age,vaishnavi.phone_number)
vaishnavi.talk()
vaishnavi.another()
vaishnavi.sleep('vaishnavi')
vaishnavi.sleep2('vaishnavi')
vaishnavi.walk()
vaishnavi.walk_return()

sriram=Person()
sriram.name='Sriram Somasundaram'
sriram.id=8029
sriram.age=32
sriram.phone_number=910090000
print(sriram.name,sriram.id,sriram.age,sriram.phone_number)
sriram.talk()
sriram.another()
sriram.sleep('sriram')
sriram.sleep2('sriram')
sriram.walk()
sriram.walk_return()