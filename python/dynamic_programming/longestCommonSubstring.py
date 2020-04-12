def lcm(x: str, y: str) -> int:
  dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

  for i, c in enumerate(x):
    for j, d in enumerate(y):
      if c == d:
        dp[i + 1][j + 1] = 1 + dp[i][j]
      else:
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
  return dp[-1][-1]

print(lcm("pmjghexybyrgzczy", "hafcdqbgncrcbihkd",))