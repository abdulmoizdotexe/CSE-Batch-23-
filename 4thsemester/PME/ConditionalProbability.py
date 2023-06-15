print("In Communication Systems, 0s have Probability of 1-p while 1s have probability of p. In case of error E is denoted while 1-E is denoted in case of Success.")

PAoBo = "(1-E)"
PA1Bo = "(E)"
PAoB1 = "(E)"
PA1B1 = "(1-E)"
PBo = "(1-P)"
PB1 = "(P)"

print(f"P(AonBo) = {(PAoBo)+(PBo)}") #it is multiplying but in case of strings it was not possible so, to write them together we added them.
print(f"P(AonB1) = {(PAoB1)+(PB1)}")
print(f"P(AonBo) = {(PA1B1)+(PB1)}")
print(f"P(AonBo) = {(PA1Bo)+(PBo)}")
