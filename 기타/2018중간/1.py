def complement9(n):
      s = str(n)
      ans = ""
      for c in s:
            ans += str(abs(9-int(c)))
      return int(ans)

print(complement9(9965))
