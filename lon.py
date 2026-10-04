import random
so_ki_tu= int(input("so ki tu"))
so= "01234567989"
chu="abcdifg"
dac_biet="!@#$%^&*"
tat_ca=so+chu+dac_biet
ki_tu=[random.choice(so),random.choice(chu),random.choice(dac_biet)]
for _ in range(so_ki_tu - 3):
    ki_tu.append(random.choice(tat_ca))
opt="".join(ki_tu)
print(opt)