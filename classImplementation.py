class Students:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def inputGrades(self, numGrades):
        self.numGrades = numGrades
        self.grades = []

        for i in range(0, numGrades, 1):
            grade = float(input('please enter grade: '))
            self.grades.append(grade)

        # return self.grades

    def printGrades(self):
        print(self.first, self.last, "'s grades are: ")

        for i in range(0, self.numGrades, 1):
            print(self.grades[i])
            print(' ')

    def averageGrades(self):
        total = 0
        for i in range(0, self.numGrades, 1):
            total += self.grades[i]
        average = total/self.numGrades
        #self.average = average
        return average

    def lowGrade(self):
        low = 100
        for i in range(0, self.numGrades, 1):
            if(self.grades[i] < low):
                low = self.grades[i]

        return low

    def highGrade(self):
        high = 0
        for i in range(0, self.numGrades, 1):
            if(self.grades[i] > high):
                high = self.grades[i]

        return high


student1 = Students('efe', 'oguslu')


print(student1.first, student1.last)


numGrades = int(input("how many grades do you want: "))

student1.inputGrades(numGrades)
student1.printGrades()

average = student1.averageGrades()
low = student1.lowGrade()
high = student1.highGrade()

print("average of grades: ", average)
print("low grade: ", low)
print("high grade: ", high)


# print(testGrade)
# print(student1.grades)
