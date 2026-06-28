
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        wants={}
        rem=len(students)
        for i in students:
            if i in wants:
                wants[i]+=1
            else:
                wants[i]=1
        for i in sandwiches:
            if wants[i] > 0:
                wants[i]-=1
                rem-=1
            else:
                return rem
        return 0
        