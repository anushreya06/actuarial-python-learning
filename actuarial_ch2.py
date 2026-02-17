from actuarialmath import Interest
#import describe


interest = Interest(i=0.05)
#set annual interest rate to i

print("Different interest rate froms:")
print(interest.d,interest.v,interest.delta,interest.i)
#calcuates all the different interest types and prints it

print()
print("Convert delta to other forms:")
delta = 0.05

#mthly static method: converts between annual and mothly pay interest in any form
i = Interest(delta=delta).i  # convert to annual interest rate
d = Interest(delta=delta).d  # convert to annual discount rate
i_m = Interest.mthly(d=d ,m=12)  # convert to annual interest rate mothly pay
d_m = Interest.mthly(d=d,m=12)  # same but discount rate

print('Continuously-compounded annual rate of interest:', delta)
print(' Convert to annual interest rate:', i)
print(' Convert to annual discount rate:', d)
print(' Convert to annual interest rate (monthly-pay):', i_m)
print(' Convert to annual discount rate (monthly-pay):', d_m)
print()
print("Annuity calculations:")

import matplotlib.pyplot as plt
t = range(100)
plt.plot(t,[interest.annuity(t=s,due=True) for s in t]) #calcuates annuity for each item
plt.title(f'Present Value of Annuity Certain Due (i={interest.i * 100}%)') #makes graphs,sets interest rate as percentages
plt.xlabel('Period (years)')
plt.ylabel('Annuity Due Factor')
print('Annuity Factors By Payment Frequency (perpetual, i=5%):')




print('1. Immediate:', interest.annuity(t=Interest.WHOLE, due=False))
print('2. Immediate (quarterly pay): ', interest.annuity(t=Interest.WHOLE, m=4, due=False))
print('3. Continuous:       ', interest.annuity(t=Interest.WHOLE, m=0))
print('4. Due (quarterly pay):       ', interest.annuity(t=Interest.WHOLE, m=4, due=True))
print('5. Due:              ', interest.annuity(t=Interest.WHOLE, due=True))
#call annuity parameter,sets the time/due date, then sets when the payment starts or ends, based on the t(start), f(end)

print("SOA Question 3.10:  (C) 0.86")
interest = Interest(v=0.75)
L = 35 * interest.annuity(t=4, due=False) + 75 * interest.v_t(t=5)
interest = Interest(v=0.5)
R = 15 * interest.annuity(t=4, due=False) + 25 * interest.v_t(t=5)
print(L/(L+R))

print("SOA Claude Question")
interest = Interest(v=0.70)
S = 40 * interest.annuity(t=4, due=False) + 120 * interest.v_t(t=5)
interest = Interest(v=0.80)
P = 25 * interest.annuity(t=4, due=False) + 80 * interest.v_t(t=5)
print(S/(S+P))



