class Solution:
    def calPoints(self, operations):
        record=[]
        for i in operations:
            if i=="+":
                record.append(record[-1]+record[-2])
            elif i=="D":
                record.append(record[-1]*2)
            elif i=="C":
                record.pop()
            else:
                record.append(int(i))
            # print(f"Op:{i}   Record:{record}   Count:{count}")
        return sum(record)
    
# print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))