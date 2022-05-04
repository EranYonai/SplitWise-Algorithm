# Split Wise script & Algorithm, from what've read there are two approaches to solving this problem
# 1. Greedy Algorithm
# 2. Dynamic Programming
# According to Splitwise themselves, the greedy algorithm is the best approach.
# And the rules are:
# 1. Everyone owes the same net amount at the end,
# 2. No one owes a person that they didn’t owe before, and (which is not as important imo)
# 3. No one owes more money in total than they did before the simplification.
#
# Articles on the subject:
# 1. NP Completeness - https://en.wikipedia.org/wiki/NP-completeness
# 2. Dinic's Algorithm - https://en.wikipedia.org/wiki/Dinic%27s_algorithm
# 3. Simplifying Payments with Linear Programming - https://miguelbiron.github.io/post/2018-02-09-simplifying-pmts-with-lp/

import sys
# import numpy as np, pandas as pd


def init() -> dict:
    """ Initialize the payments dictionary
    Returns:
        _type_: dict
    """
    print("Welcome my Split Wise Algo")
    print("Add a friend and the amount they paid, \"Joe 10\".\nWhen you are done, type \"done\"")
    payments = {}
    key = ""
    while key != "done":
        key = input("Add friend and amount: ")
        if key == "done":
            break
        if key.find(" ") == -1:
            print("Invalid input")
            continue
        toInsert = key.split(" ")
        payments[toInsert[0]] = int(toInsert[1])
    return payments
    
def splitAlgoZero(payments: dict) -> None:
    """This is my first approach to Splitwise Algorithm
    not perfect, it will never pay more/less than needed but in certian cases it will make someone who basically doesn't need to pay - to pay.
    for example, input: A 150, B 223, C 0, D 0 | net cash: A 57, B 130, C -93, D -93
    1. C -> B 93 | A 57, B 36, C 0, D -93
    2. D -> A 93 | A -36, B 36, C 0, D 0
    3. A -> B 36 | A 0, B 0, C 0, D 0 # A does not need to pay in this case. optimal solution is that D/C pays some of the debt to A and some to B.
    Args:
        payments (dict): dictionary of {name: amount}
    """
    # start with integers i need:
    total_participants = len(payments)
    total_spent = sum(payments.values())
    share = total_spent / total_participants
    # net cash everyone: NetChange(name) = (amount - share)
    for name in payments:
        payments[name] -= share
        payments[name] = round(payments[name], 2) #2?
    
    print(f"{total_participants} Total Participants, each one should pay: {str(share)} ")
    print("-------------------------------------")
    # this is the heart algoritm, basic, easy, and has some problems. :), but it works.

    while evenedOut(payments):
        min = getMin(payments)
        max = getMax(payments)
        print(min[0] + " owes " + max[0] + " " + str(abs(min[1])))
        payments[max[0]] += min[1]
        payments[min[0]] = 0
    print("-------------------------------------")

    # this part is for future output, outputing the debt in a matrix using numpy and pandas.
    # mat = matrix of payments
    # column_labels = [f"to_{person}" for person in payments.keys()] 
    # index_labels = [f"{person}_owes" for person in payments.keys()]
    # df = pd.DataFrame(data=mat, columns=column_labels, index=index_labels)
    # return df.round(2)

def splitAlgoOne(payments: dict) -> None:
    """Second approach, which solves Zero's problems.
    Rules:
    1. Each Giver shall pay exactly his share, this can be divided between receviers.
    2. Recivers shall not pay, only receive.
    Let's see an example of the current algo:
    input: A 150, B 223, C 0, D 0 | net cash: A 57, B 130, C -93, D -93
    1. C -> B 93 | A 57, B 36, C 0, D -93
    2. D -> A 57 | A 0, B 36, C 0, D 36
    3. D -> B 37 | A 0, B 0, C 0, D 0 /exit
    Args:
        payments (dict): dictionary of {name: amount}
    """
    # start with integers i need:
    total_participants = len(payments)
    total_spent = sum(payments.values())
    share = total_spent / total_participants
    # net cash everyone: NetChange(name) = (amount - share)
    for name in payments:
        payments[name] -= share
        payments[name] = round(payments[name], 2) #2?
    
    print(f"{total_participants} Total Participants, each one should pay: {str(share)} ")
    print("-------------------------------------")
    # this is the heart algoritm, basic, easy, and has some problems. :), but it works.
    while evenedOut(payments):
        min = getMin(payments)
        max = getMax(payments)
        to_pay = 0
        if abs(min[1]) <= max[1]:
            to_pay = min[1]
        else:
            to_pay = max[1]
        to_pay = abs(to_pay)
        print(min[0] + " owes " + max[0] + " " + str(to_pay))
        payments[max[0]] -= to_pay
        payments[min[0]] = min[1] + to_pay
    print("-------------------------------------")


def getMin(payments: dict) -> list:
    """Calculates minimum amout paid in given dict.

    Args:
        payments (dict): payments dictionary of {name: amount}

    Returns:
        list: [name, amount] min value
    """
    min = ["", sys.maxsize]
    for name in payments:
        if payments[name] < min[1]:
            min = [name, payments[name]]
    return min

def getMax(payments: dict) -> list:
    """Calculates maximum amount paid in given dict.

    Args:
        payments (dict): payments dictionary of {name: amount}

    Returns:
        list: [name, amount] max value
    """
    max = ["", -sys.maxsize]
    for name in payments:
        if payments[name] > max[1]:
            max = [name, payments[name]]
    return max

def evenedOut(payments: dict) -> bool:
    """Verifies that all net cash is 0.

    Args:
        payments (dict): payments dictionary of {name: amount}, after net cash.

    Returns:
        bool: True if all net cash is 0, False otherwise.
    """
    for name in payments:
        if abs(payments[name]) > 0.1: # TODO fix this!
            return True 
    return False    

# def minOf2(a, b): not using that for now.
#     return a if a < b else b


def main():
    """Main function, kickstarter.
    """
    splitAlgoOne(init())

if __name__ == "__main__":
    main()