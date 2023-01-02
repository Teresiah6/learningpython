'''
Create a class that returns values from the fibonacco sequence
each time next is called
sample output
Fib: 1
Fib: 2
Fib: 3
Fib: 5
'''
class Fibo:
    def __init__(self):
        self.fib1= 0
        self.fib2 = 1
    def __iter__(self):
        return(self)

    def __next__(self):
        fibNum  =  self.fib1 + self.fib2
        self.fib1 = self.fib2
        self.fib2 =  fibNum
        return fibNum

fibing = Fibo()
for i in range(10):
    print(f"Fib: {next(fibing)}")
