import matplotlib.pyplot as plt

S = [0,1,2,3]
C = [1/8,3/8,3/8,1/8]
Ex = (S[0]*C[0]) + (S[1]*C[1]) + (S[2]*C[2]) + (S[3]*C[3])
Ex2 = Ex**2
EX = ((S[0]**2)*C[0]) + ((S[1]**2)*C[1]) + ((S[2]**2)*C[2]) + ((S[3]**2)*C[3])

print(f"The probability of 3 coins is: {S}")
print(f"The Value of E(x) is: {Ex}")
print(f"The Value of [E(x)]^2 is: {Ex2}")
print(f"The Value of E(x)^2 is: {EX}")

var = EX - Ex2

print(f"The VAR[x] is: {var}")

plt.plot(var, 'r-' , label = 'Variance')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()