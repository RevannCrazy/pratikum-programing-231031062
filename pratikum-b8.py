import os
os.system('cls')

pwd_benar = 'si23b'
a = True
i = 0
limit = 3
while a:
    i += 1
    pwd = input('Masukkan password:')
    if pwd == pwd_benar:
        print ('Selamat anda login!')
        a = False
    else:
        print ('password salah')
        if i == limit:
            a = False
            print ('Anda kehabisan kesempatan')
        else:
            print (f'Kesmpatan anda tersisa {limit-i} kali')