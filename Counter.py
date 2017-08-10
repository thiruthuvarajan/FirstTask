import random

balance = waitList = waitList75 = waitList100 = ticketed = 0
waitList100Flag = waitList75Flag = False
denomination = []

print("\nWelcome to Ticket Counter!!!")
print("\nTicket Price = Rs.25\nInitial Balance = Rs." + str(balance))
highRange = int(input("\nEnter total number of people waiting in Queue : "))

if highRange <= 20:

    for i in range(1, highRange+1):
        ticket = random.choice([25, 75, 100])
        print("\nPerson" + str(i) + ' = Rs.' + str(ticket))
        balance = balance + ticket
        print("Account Balance = Rs." + str(balance))
        denomination.append(ticket)
        print("Denomination : " + str(denomination))

        if ticket == 25:
            ticketed = ticketed+1
            print("$$Ticket Confirmed$$\nTickets Sold : " + str(ticketed))

            if denomination.count(25) > 1 and waitList75Flag:
                ticketed = ticketed + 1
                print("$$Ticket Confirmed for Wait List$$\nTickets Sold : " + str(ticketed))
                denomination.remove(25)
                denomination.remove(25)
                balance = balance - 50
                print("Updated Account Balance = Rs." + str(balance))
                print("Updated Denomination : " + str(denomination))
                waitList = waitList-1
                print("Updated Waiting List : " + str(waitList))
                waitList75 = waitList75-1
                if waitList75 == 0:
                    waitList75Flag = False

            if denomination.count(25) > 2 and waitList100Flag:
                ticketed = ticketed + 1
                print("$$Ticket Confirmed for Wait List$$\nTickets Sold : " + str(ticketed))
                denomination.remove(25)
                denomination.remove(25)
                denomination.remove(25)
                balance = balance - 75
                print("Updated Account Balance = Rs." + str(balance))
                print("Updated Denomination : " + str(denomination))
                waitList = waitList-1
                print("Updated Waiting List : " + str(waitList))
                waitList100 = waitList100-1
                if waitList100 == 0:
                    waitList100Flag = False

        elif ticket == 75 and (denomination.count(25) > 1 or waitList100Flag):

            if denomination.count(25) > 1:
                ticketed = ticketed + 1
                print("$$Ticket Confirmed$$\nTickets Sold : " + str(ticketed))
                denomination.remove(25)
                denomination.remove(25)
                balance = balance - 50
                print("Updated Account Balance = Rs." + str(balance))
                print("Updated Denomination : " + str(denomination))
            else:
                waitList = waitList+1
                waitList75Flag = True
                waitList75 = waitList75 + 1
                print("Waiting List!!!\nTotal Waiting List : " + str(waitList))

            if waitList100Flag:
                ticketed = ticketed + 1
                print("$$Ticket Confirmed for Wait List$$\nTickets Sold : " + str(ticketed))
                denomination.remove(75)
                balance = balance - 75
                print("Updated Account Balance = Rs." + str(balance))
                print("Updated Denomination : " + str(denomination))
                waitList = waitList-1
                print("Updated Waiting List : " + str(waitList))
                waitList100 = waitList100-1
                if waitList100 == 0:
                    waitList100Flag = False

        elif ticket == 100 and 75 in denomination:
            ticketed = ticketed + 1
            denomination.remove(75)
            balance = balance-75
            print("$$Ticket Confirmed$$\nTickets Sold : " + str(ticketed))
            print("Updated Account Balance = Rs." + str(balance))
            print("Updated Denomination : " + str(denomination))

        elif ticket == 100 and denomination.count(25) > 2:
            ticketed = ticketed + 1
            denomination.remove(25)
            denomination.remove(25)
            denomination.remove(25)
            balance = balance - 75
            print("$$Ticket Confirmed$$\nTickets Sold : " + str(ticketed))
            print("Updated Account Balance = Rs." + str(balance))
            print("Updated Denomination : " + str(denomination))

        else:
            waitList = waitList+1
            if ticket == 75:
                waitList75Flag = True
                waitList75 = waitList75+1
            elif ticket == 100:
                waitList100Flag = True
                waitList100 = waitList100+1
            print("Waiting List!!!\nTotal Waiting List : " + str(waitList))

    finalWaitList = waitList75 + waitList100
    print("\nSTATUS\nTotal No. of Tickets Sold : " + str(ticketed))
    print("Total No. of Wait Listed People : " + str(finalWaitList))
    print("\nFinal Account Balance = Rs." + str(balance))

else:
    print("These many people cannot be accommodated. Maximum is 20")
