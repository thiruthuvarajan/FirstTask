
#Author: Thiru

def method(arg1,arg2):
 tmpList = arg1[:]
 #print(tmpList)
 if len(arg1) > 0 :
  print(arg1,arg2)
  i = 0
  while (i < len(tmpList)):
    OrgVal = arg2 - tmpList[i]
    if OrgVal ==0 or OrgVal > 0 :
      arg2 = OrgVal
#      print("TEMP LIST VALUE : {0} ".format(tmpList[i]))
      del tmpList[i]
      i=i-1
    i=i+1

 if arg2 != 0 and len(arg1)>0:
     return arg1
 else:
     return  tmpList
