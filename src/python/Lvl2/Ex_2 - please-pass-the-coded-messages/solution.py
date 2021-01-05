def solution(l):
  if len(l) == 0:
    return 0
  if len(l) == 1:
    return sorted_list[0] if sorted_list[0] % 3 == 0 else 0

  sorted_list = sorted(l)
  list_sum_mod = sum(sorted_list) % 3
  if list_sum_mod == 0:
    return create_largest_num(sorted_list)
  else:
      element_to_remove = find_first_occ(sorted_list, lambda x: x%3 == list_sum_mod, -1)
      if element_to_remove != -1:
        sorted_list.remove(element_to_remove)
      else:
          modulo_to_remove = (3 - list_sum_mod)
          element_to_remove = find_first_occ(sorted_list, lambda x: x%3 == modulo_to_remove, -1)
          sorted_list.remove(element_to_remove)
          element_to_remove = find_first_occ(sorted_list, lambda x: x%3 == modulo_to_remove, -1)
          sorted_list.remove(element_to_remove)
  return create_largest_num(sorted_list)

def find_first_occ(lst,condition,default_val):
  return next((num for num in lst if condition(num)), default_val)

def create_largest_num(lst):
  if len(lst) == 0 :
    return 0
  sorted_l_reverse = reversed(lst)
  str_number = ''.join(str(num) for num in sorted_l_reverse)
  return int(str_number)