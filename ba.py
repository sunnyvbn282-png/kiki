import random

so="0123456789"
opt=[]
for _ in range(6):
    opt.append(random.choice(so))
    
lon="".join(opt)
print (opt)