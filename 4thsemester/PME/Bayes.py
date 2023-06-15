print("55% of adults are male and 10% of male use Credit cards, while 45% are female and 2% of female use Credit cards")

Pcm = 10/100
Pm = 55/100
Pcf = 2/100
Pf = 45/100

PC = (Pcm*Pm) + (Pcf*Pf)
PMC = (Pcm * Pm)/PC

print(f"The Probability of Male Adults after Bayes Law is: {PMC}")