import calendar

def validate_date(dueDate):
  s = duedate.split("-")
  if len(s) != 3:
    return False
  
  if len(s[0]) != 4:
    return False
  
  if len(s[1]) != 2 or int(s[1]) > 12:
    return False

  if len(s[2]) != 2 or int(s[2]) > calendar.monthrange(int(s[0]), int(s[1]))[1]:
    return False
  
  return True
  


duedate = "2023-01-31"

res = validate_date(duedate)
print(res)