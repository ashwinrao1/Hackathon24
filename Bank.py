savingsAPR = 1+ 0.05
savingsBalance = 0
checkingBalance = 0
checkingPercent = 50
savingsPercent = 1-checkingPercent
savingsHistory  = []
checkingHistory  = []

def setCheckingBalance(balance):
    global checkingBalance
    checkingBalance = balance
def getCheckingBalance():

    return checkingBalance
def setSavingsBalance(balance):
    global savingsBalance
    savingsBalance = balance
def getSavingsBalance():
    return savingsBalance

def changeSavings(money, reason):
    global savingsBalance
    savingsBalance = savingsBalance+ money
    savingsHistory.append(reason)
    savingsHistory.append(money)

def changeChecking(money, reason):
    global checkingBalance
    checkingBalance +=money
    checkingHistory.append(reason)
    checkingHistory.append(money)
def compoundSavings():
    global savingsBalance
    savingsBalance = getSavingsBalance()
    savingsBalance *= savingsAPR

def checkingToSaving(money):
    changeSavings(money, "Transfer")
    changeChecking(-money, "Transfer")
def savingToChecking(money):
    changeSavings(-money, "Transfer")
    changeChecking(money, "Transfer")

def setSettings(sPercent):
    global savingsPercent
    global checkingPercent
    savingsPercent = sPercent
    checkingPercent = 1-sPercent

def addToAccount(money, reason):
    changeSavings(money*savingsPercent, reason)
    changeChecking(money*checkingPercent, reason)
def addToAccountNOLOG(money):
    print("here")
    global savingsBalance
    global checkingBalance
    savingsBalance+=money*savingsPercent
    checkingBalance += money * (1-savingsPercent)
def init():
    setCheckingBalance(100)
    setSavingsBalance(100)
    setSettings(0.10)
    addToAccount(100, "Just cuz")
    print(getCheckingBalance(), getSavingsBalance())
init()