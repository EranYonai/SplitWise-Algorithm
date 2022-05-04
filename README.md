# SplitWise-Algorithm
Simple console based Split Wise algorithm to split payments between friends.

Split Wise script & Algorithm, from what I know there are two approaches to solving this problem:
1. Greedy Algorithm
2. Dynamic Programming

According to Splitwise themselves, the greedy algorithm is the best approach.

And the rules are (according to SplitWise):
1. Everyone owes the same net amount at the end,
2. No one owes a person that they didn’t owe before, and (which is not as important imo)
3. No one owes more money in total than they did before the simplification.

Intersting reads on the subject:
1. NP Completeness - https://en.wikipedia.org/wiki/NP-completeness
2. Dinic's Algorithm - https://en.wikipedia.org/wiki/Dinic%27s_algorithm
3. Simplifying Payments with Linear Programming - https://miguelbiron.github.io/post/2018-02-09-simplifying-pmts-with-lp/
