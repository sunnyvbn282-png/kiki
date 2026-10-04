import random
do_dai= int(input("độ dài mật khẩu"))
thuong = "abc"
hoa = "ABC"
so= "123"
dac_biet= "@$#!"
tat_ca= thuong+hoa+so+dac_biet
mk= [random.choice(thuong),random.choice(hoa),random.choice(so),random.choice(dac_biet)]
for _ in range(do_dai - 4):
    mk.append(random.choice(tat_ca))
random.shuffle(mk)
mat_khau="".join(mk)
print (mat_khau)

    