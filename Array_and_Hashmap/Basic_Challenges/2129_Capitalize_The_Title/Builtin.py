class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.split()
        for i in range(len(title)):
            e=title[i]
            if len(e)<3:
                title[i]=e.lower()
            else:
                title[i]=e.title()
        return " ".join(title)