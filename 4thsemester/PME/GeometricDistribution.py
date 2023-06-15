import matplotlib.pyplot as plt

Ph = 0.6 #Probability of Heads
Pt = 0.4 #Probability of Tails

P1 = ((1-Ph)**(1-1))*Ph
P2 = ((1-Ph)**(2-1))*Ph
P3 = ((1-Ph)**(3-1))*Ph
P4 = ((1-Ph)**(4-1))*Ph
P = 1-(P1 + P2 + P3 + P4)

print(f"The probability by Geometric Distribution of Heads 4 times is: {P4}")
print(f"The probability by Geometric Distribution more than 4 times is: {P}")

pl = [P,P4]

plt.plot(pl , 'b-' , label = 'Geometric Distribution')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()