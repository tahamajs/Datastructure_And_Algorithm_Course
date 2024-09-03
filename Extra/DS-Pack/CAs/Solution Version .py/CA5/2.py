import sys
sys.setrecursionlimit(10 ** 6)

class Person :
    def __init__(self, teamWork, hardWorking, index) :
        self.teamWork = teamWork
        self.hardWorking = hardWorking
        self.index = index
        self.totalPower = teamWork + hardWorking

class Solution :
    def __init__(self) :
        self.n = int(input())
        self.hardWorkings = input().split()
        self.teamWorks = input().split()
    
    def make_persons(self) :
        persons = []
        for i in range(self.n) :
            p = Person(int(self.teamWorks[i]), int(self.hardWorkings[i]), i + 1)
            persons.append(p)
        return persons
    
    def merge_sort(self, ls) :
        if len(ls) > 1 :
            m = len(ls) // 2
            left = ls[: m]
            right = ls[m :]
            self.merge_sort(left)
            self.merge_sort(right)
        
            i = j = k = 0

            while i < len(left) and j < len(right) :
                if left[i].totalPower >= right[j].totalPower :
                    ls[k] = left[i]
                    i += 1
                else :
                    ls[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left) :
                ls[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right) :
                ls[k] = right[j]
                j += 1
                k += 1
    

    def check_validation(self, persons, k) :
        lTWSum = 0
        rTWSum = 0
        lHWSum = 0
        rHWSum = 0
        
        for i in range(k) :
            lTWSum += persons[i].teamWork
            lHWSum += persons[i].hardWorking
        
        for i in range(k, self.n) :
            rTWSum += persons[i].teamWork
            rHWSum += persons[i].hardWorking
        
        if lTWSum > rTWSum and lHWSum > rHWSum :
            return
        else :
            lMinTW = lMinHW = persons[0]
            rMaxTW = rMaxHW = persons[self.n - 1]

            for i in range(k) :
                if persons[i].teamWork < lMinTW.teamWork :
                    lMinTW = persons[i]
                if persons[i].hardWorking < lMinHW.hardWorking :
                    lMinHW = persons[i]
            
            for i in range(k, self.n) :
                if persons[i].teamWork > rMaxTW.teamWork :
                    rMaxTW = persons[i]
                if persons[i].hardWorking > rMaxHW.hardWorking :
                    rMaxHW = persons[i]
            
            dTW = rMaxTW.teamWork - lMinTW.teamWork
            dHW = rMaxHW.hardWorking - lMinHW.hardWorking

            if dTW > dHW :
                persons[lMinTW.index - 1] = rMaxTW
                persons[rMaxTW.index - 1] = lMinTW
            else :
                persons[lMinHW.index - 1] = rMaxHW
                persons[rMaxHW.index - 1] = lMinHW
            
            self.check_validation(persons, k)


    def print_ans(self) :
        persons = self.make_persons()
        self.merge_sort(persons)
        k = self.n // 2 + 1
        self.check_validation(persons, k)
        print(k)
        for i in range(k) :
            print(persons[i].index, end = ' ')
        print()

s = Solution()
s.print_ans()