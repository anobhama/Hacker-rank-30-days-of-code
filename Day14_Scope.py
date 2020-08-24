class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None
    def computeDifference(self):
        max_value = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                value = abs(self.__elements[i] - self.__elements[j])
                if value > max_value:
                    max_value = value
        self.maximumDifference = max_value

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)