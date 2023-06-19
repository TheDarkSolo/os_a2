from threading import Thread #import the Thread

balance = 1000 #initialize the initial balance

def john(): #withdraw function of john
    global balance #global variable to be accessed by both John and Anna
    for i in range(numberOfTransactions): #in range numberOfTransactions
        amount = 100 + (200 * i) #100,300,500...
        balance -= amount # when withdraw balance decreases
        print(f"John withdrawn {amount} with remaining current balance {balance}") #string literals to print the message

def anna(): #deposit function of anna
    global balance #global variable to be accessed by both John and Anna
    for i in range(numberOfTransactions): #loop until numOfTransactions
        deposit = 200 + (200 * i) #deposit is $100 more than john withdraw
        balance += deposit  # when deposit balance increases
        print(f"Anna deposited {deposit} and new balance is [{balance}]") #f-string to print message

numberOfTransactions = int(input("Enter the number of John&Anna transactions:")) #ask user input
print(f"The initial value of the account: {balance}") #print initial balance

t1 = Thread(target=john) #create john thread
t2 = Thread(target=anna) #create anna thread

t1.start() #start john thread
t2.start() #start anna thread

t1.join() #wait for thread to finish
t2.join() #wait for thread to finish

print(f"The final amount: {balance}") #print final balance

# If process synchronization is not considered, the issues are the race condition
# and incorrect, unordered outputs due to the mix of thread operations.
