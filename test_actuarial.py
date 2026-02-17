from actuarialmath import Actuarial
import math

result = Actuarial.solve(
    fun=lambda x: 1 - math.exp(-x),
    target=0.5,
    grind=[0, 2]
) # irl use- "what interest rate gives a certain present value or What mortality rate produces a specific probability?"


print(f"Solve result: {result}")

actuarial = Actuarial() # create instance of Acturial class

def as_term(t):
    return "WHOLE_LIFE" if t == Actuarial.WHOLE else t
#insurance that last for a whole life, 5 = 5 years of coverage, converts numbers to displayable names

for a,b in [(5, Actuarial.WHOLE),(Actuarial.WHOLE,-1),(3,2),(1,-1)]:
    result = actuarial.add_term(a,b)
    print(f"{as_term(a)}+{as_term(b)}={as_term(result)}")
#Combines policys and adjust coverage periods

print(f"\nWHOLE_LIFE constant={Actuarial.WHOLE}")
