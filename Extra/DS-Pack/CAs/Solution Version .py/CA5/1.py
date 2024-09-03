class Solution :
    def __init__(self) :
        self.info = input().split()
        self.x = self.info[0]
        self.y = self.info[1]
    
    def count_common_divisors(self) :
        cdCounts = 0
        p = len(self.x)
        q = len(self.y)

        for i in range(1, min(p, q) + 1) :
            if p % i == 0 and q % i == 0 :
                if self.x[0 : i] == self.y[0 : i] :
                    if self.x[0 : i] * (p // i) == self.x and self.y[0 : i] * (q // i) == self.y :
                        cdCounts += 1
        return cdCounts

s = Solution()
print(s.count_common_divisors())
