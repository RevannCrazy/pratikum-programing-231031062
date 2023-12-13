import os
a = True

while a:
    jawab = input('Apakah ingin melanjutkan? (y/n)')
    if jawab == 'y':
        print ('selamat datang lagi!')
        a = True
    elif jawab == 'n':
        print ('Sampai ketemu lagi :D')
        a = False
    else:
        os.system('cls')
        print ('Jangan aneh-aneh deh :,)')
        a = True