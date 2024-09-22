import Bank
salary = 0
clickSalary = 0

def setClickSalary(s):
    global clickSalary
    clickSalary = s
def getClickSalary():
    return clickSalary

def setSalary(s):
    global salary
    salary = s
def getSalary():
    return salary

def increaseSalary():
    salary*=1.1

def clicked():
    Bank.addToAccountNOLOG(clickSalary)


