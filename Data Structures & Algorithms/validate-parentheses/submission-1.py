class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="[" or i=="(" or i=="{" :
                stack.append(i)
            elif i==")":
                try:
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
            elif i=="]":
                try:
                    if stack[-1]=="[":
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
            elif i=="}":
                try:
                    if stack[-1]=="{":
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
        return True


        
        