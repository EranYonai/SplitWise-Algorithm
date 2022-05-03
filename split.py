import sys
# import numpy as np, pandas as pd

# Simple Split Wise script to split payment between multiple people

def init():
    print("Welcome to Split Wise")
    print("Add a friend and the amount they paid, \"Joe 10\".\nWhen you are done, type \"done\"")
    payments = {}
    key = "!=0"
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
    
def splitAlgo(payments):
    # this is an NP-complete problem, so we will use a greedy algorithm @https://en.wikipedia.org/wiki/NP-completeness
    # also, intersting read about Dinic's maxflow algorithm https://en.wikipedia.org/wiki/Dinic%27s_algorithm
    # and finally, the math https://miguelbiron.github.io/post/2018-02-09-simplifying-pmts-with-lp/
    total_participants = len(payments)
    total_spent = sum(payments.values())
    share = total_spent / total_participants
    # net out everyone's position
    for name in payments:
        payments[name] -= share
        payments[name] = round(payments[name], 2)
    print(f"{total_participants} Total Participants, each one should pay: {str(share)} ")
    print("-------------------------------------")
    while evenedOut(payments):
        min = getMin(payments)
        max = getMax(payments)
        print(min[0] + " owes " + max[0] + " " + str(abs(min[1])))
        payments[max[0]] += min[1]
        payments[min[0]] = 0
    print("-------------------------------------")
        
     
    # create a readable dataframe - will return to this.
    # mat = matrix of payments
    # column_labels = [f"to_{person}" for person in payments.keys()] 
    # index_labels = [f"{person}_owes" for person in payments.keys()]
    # df = pd.DataFrame(data=mat, columns=column_labels, index=index_labels)
    # return df.round(2)


# helper function, get minimum value of payments
def getMin(payments):
    min = ["", sys.maxsize]
    for name in payments:
        if payments[name] < min[1]:
            min = [name, payments[name]]
    return min

# helper function, get maximum value of payments
def getMax(payments):
    max = ["", -sys.maxsize]
    for name in payments:
        if payments[name] > max[1]:
            max = [name, payments[name]]
    return max

def evenedOut(payments):
    for name in payments:
        if abs(payments[name]) > 0.1:
            return True 
    return False    

# helper functions, get minimum of two values
def minOf2(a, b):
    return a if a < b else b


def main():
    splitAlgo(init())

main()