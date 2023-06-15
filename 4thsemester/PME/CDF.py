import matplotlib.pyplot as plt

print("For a Fair Dice we have 6 outcomes")
Fx = 1/6
print(f"For each Number the probabiltity is 1/6")

Fx1 = Fx
Fx2 = Fx + Fx
Fx3 = Fx + Fx + Fx
Fx4 = Fx + Fx + Fx + Fx
Fx5 = Fx + Fx + Fx + Fx + Fx
Fx6 = Fx + Fx + Fx + Fx + Fx + Fx

print(f"For x <= 1: {Fx1}")
print(f"For x <= 2: {Fx2}")
print(f"For x <= 3: {Fx3}")
print(f"For x <= 4: {Fx4}")
print(f"For x <= 5: {Fx5}")
print(f"For x <= 6: {Fx6}")

pl = [Fx1 , Fx2 , Fx3 , Fx4 , Fx5 , Fx6]
plt.plot(pl , 'b-' , label = 'CDF')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

plt.show()