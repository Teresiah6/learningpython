import threading
import time
import random

class BankAccount(threading.Thread):
    accountBalance = 100
    def __init__(self, name, amountRequested):
        threading.Thread.__init__(self)
        self.name = name
        self.amountRequested = amountRequested

    def run(self):
        threadLock.acquire()
        BankAccount.getMoney(self)
        threadLock.release()
    @staticmethod
    def getMoney(customer):
        print("{} tries to withdraw ${} at {}".format(customer.name,
                                                      customer.amountRequested,
                                                      time.strftime("%H:%M:%S", time.gmtime())))
        if BankAccount.accountBalance - customer.amountRequested > 0:
            BankAccount.accountBalance -= customer.amountRequested
            print("New account balance: $ {}". format(BankAccount.accountBalance))
        else:
            print("Not enough money in account")
            print("Current balance: ${}".format(BankAccount.accountBalance))
        time.sleep(3)
threadLock = threading.Lock()

doug = BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally", 45)

doug.start()
paul.start()
sally.start()

doug.join()
paul.join()
sally.join()

print("Transactions have ended")
