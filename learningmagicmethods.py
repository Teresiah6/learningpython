'''surrounded by __ on both sides
used to define how operators like +, -, *, /. == , > < etc work
e.g __eq__: Equal
__mod__: modulus etc
'''
class Time():

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return ("{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))

    def __add__(self, other_time):
        new_time = Time()
        #add in a way that time makes sense minutes and seconds !> 60 and hours !>24
        if (self.second + other_time.second) >=  60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second - other_time.second
        #for minutes
        if (self.minute + other_time.minute) >=  60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute - other_time.minute
        #for hours
        if (self.hour + other_time.hour) >= 24:
            new_time.hour  = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour
        return new_time

    # EXERCISE: Get Time to work with other operators
    #subtract
    def __sub__(self, other_time):
        new_time = Time()
        if (self.second - other_time.second) < 0:
            self.minute -= 1
            self.second += 60
            new_time.second = (self.second - other_time.second)
        else:
            new_time.second = self.second - other_time.second
        #for minutes
        if (self.minute - other_time.minute) < 0:
            self.hour -= 1
            self.minute += 60
            new_time.minute = (self.minute - other_time.minute)
        else:
            new_time.minute = self.minute - other_time.minute
        #for hours
        if (self.hour - other_time.hour):
            new_time.hour = (self.hour - other_time.hour)
        '''else:
            new_time.hour = self.hour - other_time.hour'''
        return new_time


def main():
    time1 = Time(23, 60, 30)
    print(time1)

    time2 = Time(21, 41, 30)
    print(time1 + time2)
    print()
    print(time1 - time2)
    print(time2 - time1) # i'm losing a minute somewhere

main()
#EXERCISE: Get Time to work with other operators