import pprint

class employee:

    def __init__(self, uuid, date, firstname, lastname, email):
        self.uuid = uuid
        self.date = date
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __str__(self):
        return f"UUID: {self.uuid} Birthdate: {self.date} Name: {self.firstname} {self.lastname} Email: {self.email}"



def loadData():
    f = open("employees.csv", "r")
    lines = f.readlines()
    f.close()
    employees = []
    for line in lines:
        tokens = line.strip().split(",")
        e = employee(tokens[0], tokens[1], tokens[2], tokens[3], tokens[4])
        employees.append(e)
    return employees

employees = loadData()

employeeStrings = [str(e) for e in employees]

uuids = set([e.uuid for e in employees])
dates = set([e.date for e in employees])
firstNames = set([e.firstname for e in employees])
lastNames = set([e.lastname for e in employees])
emails = set([e.email for e in employees])

pprint.pprint(employeeStrings)

