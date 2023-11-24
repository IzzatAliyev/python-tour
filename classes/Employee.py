class Person:
    def __init__(self, fname, lname):
        self.__fname = fname
        self.__lname = lname

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, lname):
        self.__lname = lname
        
    def getInfo(self):
        print("First Name : ", self.fname, "Last Name : ", self.lname)


class Employee(Person):
    
    def __init__(self, fname, lname, lohn):
        super().__init__(fname, lname)
        self.__lohn = lohn
        
    @property
    def lohn(self):
        return self.__lohn
    
    @lohn.setter
    def lohn(self, lohn):
        self.__lohn = lohn

    def work(self):
        print('Employee is working')
        
    def getInfo(self):
        print("First Name : ", self.fname, "Last Name : ", self.lname, "Lohn : ", self.lohn)


person1 = Employee('kiril', 'onacki', 20_000)
person1.fname = 'kiri'
person1.lname = 'ona'
person1.lohn = 15_000
print(person1.fname)
print(person1.lname)
print(person1.lohn)
person1.work()
person1.getInfo()
