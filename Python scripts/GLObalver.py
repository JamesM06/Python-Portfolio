

score = 0
answer = "Yes"


def increase_score(a, b):
    if b == "Yes":
        score = a + 1
        return score

score = 0
answer = "Yes"
 
z = increase_score(score, answer)
print(z)
