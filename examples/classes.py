class Employee:
    years_worked = 0;

    def __init__(self, fixed_salary, variable_salary):
        """
        constructor - executing when creating a new Employee object

        :param fixed_salary : the monthly fixed salary
        :param variable_salary : the montly variable salary at 100%
        """
        self.fixed_salary = fixed_salary
        self.variable_alary = variable_salary

    def raise(self, percentage, type):
        """
        gives a raise

        :param percentage: the percentage the salary is to be raised
        :param type: should be
        :return:
        """
