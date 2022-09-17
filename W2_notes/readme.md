# Greedy Algorithms

## Greedy works for local not global

If you use the same greedy strategy, then LargestConcatenate([2, 21]) returns 212 and Change(8, [1, 4, 6]) returns 3 because 8 = 6 + 1 + 1. But this strategy fails because the correct solutions are 221 (concatenating 2 with 21) and 2 because 8 = 4 + 4!

Thus, in rare cases when a greedy strategy works, one should be able to prove its correctness: A priori, there should be no reason why a sequence of locally optimal moves leads to a global optimum!

## Change problem

```py
return money//10 + (money % 10)//5 + money % 5
```
