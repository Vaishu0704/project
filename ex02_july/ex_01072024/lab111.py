class parent:
    gold='2kg'
    def bhk2(self):
        print('2 BHK')

class child(parent):
    def bhk3(self):
        print('3 BHK')
child_obj=child()
child_obj.bhk3()
child_obj.bhk2()
print(child_obj.gold)

#father=parent()
#father.bhk3() #it is not callable