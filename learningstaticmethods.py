'''static method allows accces without the need to initialize a class
init without creatig an object
mainly used as utility method or when it doesn't make sense for a real world obejct to
be able to perform a task but you still need to have that method available
'''
class Sum:
    @staticmethod
    def getSum(*args):

        sum = 0
        for i in args:
            sum += i
        return sum
def main():
    print("Sum: ", Sum.getSum(1,2,3,4,5))

main()