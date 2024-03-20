def is_mobile_number(Number):
  if len(Number) == 10 :
    if Number[:2] == '06' or Number[:2] == '08' or Number[:2] == '09':
      return True
    else:
      return False
  else:
    return False
exec(input())