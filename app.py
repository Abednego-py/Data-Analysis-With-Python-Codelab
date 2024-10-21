def sort_numbers(list_of_nums,sort_order):
  sort_order = sort_order.lower()
  if sort_order not in ("asc", "desc", "none"):
    return "You did not enter a valid sorting order"
  if sort_order == "asc":
    list_of_nums = sorted(list_of_nums)
    return f'The list of nums in asc order : {list_of_nums}' 
  elif sort_order == "desc":
    return f'The list of nums in desc order : {sorted(list_of_nums, reverse=True)}'
  else:
     return f'The original list is : {list_of_nums}'
  
