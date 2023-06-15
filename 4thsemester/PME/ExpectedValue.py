import matplotlib.pyplot as plt
Sy = [-3,-1,1,3]
Px = 1/4
print(f"The expected value at -3 is {((2*(Sy[0])+10)**2)*Px}")
print(f"The expected value at -1 is {((2*(Sy[1])+10)**2)*Px}")
print(f"The expected value at 1 is {((2*(Sy[2])+10)**2)*Px}")
print(f"The expected value at 3 is {((2*(Sy[3])+10)**2)*Px}")

Sx = [((2*(Sy[0])+10)**2)*Px,((2*(Sy[1])+10)**2)*Px,((2*(Sy[2])+10)**2)*Px,((2*(Sy[3])+10)**2)*Px]

plt.plot(Sy, 'b-', label='Original') # b- stands for solid blue line
plt.plot(Sx, 'r-', label='Expected')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

plt.show()