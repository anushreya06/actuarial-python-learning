import math
from actuarialmath import Life
#import describe

#describe.methods(Life)


print(Life.bernoulli(p=0.5,a=0,b=1), Life.bernoulli(p=0.5, a=0, b=1, variance=True))
#p = probailty of getting value a, a= first pssible value, b = 2nd possible value, 2 exact outcomes
print(Life.binomial(p=0.5, N=100), Life.binomial(p=0.5, N=100, variance=True))
#p = each trials success rate, n = number of independent trials return mean, return varinace: , ex, 100 ppl 50% death --> how many die total?

print(Life.mixture(p=0.5, p1=0.3, p2=0.4, N=100),
      Life.mixture(p=0.5, p1=0.3, p2=0.4, N=100, variance=True))
#p = probailty of being in group 1, p1= group 1 success rate, p2 = group 2 success rate, n= total number or people, ex. smokers vs non somkers in a life insurance pool

Life.portfolio_cdf(mean=0, variance=1, N=50, value=5)
#ex. "what is the probability our total claims/losses stay below a certain amount"

Life.portfolio_percentile(mean=0, variance=1, N=50, prob=0.76)
#ex. what value will the total be below X% of the time?

Life = Life().set_interest(i=0.05)
Life.interest.delta

print("SOA Question 2:2:(D) 400")
p1=(1. - 0.02) * (1. - 0.01)
p2 = (1. - 0.02) * (1. - 0.02)
print(math.sqrt(Life.conditional_variance(p=.2, p1=p1, p2=p2, N=100000)))
print(math.sqrt(Life.mixture(p=.2, p1=p1, p2=p2, N=100000, variance=True)))

print("Claude practice problem 1")
print(math.sqrt(Life.binomial(p=0.03,N=10000),Life.binomial(p=0.03, N=10000),variance=True))

print("Claude practice problem 2")
print(Life.binomial(p=0.95, N=50000, varinace=True))


