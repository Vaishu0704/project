class password:
    def __init__(self,password):
        self.__password=password
        self.public_var=10

    def get_password(self,is_auth):
        if is_auth:
            print(self.__password)
        else:
            print('Invalid password')

    def set_password(self,password):
        if len(password)>10:
            if password.endswith('i'):
                self.__password=password
                print('set to allow',self.__password)
        else:
                print('Not allowed,wrong password')

pwd=password('Hacker123')
pwd.get_password(True)
pwd.set_password('read12345i') #length of pwd=10
pwd.set_password('Read123456i')#pwd length>10
pwd.set_password('read123456i')#pwd length>10


