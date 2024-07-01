class vwologin:
    def __init__(self,email,password,name):
        self.__email=email
        self.__password=password
        self.name=name

    def login_confirm(self):
        if self.__email=='abc@gmail.com' and self.__password=='123':
            print('Allowed')
        else:
            print('Not allowed')

#end of class
page1=vwologin('abc@gmail.com','123','Vaishnavi')
print(page1.name)
page1.login_confirm()
page2=vwologin('abc@gmail.com','345','Sriram')
print(page2.name)
page2.login_confirm()
