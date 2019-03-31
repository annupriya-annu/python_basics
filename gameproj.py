import random

#get guess
def get_guess():
    return list(input('please enter  your guess:'))

#get computer logic digit 123
def generate_code():
    digits=[str(num) for num in range(10)]
        #shuffle the digits
    random.shuffle(digits)
        # grab first 3 digits
    return digits[:3]
    

def generate_clues(code,user_guess):
    if user_guess==code:
        return "CODE CRACKED!"
    clues = []

    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append('Match')
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

#get clues



#run gane logic

print("welcome code breaker")
secret_code=generate_code()
print(secret_code)
clueReport=[]
while clueReport!="Code Cracked!":
    guess=get_guess()

    clueReport=generate_clues(guess,secret_code)
    print("Here is the result of your guess: ")

    for clue in clueReport:
        print(clue)






    

    

    

x= get_guess()
print(type(x))
print(generate_code())
