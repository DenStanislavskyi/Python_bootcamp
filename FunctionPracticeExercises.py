# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
    # lesser_of_two_evens(2,4) --> 2
    # lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a,b):
    if a % 2==0 and b % 2 == 0:
        return min(a,b)
    elif a % 2 != 0 or b % 2 != 0:
        if a > b:
        return max(a,b)


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
   #animal_crackers('Levelheaded Llama') --> True
   #animal_crackers('Crazy Kangaroo') --> False
   def animal_crackers(text):
    list = text.split()
    if list[0][0] == list[1][0]:
        return True
    else:
        return False

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or (n1 + n2) == 20:
        return True
    else:
        return False

 # OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
 # old_macdonald('macdonald') --> MacDonald
 def old_macdonald(name):
    if len(name) > 3:
        return name[0].upper()+ name[1:3] + name[3].upper() + name[4:]


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
def master_yoda(text):
    list = text.split()
    list.reverse()
    return (" ".join(list))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

def almost_there(n):
    if n in range(90,111) or n in range(190,211):
        return True
    else:
        return False


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(text):
    longstring = ""
    for elem in text:
        longstring =longstring + elem*3 
    return longstring

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    sum = a + b + c
    if a == 11 or b == 11 or c == 11:
        sum = sum - 10
    if sum <= 21:
        return sum
    else:
        return "BUST"

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    agent=[]
    for num in nums:
        if num ==0 or num ==7:
            agent.append(str(num))
    isagent = "".join(agent)
    if isagent == "007":
        return True
    else: 
        return False

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)