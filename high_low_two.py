# def usernum():
#     number = input('Give me a number between 0-10\n')
#
# def random():
#     x = range(0, 11)
#     for r in x:
#         rand = r
import random

def decider():
    number = int(input('Give me a number between 0-10\n'))
    rand = random.randint(0, 11)
    # for number > 0 and number <= 10:

    """line 13 is supposed to validate whether or not the user in put is between 1-10.  It's not working"""

    if rand > number:
        print('Too low')
        decider()
    elif number > rand:
        print('Too high')
        decider()
    else:
        print('You got it')


# usernum()
decider()
# print(rand)

# else:
# print("number's not between 1 and 10")
