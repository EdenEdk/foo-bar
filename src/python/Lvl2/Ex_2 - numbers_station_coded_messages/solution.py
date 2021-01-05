def solution(numbers_list: list, target: int) -> list:
  result= [-1,-1]
  left_index = 0
  right_index = 0
  sum = numbers_list[0]
  numbers_list_length = len(numbers_list)
  while sum!=target and right_index<numbers_list_length : 
    print("Now: ", left_index, right_index, sum)
    if sum < target:
      right_index+=1
      if right_index<numbers_list_length:
        sum+=numbers_list[right_index]
    elif sum > target:
      sum-=numbers_list[left_index]
      left_index+=1
  if sum == target:
    result = [left_index, right_index]
  return result