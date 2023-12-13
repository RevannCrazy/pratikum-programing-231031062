import os
def judul():
    print('Program menghitung volume dan luas permukaan'.center(45))
    print('Bangun ruang balok'.center(45))
    print()

def inputan():
    p   = float(input('Masukkan panjang:'))
    l   = float(input('Masukkan Lebar:'))
    t   = float(input('Masukkan Tinggi:'))
    return p,l,t

def hitung(p,l,t):
    vol =p*l*t
    luas_surf = 2*(p*l*t + p*l)
    luas_non_tutup = luas_surf - p*l
    return vol,luas_surf,luas_non_tutup

def tampilan(pesan,nilai):
    print(f'Nilai {pesan} : {nilai}')


def pilihan():
    pilih = input('Apakah lanjutkan [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Terimah Kasih!!')
    return a

def main():
    os.system('cls') 
    judul()                                         #judul
    p,l,t = inputan()                               #inputan
    vol,luas_surf,luas_non_tutup = hitung(p,l,t)    #Hitung
    #tampilan
    tampilan ('volume',vol)
    tampilan ('Luas permukaan',luas_surf)
    tampilan ('Luas permukaan tanpa tutup',luas_non_tutup)
    a = pilihan()                                   #pilihan
    return a

a =True
while a:
    a = main()