class Employee:
    """ Controls the wage of any employee """

    def __init__(self, name, fixed_salary):
        """ constructor - executing when creating a new Employee object

        :param name : name of the Employee
        :param fixed_salary : the monthly fixed salary
        """
        self.name = name
        self.fixed_salary = fixed_salary
        print("Employee %s created" % name)

    def raise_salary(self, percentage):
        """ gives a raise

        :param percentage: the percentage the fixed salary is to be raised
        :return:
        """
        self.fixed_salary = self.fixed_salary * (1 + percentage/100)
        print("Fixed salary raised to %.2f " % self.fixed_salary)


class Manager(Employee):
    """ Controls the wage of a manager """

    def __init__(self, name, fixed_salary, variable_salary):
        """ constructor - executing when creating a new Manager object

        :param name : name of the Manager
        :param fixed_salary : the monthly fixed salary
        :param variable_salary : the montly variable salary at 100%
        """
        super(Manager, self).__init__(name, fixed_salary)
        self.variable_salary = variable_salary

    def raise_salary(self, percentage, type):
        """ gives a rise for a manager

        :param percentage:
        :param type: string that indicates type of salary: "FIXED" or "VARIABLE"
        :return:
        """
        if type == "VARIABLE":
            self.variable_salary = self.variable_salary * (1 + percentage/100)
            print ("Variable salary raised to %.2f " % self.variable_salary)
        elif type == "FIXED":
            super(Manager, self).raise_salary(percentage)
        else:
            print ("%s is wrong salary type, must be VARIABLE or FIXED" % type)


john = Employee("John", 1555)
jeff = Employee("Jeff", 1800)
mary = Manager("Mary", 1500, 1000)

john.raise_salary(25)
jeff.raise_salary(15)
mary.raise_salary(10, "FIXED")
mary.raise_salary(30, "VARIABLE")
mary.raise_salary(30, "SUPER")

"""Output

Employee John created
Employee Jeff created
Employee Mary created
Fixed salary raised to 1943.75 
Fixed salary raised to 2070.00 
Fixed salary raised to 1650.00 
Variable salary raised to 1300.00 
SUPER is wrong salary type, must be VARIABLE or FIXED
"""
