class Person(object):
    def __init__(self, name, birth, gender, legitimacy="Trueborn"):
        self.birth = birth
        self.name = name
        self.gender = gender
        self.legitimacy = legitimacy
        self.children = []

    def __repr__(self):
        return f"{self.name}"

    def age(self, year):
        return year - self.birth

    def legitimacy(self):
        return self.legitmacy