import random
thuong = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
hoa = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
dac_biet="!@#$%^&*"
so="0123456789"
tat_ca= thuong+hoa+dac_biet+so
do_dai= int(input("do dai:"))
if do_dai<8:
    print("cần in ra ít nhất 8 kí tự")
else:
    print("độ dài hợp lệ, bắt đầu tạo mật khẩu...")
    mk=[random.choice(thuong),random.choice(hoa),random.choice(dac_biet)]
    for i in range(do_dai-4): 
        mk.append(random.choice(tat_ca))
        random.shuffle(mk)
        print("".join(mk))