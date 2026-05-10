from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def show_info(self):
        pass

    @abstractmethod
    def get_factor(self):
        pass

class Teacher(Employee):

    def __init__(self, name: str, basic_salary: float):
        self.__name = name
        self.__basic_salary = basic_salary

    def get_salary(self):
        return self.__basic_salary

    def show_info(self):
        print("Teacher Name :", self.__name)
        print("Basic Salary :", self.__basic_salary)

    def get_factor(self):
        return 1

class PhdTeacher(Teacher):

    def get_salary(self):
        return super().get_salary() + 10000

    def get_factor(self):
        return 1.5

    def show_info(self):
        super().show_info()
        print("Teacher Type : PhD")

class NonPhdTeacher(Teacher):

    def get_salary(self):
        return super().get_salary()

    def get_factor(self):
        return 1

    def show_info(self):
        super().show_info()
        print("Teacher Type : Non-PhD")

# Base Decorator
class ExtraDuties(Employee):

    def __init__(self, employee: Employee):
        self.employee = employee

    def get_salary(self):
        return self.employee.get_salary()

    def get_factor(self):
        return self.employee.get_factor()

    def show_info(self):
        self.employee.show_info()

class HallProvost(ExtraDuties):

    def get_salary(self):
        extra_amount = 5000 * self.employee.get_factor()
        return super().get_salary() + extra_amount

    def show_info(self):
        self.employee.show_info()
        print("Extra Duty : Hall Provost")

class Chairman(ExtraDuties):

    def get_salary(self):
        extra_amount = 7000 * self.employee.get_factor()
        return super().get_salary() + extra_amount

    def show_info(self):
        self.employee.show_info()
        print("Extra Duty : Chairman")

class StudentAdvisor(ExtraDuties):

    def get_salary(self):
        extra_amount = 3000 * self.employee.get_factor()
        return super().get_salary() + extra_amount

    def show_info(self):
        self.employee.show_info()
        print("Extra Duty : Student Advisor")


phd_teacher = PhdTeacher("Rahim", 50000)
phd_teacher = HallProvost(phd_teacher)
phd_teacher = Chairman(phd_teacher)
phd_teacher = StudentAdvisor(phd_teacher)
phd_teacher.show_info()
print("Total Salary :", phd_teacher.get_salary())

print("---------------------")

nonphd_teacher = NonPhdTeacher("Karim", 50000)
nonphd_teacher = HallProvost(nonphd_teacher)
nonphd_teacher = Chairman(nonphd_teacher)
nonphd_teacher.show_info()
print("Total Salary :", nonphd_teacher.get_salary())