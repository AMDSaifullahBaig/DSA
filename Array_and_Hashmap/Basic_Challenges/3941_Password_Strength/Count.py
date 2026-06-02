class Solution:
    def passwordStrength(self, password: str) -> int:
        password=set(password)
        char=set("!@#$")
        c=0
        for i in password:
            if i.isdigit():
                c+=3
            elif i in char:
                c+=5
            elif i.isupper():
                c+=2
            elif i.islower():
                c+=1
        return c