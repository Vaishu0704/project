#Multilevel inheritance
#GF-F-Son
class Grandparent:
    key_gold='1 kg'
    def grandparent_method(self):
        return 'Grandparent method'

class Parent(Grandparent):
    def parent_method(self):
        return 'Parent method'

class Child(Parent):
    def child_method(self):
        return 'Child method'

child=Child()
print(child.child_method())
print(child.parent_method())
print(child.grandparent_method())
print(child.key_gold)

parent=Parent()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key_gold)

grandparent=Grandparent()
print(grandparent.grandparent_method())
print(grandparent.key_gold)