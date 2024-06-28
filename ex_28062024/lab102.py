#web automation in selenium
#page-you are going to automate

class vwologinpage:
    email=None
    password=None

    def __init__(self,email,password):
        self.email=email
        self.password=password

    def login_confirm(self):
        if self.password=='Pass123':
            print('Allowed to enter')
        else:
            print('Not allowed')

#end of the class
amit=vwologinpage('amit@gmail.com','123')
amit.login_confirm()
sriram=vwologinpage('sriramcivil92@gmail.com','Pass123')
sriram.login_confirm()