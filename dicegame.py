import random
total=500
print('Your total is:', total)
while True:
  while total>0:
    bet=int(input('Place your bet: '))
    if bet<0:
      print('The bet must be positive.')
    elif bet>total:
      print('You dont have enough money, your balance is:', total)
    else:
      break

  total=total-bet
  print('Your balance is:', total)
  nt1=int(input('Choose a number from 1 to 6: '))
  nt2=int(input('Choose a number from 1 to 6: '))
  n1=random.randint(1, 6)
  n2=random.randint(1, 6)
  print('The numbers are:', n1, 'and', n2)
  if ((nt1==n1 and nt2==n2) or (nt1==n2 and nt2==n1)):
    print('You won!')
    total=total+(bet*2)
  elif (nt1+nt2==n1+n2):
    total = total + bet
  else:
    print('You lost!')
    print('The winning numbers are:', n1, ',', n2)
    print('Your total is:', total)
  if total == 0:
    print('You lost all your money, fool!')
    break
