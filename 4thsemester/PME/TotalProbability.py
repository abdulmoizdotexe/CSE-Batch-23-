print("2 Black Balls and 3 White Balls. 2 Balls selected")

Pb1 = 2/5
Pw1 = 3/5
Pb2b1 = 1/4
Pw2b1 = 3/4
Pw2w1 = 2/4
Pb2w1 = 2/4

print(f"Initial Probability of Black balls: {Pb1}")
print(f"Initial Probability of White balls: {Pw1}")
print(f"After removal of Black Ball, the remaining Black Balls: {Pb2b1}")
print(f"After removal of Black Ball, the remaining White Balls: {Pw2b1}")
print(f"After removal of White Ball, the remaining Black Balls: {Pb2w1}")
print(f"After removal of White Ball, the remaining White Balls: {Pw2w1}")

TP = (Pw2b1*Pb1) + (Pb2w1*Pw1)

print(f"The Total Probability is: {TP}")