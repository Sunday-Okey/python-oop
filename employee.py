from datetime import datetime


class Employee:
    company = 'Sapkowsk, Inc.'

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def birth_date(self):
        return self._birthdate

    @birth_date.setter
    def birth_date(self, value):
        self._birthdate = datetime.fromisoformat(value)

    def compute_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        birthday = datetime(
            today.year, self.birth_date.month, self.birth_date.day)
        if today < birthday:
            return age - 1
        return age

    @classmethod
    def from_dict(cls, data):
        # using ** on a dictionary turns it argurments for the class,
        return cls(**data)
    # Each key value pair in the dictionary is used as a named argument to the constructor

    def __str__(self):
        return f"{self.name} is {self.compute_age()} years old"

    def __repr__(self):
        return (
            "Employee("
            f"""name="{self.name}", """
            f"""birth_date="{self.birth_date.strftime('%Y-%m-%d')}")"""
        )


print(Employee.company)
geralt = Employee("Geralt of Rivia", '1986-12-01')
