class Solution:
    def calPoints(self, operations):
        record=[]
        count=-1
        for i,txt in enumerate(operations):
            if txt.isdigit():
                record.append(int(txt))
                count+=1
            elif txt=="+":
                record.append(record[count-1]+record[count-2])
                count+=1
            elif txt=="D":
                record.append(record[count]*2)
                count+=1

            elif txt=="C":
                record.pop()
                count-=1
            # print(f"Op:{txt}   Record:{record}   Count:{count}")


        return sum(record)
    
# print(Solution().calPoints(["1","2","+","C","5","D"]))