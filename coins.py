# name of student: Daniel Bos
# number of student: 99069008
# purpose of program: calculate change 
# function of program: calculate change
# structure of program:

toPay = int(float(input('Amount to pay: '))* 100) # ask amount to be payed and convert it to cents
payed = int(float(input('Payed amount: ')) * 100) # ask amount you already payed and convert it to cents
change = payed - toPay # find the change you still need to get back
payed = []

if change > 0: # if there is change to be payed execute this
  coinValue = 500 # a value gets added to start the if-tree
  
  while change > 0 and coinValue > 0: # execute while change and coinvalue is still greater than 0
    nrCoins = change // coinValue # number of coins gets calculated

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # print the maximum coins you can give
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # asks how many coins of the value you returned
      change -= nrCoinsReturned * coinValue # calculates the change after the said value has been retracted from the total

      if coinValue >= 100:
        payed.append("U heeft {} muntjes van {} euro betaalt".format(nrCoinsReturned,int(coinValue/100)))
      else:
        payed.append("U heeft {} muntjes van {} cent betaalt".format(nrCoinsReturned,coinValue))
        

# comment on code below:
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200 
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # if the change is still greater than 0, the program will tell you the amount you didnt return yet
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
  for x in payed:
    print(x)