class Teacher:
    def __init__(self) -> None:
        self.user = []

class person:
    def __init__(self,name) -> None:
        self.name = name

t1 = Teacher()
sifat = person('Sifat')
rifat = person('Rifat')

t1.user.append(sifat)
t1.user.append(rifat)

for value in t1.user:
    if 'Sifat' in value.name:
        print('Yea')