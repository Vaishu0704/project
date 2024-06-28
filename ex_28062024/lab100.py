class person:
    #class variables/instance variables
    name=None
    age=None
    def walk(self):
        a=10
        print('I am a method')
        print('Hi',self.age)

amit=person()
amit.walk()