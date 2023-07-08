#Common Class:
class Users:
    def __init__(self,email,password) -> None:
        self.email = email
        self.__password = password

#User Class: Inherited Common class
class User(Users):
    def __init__(self, name, email, password, amount) -> None:
        self.name = name
        self.__total_amount = amount
        super().__init__(email, password)

    @property
    def totalTaka(self):
        return self.__total_amount
    
    def deposit(self,amount):
        self.__total_amount += amount
    def minus(self,amount):
        self.__total_amount -= amount

    def withdrawal(self,amount):
        if amount<= self.__total_amount:
            print('Please wait Your tranjection is processing...')
            self.__total_amount -= amount
            print(f'Your Total Balance Now {self.__total_amount} Taka')
            return amount
        else:
            print('Sorry You Do Not Have The Money...')

    #Printing A User:
    def __repr__(self) -> str:
        print(f'Name:{self.name}|Email:{self.email}|Total Amount:{self.__total_amount}')
        return ''

#Admin class : Inherited Common Class
class Admin(Users):
    def __init__(self, name, email, password) -> None:
        self.name = name
        super().__init__(email, password)


#Bank class:
class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.__BankAmount = 0
        self.__loan = 0
        self.loanAccess = True
        self.user = []
        self.admin = []

    def add_User(self,man):
        self.user.append(man)
        self.__BankAmount += man.totalTaka

    def BankBalance(self,man):
        if man in self.admin:
            return self.__BankAmount
        else:
            print('Ethical Issue...')
        
    def loanAmount(self,man):
        if man in self.admin:
            return self.__loan
        else:
            print('Ethical Issue...')

    def add_admin(self,man):
        self.admin.append(man)

    def transferAmount(self,fromAC,ToAC,amount):
        if  fromAC in self.user and ToAC in self.user:
            if fromAC.totalTaka >= amount:
                ToAC.deposit(amount)
                fromAC.minus(amount)
                print(f'Tranjection Complete From {fromAC.name} To {ToAC.name}...')
                print(f'Now the amount of {fromAC.name} is {fromAC.totalTaka} taka and {ToAC.name} is {ToAC.totalTaka} taka')


    def getLoan(self,person,amount):
        if amount <= person.totalTaka*2 and self.loanAccess:
            self.__loan += amount
            self.__BankAmount -= amount
            print(f'{person.name} You got a loan {amount} taka now your corrent amount is: {person.totalTaka} taka')
        else:
            ('SORRY bank er obostha valona...')

    def BankObostha(self,man):
        if man in self.admin:
            if self.__BankAmount <= 500:
                self.loanAccess = False
            else:
                self.loanAccess = True


    def __repr__(self) -> str:
        print(f'-------{self.name}-------')
        print('There are the user :')
        i = 0
        for value in self.user:
            i += 1
            print(f'{i}.Name: {value.name}|Email: {value.email}')

        print('There are the Admin :')
        j = 0
        for value in self.admin:
            j += 1
            print(f'{j}.Name: {value.name}|Email: {value.email}')
        return ''






#First Trial Account:
Islamik_Bank = Bank('Islamik Bank LTD.')

sifat = User('sifat','sifat@ene','ssss',5000)
Islamik_Bank.add_User(sifat)

safed = User('safed','safed@ene','ffff',2000)
Islamik_Bank.add_User(safed)

Islamik_Bank.transferAmount(sifat,safed,1000)

Islamik_Bank.getLoan(sifat,3000)
Islamik_Bank.getLoan(sifat,3500)

Mr_Alam = Admin('Mr. Alam','alam@aaa','aaaaaa')
Islamik_Bank.add_admin(Mr_Alam)
Mr_Jolil = Admin('Mr. Jolil','jolil@jjj','jjjjj')
Islamik_Bank.add_admin(Mr_Jolil)

print(Islamik_Bank.BankBalance(Mr_Alam))
print(Islamik_Bank.loanAmount(Mr_Jolil))
Islamik_Bank.BankObostha(Mr_Jolil)
Islamik_Bank.getLoan(sifat,3500)

print(Islamik_Bank)