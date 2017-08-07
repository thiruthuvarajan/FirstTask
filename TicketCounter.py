#Author : Thiru

import random
import Ticket_MoneyChange

TicktPrice = 25
choiceAvailable = [25,50,100]
Denominations_List = []
TotalCollection = 0
provideChange = {}
for i in range(1,10):
 AmountHolding = random.choice(choiceAvailable) #Choices Generated Randomly
 print("Person {0} : Holding : {1}".format(i,AmountHolding))

 if AmountHolding == TicktPrice :
  TotalCollection = TotalCollection + AmountHolding
  Denominations_List.append(AmountHolding)
  print("Ticket provided for Person number {0} and Total {1}".format(i,TotalCollection))
 else:
  Actcount = len(Denominations_List)
  tempHolding = AmountHolding - TicktPrice
  if Actcount > 0:
   lst = Ticket_MoneyChange.method(Denominations_List,tempHolding)
  else:
   lst = []

  if Actcount != len(lst) : #Checks change is available or not so it could change the returned List
    Denominations_List = lst
    Denominations_List.append(AmountHolding)
    TotalCollection = TotalCollection + AmountHolding
    AmountHolding = AmountHolding - TicktPrice
    TotalCollection = TotalCollection - AmountHolding
    print("Ticket provided for Person number {0} and Total Amount in Account {1}".format(i, TotalCollection))
  else:
    Denominations_List.append(AmountHolding)
    provideChange[i] = AmountHolding
    TotalCollection = TotalCollection + AmountHolding
    print("Ticket Holded for Person number {0} and Total Amount in Account {1}".format(i, TotalCollection))

 print("Denomination List",Denominations_List)
 print("Total Collection",TotalCollection)
 print("People await for Change",provideChange)
