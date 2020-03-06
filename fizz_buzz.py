def fizzbuzz():
    for i in range (1, 101):
        if i % 3 == 0:
            print('Fizz')
        if i % 5 == 0:
            print('Buzz')
        if i % 3 == 0 and i % 5 == 0:
            print ('FizzBuzz')
        else:
            print(i)

"""modulus is establishing the multiples of 3 and 5 for the 'if' statements in lines 3 and 5
in line 7 its acknowledging numbers that are both and in line 9 its dealing with all other conditions"""

fizzbuzz()
