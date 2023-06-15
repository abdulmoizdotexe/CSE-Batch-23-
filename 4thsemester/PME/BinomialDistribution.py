import matplotlib.pyplot as plt

print("For 3 tosses of a coin, we have S = [0,1,2,3]")

P = 0.4
Q = 1-P

Px0 = (P**0)*(Q**3)
Px1 = (P**1)*(Q**2)
Px2 = (P**2)*(Q**1)
Px3 = (P**3)*(Q**0)

print(f"for P(x = 0): {Px0}")
print(f"for P(x = 1): {Px1}")
print(f"for P(x = 2): {Px2}")
print(f"for P(x = 3): {Px3}")

PX = [Px0 , Px1 , Px2 , Px3]

plt.plot(PX , 'r-' , label = 'Binomial Distribution')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()