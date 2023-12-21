inp = input('Masukan suatu input: ')

if len(inp) != 3:
    print('Panjang string', len(inp),'tidak sama dengan 3')

else:
    print('Panjang input sesuai yang diinginkan')

print()
nilai = int(input('Masukan nilai: '))

if nilai >= 90:
    print('Nilai Anda Adalah: A')
elif nilai > 75:
    print('Nilai Anda Adalah: B')
elif nilai > 55:
    print('Nilai Anda Adalah: C')
else:
    print('Nilai Anda Adalah: D')