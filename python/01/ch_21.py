"""
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True"""

def close_far(a, b, c):
  close_found = False
  far_found = False
  smallest = min(a, b, c)  
  largest = max(a, b, c)
  mid = None
  for num in [a,b,c]:
      if num == smallest:
          continue  
      elif num == largest:
          continue
      else:
          mid = num  

  if abs(largest) - abs(smallest) >= 2 or abs(mid) - abs(smallest) >= 2 or abs(largest) - abs(mid) >= 2:
      far_found = True
  if abs(largest) - abs(smallest) <= 1 or abs(mid) - abs(smallest) <= 1 or abs(largest) - abs(mid) <= 1:
      close_found = True
  return (close_found and far_found)


print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))