import re

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        worlds_1 = sentence1.split()
        worlds_2 = sentence2.split()
        if len(worlds_1) > len(worlds_2):
            w2 = worlds_2
            s1 = sentence1
        else:
            w2 = worlds_1
            s1 = sentence2
            
        reg_word = '(^{word} .*$)|(^.* {word}$)'.format(word = ' '.join(w2))
        for idx in range(len(w2)):
            global_split = '|'
            if idx+1 != len(w2):
                reg_word += (global_split + '(^' + ' '.join(w2[:idx+1]) + ' .* ' + ' '.join(w2[idx+1:]) + '$)')

        reg = rf'^{reg_word}$'

        reg_match = re.match(reg, s1)
        if reg_match:
            return True
        return False

solution = Solution()

sentence1 = "My name is Haley"
sentence2 = "My Haley"
expected = True

print(solution.areSentencesSimilar(sentence1, sentence2), '==', expected, ':', sentence1, ':', sentence2)

sentence1 = "of"
sentence2 = "A lot of words"
expected = False

print(solution.areSentencesSimilar(sentence1, sentence2), '==', expected, ':', sentence1, ':', sentence2)

sentence1 = "Eating right now"
sentence2 = "Eating"
expected = True

print(solution.areSentencesSimilar(sentence1, sentence2), '==', expected, ':', sentence1, ':', sentence2)

sentence1 = "pp ZM ZJ lE B"
sentence2 = "ZM"
expected = False

print(solution.areSentencesSimilar(sentence1, sentence2), '==', expected, ':', sentence1, ':', sentence2)

sentence1 = "qbaVXO Msgr aEWD v ekcb"
sentence2 = "Msgr aEWD ekcb"
expected = False

print(solution.areSentencesSimilar(sentence1, sentence2), '==', expected, ':', sentence1, ':', sentence2)

sentence1 = "eTUny i b R UFKQJ EZx JBJ Q xXz"
sentence2 = "eTUny i R EZx JBJ xXz"
expected = False

print(solution.areSentencesSimilar(sentence1, sentence2), '==', expected, ':', sentence1, ':', sentence2)

sentence1 = "A A"
sentence2 = "A aA"
expected = False

print(solution.areSentencesSimilar(sentence1, sentence2), '==', expected, ':', sentence1, ':', sentence2)

sentence1 = "AaA AA"
sentence2 = "a AaA AA A"
expected = False

print(solution.areSentencesSimilar(sentence1, sentence2), '==', expected, ':', sentence1, ':', sentence2)
