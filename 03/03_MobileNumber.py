def MobileNumber(Number):
  if len(Number) == 10 :
    if Number[:2] == '06' or Number[:2] == '08' or Number[:2] == '09':
      print("Mobile number")
    else:
      print("Not a mobile number")
  else:
    print("Not a mobile number")
Number = str(input())
MobileNumber(Number)