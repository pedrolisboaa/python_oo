class Employee:
    def __init__(self, name, gross_salary, tax):
        self._name = name
        self._gross_salary = gross_salary
        self._tax = tax

    @property
    def name(self):
        return self._name

    @property
    def gross_salary(self):
        return self._gross_salary

    @property
    def tax(self):
        return self.tax

    @name.setter
    def name(self, name):
        self._name = name

    @gross_salary.setter
    def gross_salary(self, gross_salary):
        self._gross_salary = gross_salary

    @tax.setter
    def tax(self, tax):
        self._tax = tax

    def net_salary(self):
        return self._gross_salary - self._tax

    def increase_salary(self, percentage):
        self._gross_salary += (self._gross_salary * percentage / 100)

    def update(self):
        return f'{self._name}, $ {Employee.net_salary(self)}'
