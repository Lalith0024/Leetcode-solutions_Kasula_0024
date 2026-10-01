class Solution:
    def isValid(self, s: str) -> bool:
        # dic = {"(" : 0, ")":0, "{" : 0, "}" : 0, "[" :0,"]":0}
        # for i in s:
        #     if i == "(":
        #         dic["("]+=1
        #     if i == ")":
        #         dic[")"]+=1
        #     if i == "{":
        #         dic["{"]+=1
        #     if i == "}":
        #         dic["}"]+=1
        #     if i == "[":
        #         dic["["]+=1
        #     if i=="]":
        #         dic["]"]+=1
        # if (dic["("] == dic[")"]) and (dic["{"] == dic["}"]) and (dic["["] == dic["]"]):
        #     return True
        # return False

        stack = []
        for i in s:
            if i=="(" or i== "{" or i=="[":
                stack.append(i)
            else:
                if stack:
                    if i==")" and stack[-1]=='(':
                        stack.pop()
                    elif i=="}" and stack[-1]=='{':
                        stack.pop()
                    elif i=="]" and stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(s)%2!=0:
            return False
        if stack:
            return False
        return True



        # for i in s:
        #     if i == "(" or i== "{" or i=="[":
        #         stack.append(i)
        #     else:
        #         if i == ")":
        #             if stack[-1] == "(":
        #                 stack.pop()
        #             else:
        #                 return False
        #         elif i == "}":
        #             if stack[-1] == "{":
        #                 stack.pop()
        #             else:
        #                 return False
        #         elif i == "]":
        #             if stack[-1] == "[":
        #                 stack.pop()
        #             else:
        #                 return False
        # if len(stack) == 0:
        #     return True
        # return False
