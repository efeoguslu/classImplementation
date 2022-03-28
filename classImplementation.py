class Students:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def inputGrades(self, numGrades):
        self.numGrades = numGrades
        self.grades = []

        for i in range(0, numGrades, 1):
            prompt = "please enter grade for "+self.first+": "
            grade = float(input(prompt))
            self.grades.append(grade)

        print("end of grades for " + self.first)
        # return self.grades

    def printGrades(self):
        print(self.first, self.last, "'s grades are: ")

        for i in range(0, self.numGrades, 1):
            print(self.grades[i])

    def averageGrades(self):
        total = 0
        for i in range(0, self.numGrades, 1):
            total += self.grades[i]
        average = total/self.numGrades
        #self.average = average
        return round(average, 3)

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
student2 = Students('yammur', 'marla')

print(student1.first, student1.last)


numGrades1 = int(input("how many grades do you want for efe: "))
numGrades2 = int(input("how many grades do you want for yammur: "))

student1.inputGrades(numGrades1)
student2.inputGrades(numGrades2)
student1.printGrades()
student2.printGrades()

average1 = student1.averageGrades()
low1 = student1.lowGrade()
high1 = student1.highGrade()

average2 = student2.averageGrades()
low2 = student2.lowGrade()
high2 = student2.highGrade()

print("average of grades of efe: ", average1)
print("lowest grade for efe: ", low1)
print("highest grade for efe: ", high1)
print(" ")
print("average of grades of yammur: ", average2)
print("lowest grade for yammur: ", low2)
print("highest grade for yammur: ", high2)


# print(testGrade)
# print(student1.grades)
