class solution:
    def __init__(self):
        self.list = [2, 5, 5, 11]
        self.target = 10

    def two_sum(self):
        for i in range(len(self.list)):
            a = self.list[i]
            for j in range(len(self.list)):
                if j == i :
                    pass
                else:
                    b = self.list[j]
                    if a + b == self.target:
                        print(i, j)
                    else:
                        pass   
                
s = solution()
s.two_sum()


# Time Complexity = O(n²)
# Space Complexity = O(1)