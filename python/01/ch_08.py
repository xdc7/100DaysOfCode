
"""

We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""

def make_chocolate(small, big, goal):
  count_big = 0
  count_small = 0
  target = goal
  for i in range (1, big + 1):
      if goal % big == 0:
        count_big += 1
        goal = goal - 5
  if (big * 5) + small >= target:
    return goal  
  else:
      return -1  




print (make_chocolate(4,1,9))
print (make_chocolate(4,1,10))
print (make_chocolate(4,1,7))