### Challenge 2 

def intersection(l1, l2, l3):
  # We create a list that checks if a number is common in the first two lists. If it is, it is added. 
  c = [x for x in l1 if x in l2]

  # We create a 2nd list that checks if a number is common in the above created (new) list and the remaing. If it is, it is added to a new list. 
  d = [x for x in l2 if x in l3]

  # The final list is returned
  return d  

print(intersection([1, 2, 3, 4, 5, 6], [2, 4, 6, 8], [3, 4, 5]))