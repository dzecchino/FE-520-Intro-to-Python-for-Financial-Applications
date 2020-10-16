class LCG:

    def __init__(self, seed, multiplier,increment, modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
    def LinearCongruentialGenerator(self):
#        while(True):      #  useless
        self.seed = ((self.multiplier*self.seed + self.increment) % self.modulus)
#            if(self.seed % 4 == 2):      #also useless
        return self.seed
    def getTheSeed(self):
        return self.seed
    def setTheSeed(self, seed):
        self.seed = seed

    def nextRandomNum(self):
        return self.LinearCongruentialGenerator()
    def giveSequence(self, length):
        array = []
        for i in range(length):
            array.append(self.LinearCongruentialGenerator())
        return array

class SCG(LCG):
    def __init__(self, seed, multiplier,increment, modulus):
        if(seed % 4 ==2):
            self.seed = seed
        else:
            raise Exception("Seed does not satisfy condition: seed % 4 = 2.")
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
    def LinearCongruentialGenerator(self):
        self.seed = ((self.seed*(self.seed + 1)) % self.modulus)
        return self.seed

if __name__ == "__main__":
    generate = LCG(2, 1103515245, 12345, 2**32)
#    print(generate.nextRandomNum())

    length = 5
#    print(generate.giveSequence(length))

#    print(generate.nextRandomNum())
#    print(generate.nextRandomNum())

#    print(generate.getTheSeed())

    generate2 = SCG(3, 1103515245, 12345, 2**32)
#    print(generate2.getTheSeed())                              #Print statements all run
#    print(generate2.giveSequence(length))                      #Error code for SCG works
#    print(generate2.nextRandomNum())                           
#    print(generate2.nextRandomNum())
