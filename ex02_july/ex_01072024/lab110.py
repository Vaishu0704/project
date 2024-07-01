#Single inheritance
class grandparent:
    key='abc@123'
    def grandparent_method(self):
        return 'Grandparent method'

class father(grandparent):
    def father_method(self):
        return 'Father method'


parent=father()
print(parent.father_method())
print(parent.grandparent_method())
print(parent.key)