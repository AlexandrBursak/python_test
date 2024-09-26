import re

# Вхідний рядок
s = "Hello world this Is a Test"
#print(s)

def count_uppercase_words(s: str) -> int:
        res = re.findall(r"[A-Z]+?", s)
        print(len(res))


count_uppercase_words(s)
