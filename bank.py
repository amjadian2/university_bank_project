# university group project
#مصطفی احمدی
#محمدرضا امجدیان
#سید مهدی الیاسی
#زهرا طالبی مقدم
#ساغر حسن پور
#مبینا رازقی مقدم
import uuid
import random

def splitAtIntervals(r,s,txt):
    my_text = txt[0]
    for i in range(1,len(txt)):
        if i%r == 0 : my_text += str(s)
        my_text += str(txt[i])
    return str(my_text)


def heapify(arr,acc, n, i):
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2   
 
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        acc[i], acc[largest] = acc[largest], acc[i]
        heapify(arr,acc, n, largest)
 

def heapSort(arr,acc):
    n = len(arr)
 
    for i in range(n//2 - 1, -1, -1):
        heapify(arr,acc, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        acc[i], acc[0] = acc[0], acc[i] 
        heapify(arr,acc, i, 0)

 


class Account:
    # _id : str ,first/last_name : str, date : (yy : int,mm : int,dd : int) 
    def __init__(self,first_name,last_name,date_created,initial_balance):
        self.id = splitAtIntervals(4,'-',str(uuid.uuid4().int)[:16])
        self.first_name = first_name
        self.last_name = last_name
        self.date_created = date_created
        self.date_created_str = str(date_created[0])+'/'+str(date_created[1])+'/'+str(date_created[2])
        self.balance = initial_balance

    def print(self):
        print("first name : {} last name : {} date created : {} id : {} balance : {}".format(self.first_name,self.last_name,self.date_created_str,self.id,self.balance))


    def increace_balance(self,f):
        if f > 0 :
            self.balance += f
    
    def decrease_balance(self,f):
        if f > 0 :
            self.balance -= f




class Bank:
    def __init__(self):
        self.accounts = {}

                
                

    def save(self):
        with open('bank.txt', 'w') as file:
            for a,i in self.accounts.items():
                file.write(i.first_name+","+i.last_name+","+i.date_created_str+","+i.id+","+str(i.balance)+";")

    def addAccount(self,first_name,last_name,date_created,balance):
        acc = Account(first_name,last_name,date_created,balance)
        self.accounts[acc.id] = acc
        # acc.print()
        # print("the id assigned to the account is "+acc.id)

    def changeFirstName(self,ID,name):
        self.accounts[ID].first_name = name
    def changeLastName(self,ID,name):
        self.accounts[ID].last_name = name
    def changeDate(self,ID,date):
        self.accounts[ID].date_created_str = date
        self.accounts[ID].date_created = date.split("/")
    def changeBalance(self,ID,balance):
        self.accounts[ID].balance = int(balance)

    def removeAccount(self,ID):
        self.accounts.pop(ID)

    def viewAccounts(self):
        # print("done")
        for i,acc in self.accounts.items() : 
            acc.print()

    def sortAccountsByDateAndView(self):
        accs = []
        arr = []
        for i,a in self.accounts.items():
            accs.append(a)
            arr.append(a.date_created[0])
        heapSort(arr,accs)
        for i in accs:
            i.print()
        
    def sortAccountsByBalance(self):
        accs = []
        arr = []
        for i,a in self.accounts.items():
            accs.append(a)
            arr.append(a.balance)
        heapSort(arr,accs)
        for i in accs:
            i.print()


    def getAccountById(self,ID):
        return self.accounts[ID]

    def transfer(self,id1,id2,f):
        if id1 in self.accounts and id2 in self.accounts :
            ac1 = self.accounts[id1]
            ac2 = self.accounts[id2]
            a1 =  int(ac1.balance) - f
            a2 =  int(ac2.balance) + f
            if a1 < 0 :
                print('not enough money !')
            ac1.balance = str(a1)
            ac2.balance = str(a2)
        else:
            print("no such account.")
Q = 0
case = [None for i in range(10)]




def createAccount(bank):
    first_name = input("enter the first name for this account : ")
    last_name = input("enter the last name for this account : ")
    date_created = input("at what date was the account created? : (format : yyyy/mm/dd)")
    initial_balance = input("what is the initial balance : ")
    
    try : 
        splited_date = date_created.split('/')
    except :
        splited_date = False
    while int(splited_date[1]) > 12 or int(splited_date[2]) > 31 :
        print("invalid date !")
        date_created = input("at what date was the account created? : (format : yyyy/mm/dd)")
        splited_date = date_created.split('/')

    while len(splited_date[0]) != 4 or len(splited_date[1]) != 2 or len(splited_date[2]) != 2 or not splited_date :
        print("invalid date format !")
        date_created = input("at what date was the account created? : (format : yyyy/mm/dd)")
        splited_date = date_created.split('/')


    bank.addAccount(first_name,last_name,splited_date,initial_balance)
case[0] = createAccount

def transfer(bank):
    account_send = input("enter the sender's id : ")
    account_recieve = input("enter the recievers's id : ")
    amount = input("how much balance do you wish to transfer : ")
    bank.transfer(account_send,account_recieve,float(amount))
case[1]=transfer

def editAccount(bank):
    ID = input("enter the id of the account you wish to edit : ")
    account_to_edit = bank.getAccountById(ID)
    field_to_change = input("what do you wish to change? : ")
    if field_to_change == "first name" :
        bank.changeFirstName(ID,input("enter the new value : "))
    elif field_to_change == "last name" :
        bank.changeLastName(ID,input("enter the new value : "))
    elif field_to_change == "date" :
        bank.cangeDate(ID,input("enter the new value (yyyy/mm/dd) : "))
    elif field_to_change == "balance" :
        bank.changeBalance(ID,input("enter the new value : "))
case[2] = editAccount

def removeAccount(bank):
    account_to_delete = input("enter the id of the account you wish to remove : ")
    bank.removeAccount(account_to_delete)
case[3] = removeAccount

def viewAccounts(bank):
    bank.viewAccounts()

case[4] = viewAccounts

def sortAccountsByDate(bank):
    bank.sortAccountsByDateAndView()

case[5] = sortAccountsByDate

def sortAccountsByBalance(bank):
    bank.sortAccountsByBalance()

case[6] = sortAccountsByBalance


def accountsFromFile(adrs):
    l = {}
    with open(adrs, 'r') as file:
        s = str(file.read())
        lls = s.split(";")
        for i in range(len(lls)-1):
            lls[i] = lls[i].split(",")
            #print(lls)
            a = Account(lls[i][0],lls[i][1],lls[i][2].split("/"),lls[i][4])
            a.id = lls[i][3]
            l[a.id] = a 
    return l



def main(case):
    bank = Bank()
    bank.accounts = accountsFromFile('bank.txt')

    while not Q :
        print("\n\n================================")
        print("to create a new account press 1")
        print("to transfer between two accounts press 2")
        print("to edit an existing account press 3")
        print("to remove existing account press 4")
        print("to view existing accounts press 5")
        print("to view existing accounts sorted by year created press 6")
        print("to view existing accounts sorted by balance press 7")
        print("to quit press q")
        user_chice = input("what do you wish to do ? ")
        print("\n\n================================")
        if user_chice == "q" : break
        case[int(user_chice)-1](bank)

    bank.save()
		










main(case)





    # bank.addAccount('ali','mohammadi',(1400,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1401,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1406,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1401,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1391,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1392,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1398,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1397,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1401,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1399,24,33),random.randrange(1000))
    # bank.addAccount('ali','mohammadi',(1405,24,33),random.randrange(1000))
