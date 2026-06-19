class Solution:
    def calPoints(self, operations):
        record=[]
        count=-1
        for i,txt in enumerate(operations):
            if txt.isdigit():
                record.append(int(txt))
            elif txt=="+":
                record.append(record[-1]+record[-2])
            elif txt=="D":
                record.append(record[-1]*2)

            elif txt=="C":
                record.pop()
            # print(f"Op:{txt}   Record:{record}   Count:{count}")


        return sum(record)
    
# print(Solution().calPoints(["1","2","+","C","5","D"]))