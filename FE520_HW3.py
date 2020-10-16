
import numpy as np

class Rectangular:
#    length_attribute = 10              #Testing
#    width_attribute = 20                #Testing /// Wrong way to go about this I think

    def __init__(self, length_attribute, width_attribute):
        self.length_attribute = length_attribute
        self.width_attribute = width_attribute

    def area(self):
        area = self.length_attribute*self.width_attribute
        return area                                         #changed from print(area) to return area
    def perimeter(self):
        perimeter = (self.length_attribute+self.width_attribute)*2
        return perimeter                                    #changed from print(perimeter) to return perimeter


class Time:
    def makeProper(self):
        if(self.sec > 60):
            self.min = self.min + self.sec//60
            self.sec = self.sec % 60
        if(self.min > 60):
            self.hours = self.hours + self.min//60
            self.min = self.min % 60

    def __init__(self, hours, min, sec):
        self.hours = hours
        self.min = min
        self.sec = sec

    def addTime(self, self2):
        self.sec = self.sec + self2.sec
        self.min = self.min + self2.min
        self.hours = self.hours + self2.hours
        self.makeProper()

    def addsTime(self, hours2, min2, sec2):
        self.sec = self.sec + sec2
        self.min = self.min + min2                  #Not sure which way you wanted us to add the time
        self.hours = self.hours + hours2            #The method can take in objects or parameters
        self.makeProper()

    def displayTime(self):
        print("Time 1: ", self.hours, " hours ", self.min, " minutes ", self.sec, " seconds")
    def DisplayMinute(self):
        self.sec = self.sec +(60*self.min) + (3600*self.hours)
        print(self.sec)



if __name__ == "__main__":
    """
    myRec = Rectangular(10,20)
    print(myRec.area())          #  If i dont want it to print the None portions into the terminal
    print(myRec.perimeter())      #  ust remove the print portions next to this comment and leave
    #                                   # myRec.area() and myRec.Perimeter()

    lengths  = np.array([1,2,3,4,5,6,7,8,9,10])
    widths = np.array([1,2,3,4,5,6,7,8,9,10])
    myRec = Rectangular(lengths,widths)
    print(myRec.area())
    print(myRec.perimeter())

    """
    myTime = Time(1, 20, 15)                        #These three cases were just used to test different method formats
    myTime2 = Time(2, 50, 10)
    myTime3 = Time(1, 20, 15)
    """
    myTime.addTime(myTime2)
    myTime.displayTime()
    print("==============")
    myTime3.addsTime(2, 50, 10)
    myTime3.displayTime()

    #print("=========", 123//6 )                #Used in testing for the makeProper function
    """
    myTime.DisplayMinute()
