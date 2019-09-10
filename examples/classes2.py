import datetime

class Employee:
    """ Controls the wage of any employee """

    def __init__(self, name, fixed_salary):
        """ constructor - executing when creating a new Employee object

        :param name : name of the Employee
        :param fixed_salary : the monthly fixed salary
        """
        self._name = name
        self._fixed_salary = fixed_salary
        print("Employee %s created" % name)

    def get_fixed_salary(self):
        return self._fixed_salary

    def raise_salary(self, percentage):
        """ gives a raise

        :param percentage: the percentage the fixed salary is to be raised
        :return:
        """
        self._fixed_salary = self._fixed_salary * (1 + percentage / 100)
        print("Fixed salary raised to %.2f " % self._fixed_salary)


class Member(Employee):

    def __init__(self, yearly_membership_fee, date_paid_str, **kwargs):
        """ Creates an employee that is also a member

        :param yearly_membership_fee: the membership fee paid
        :param date_paid_str: the date this membership was paid in "YYYYMMDD"-format
        :param kwargs: keyword arguments like name and fixed_salary
                to create the employee
        """
        self._yearly_membership_fee = yearly_membership_fee
        self._date_paid = datetime.datetime.strptime(date_paid_str, "%Y%m%d")
        super(Member, self).__init__(**kwargs)

    def get_fixed_salary(self):
        result = super().get_fixed_salary()
        if datetime.datetime.now() - datetime.timedelta(days=365) < self._date_paid:
            result += self._yearly_membership_fee/12
        return result


class Manager(Member):
    """ Controls the wage of a manager """

    def __init__(self, name, fixed_salary, variable_salary):
        """ constructor - executing when creating a new Manager object

        :param name : name of the Manager
        :param fixed_salary : the monthly fixed salary
        :param variable_salary : the montly variable salary at 100%
        """
        super(Manager, self).__init__( yearly_membership_fee=2400,
                                       date_paid_str=datetime.datetime.now().strftime("%Y%m%d"),
                                       name=name, fixed_salary=fixed_salary)
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
jeff = Member(yearly_membership_fee=1200, date_paid_str="20190701",
                name="Jeff", fixed_salary=1800)

print ("John receives", john.get_fixed_salary())
print("Jeff receives", jeff.get_fixed_salary())

mary = Manager("Mary", 1500, 1000)

print ("Mary receives", mary.get_fixed_salary(), "as fixed salary")


"""Output

Employee John created
Employee Jeff created
John receives 1555
Jeff receives 1900.0
Employee Mary created
Mary receives 1700.0 as fixed salary
"""
