def GetPrimes(num):
  # STYLE: Function name should be snake_case (get_primes)
  
  l = [] 
  # STYLE: Variable name 'l' is ambiguous (looks like 1)
  
  # This function gets all prime numbers up to num
  # BUG: range(0, num) is exclusive, so it checks up to num-1
  for i in range(0, num):
    flag = False
    
    # PERF: Dealing with 0 and 1 inside the loop is inefficient
    if i > 1:
      # PERF: Slow algorithm (O(n^2)). Should stop at sqrt(i).
      for j in range(2, i):
        if (i % j) == 0:
          flag = True
          break
      
      # STYLE: 'if flag: pass' is anti-pattern. Use 'if not flag:'
      if flag:
        pass
      else:
        l.append(i)
  return l

# Test the function
result = GetPrimes(100)
print(result)
