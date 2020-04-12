from typing import List

def knapsackNaive(W: int, wt: List[int], val: List[int], n: int) -> int:
  if n == 0 or W == 0:
    return 0

  if wt[n - 1] > W:
    return knapsackNaive(W, wt, val, n - 1)
  else:
    return max(
      val[n - 1] + knapsackNaive(W - wt[n - 1], wt, val, n - 1),
      knapsackNaive(W, wt, val, n - 1)
    )

# Time: O(nW)
def knapsack(W: int, weights: List[int], values: List[int]) -> int:
  n = len(values)
  K = [0] * (W + 1)

  K[0] = 0

  for w in range(1, W + 1):
    max_sub_result = 0
    for i in range(1, n):
      wi = weights[i]
      vi = values[i]

      if wi <= w:
        subproblem_value = K[w - wi] + vi

        if subproblem_value > max_sub_result:
          max_sub_result = subproblem_value
    K[w] = max_sub_result


  return K[W]

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapsackNaive(W , wt , val , n))
print(knapsack(W , wt , val ))