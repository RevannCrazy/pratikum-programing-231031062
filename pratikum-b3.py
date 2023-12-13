print ('pratikum-3\n\n')
print('Nama lengkap : MUH REVAN')
print('NIM          : 231031062')
print('prodi        : Sistem informasi')

######################
a = True
b = False

print ('\n==========NAND==========')
hasil = not (a and a)
print(a,'nand',a,'adalah =',hasil)
hasil = not (a and b)
print(a,'nand',b,'adalah =',hasil)
hasil = not (b and a)
print(b,'nand',a,'adalah =',hasil)
hasil = not (b and b)
print(b,'nand',b,'adalah =',hasil)

print ('\n==========NOR==========')
hasil = not (a or a)
print(a,'nor',a,'adalah =',hasil)
hasil = not (a or b)
print(a,'nor',b,'adalah =',hasil)
hasil = not (b or a)
print(b,'nor',a,'adalah =',hasil)
hasil = not (b or b)
print(b,'nor',b,'adalah =',hasil)

print ('\n==========NXOR==========')
hasil = not (a ^ a)
print(a,'nxor',a,'adalah =',hasil)
hasil = not (a ^ b)
print(a,'nxor',b,'adalah =',hasil)
hasil = not (b ^ a)
print(b,'nxor',a,'adalah =',hasil)
hasil = not (b ^ b)
print(b,'nxor',b,'adalah =',hasil)

#INI OPERATOR MEMBERSHIP
print ('\n========== IN ==========')
nama = 'Revan'

test = 'va' #Ise dengan 2 huruf yang ada di nama
cek = test in nama 
print (test,'ada di',nama,'adalah=',cek)

test = 'av' #Ise dengan 2 huruf yang ada di nama
cek = test in nama 
print (test,'ada di',nama,'adalah=',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'
print('\n==========IN==========')
cek = test1 in nama 
print (test1,'ada di',nama,'adalah=',cek)

cek = test2 in nama 
print (test2,'ada di',nama,'adalah=',cek)

cek = test3 in nama 
print (test3,'ada di',nama,'adalah=',cek)

cek = test4 in nama 
print (test4,'ada di',nama,'adalah=',cek)

cek = test5 in nama     
print (test5,'ada di',nama,'adalah=',cek)
#Tugas lanjutkan kode
#dengan cara yang sama buat operator not in

print('\n==========NOT IN==========')
cek = not(test1 in nama) 
print (test1,'ada di',nama,'adalah=',cek)

cek = not(test2 in nama) 
print (test2,'ada di',nama,'adalah=',cek)

cek = not(test3 in nama) 
print (test3,'ada di',nama,'adalah=',cek)

cek = not(test4 in nama) 
print (test4,'ada di',nama,'adalah=',cek)

cek = not(test5 in nama) 
print (test5,'ada di',nama,'adalah=',cek)

# INI operator BTWISE
print('\n')
a = 7
b = 4
a += 60
b += 80
print ('==========AND==========')
print('Nilai',a,'biner adalah       =',format(a,'08b'))
print('Nilai',b,'biner adalah       =',format(b,'08b'))
print('-----------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'biner adalah  =',format (c,'08b'))

print ('==========OR==========')
#Tugas buat untuk OR
print('Nilai',a,'biner adalah       =',format(a,'08b'))
print('Nilai',b,'biner adalah       =',format(b,'08b'))
print('-----------------------------------------AND')
c = a | b
print('Nilai',a,'|',b,'biner adalah  =',format (c,'08b'))

print ('==========XOR==========')
#Tugas buat untuk xOR
print('Nilai',a,'biner adalah       =',format(a,'08b'))
print('Nilai',b,'biner adalah       =',format(b,'08b'))
print('-----------------------------------------AND')
c = a ^ b
print('Nilai',a,'^',b,'biner adalah  =',format (c,'08b'))

print ('\n==========NOT==========')
c = ~a
print('Nilai',a,'biner adalah       =',format(a,'09b'))
print('Nilai not',a,'biner adalah   =',format(c,'09b'))
#Tugas lanjutkan untuk not b
c = ~b
print('Nilai',b,'biner adalah       =',format(a,'09b'))
print('Nilai not',b,'biner adalah   =',format(c,'09b'))

print('\n==========left shift==========')
c = a << 2
print('Nilai',a,'biner adalah         =',format(a,'09b'))
print('Nilai not',a,'<<biner adalah   =',format(c,'09b'))
c = b << 2
print('Nilai',b,'biner adalah         =',format(b,'09b'))
print('Nilai not',b,'<< biner adalah  =',format(c,'09b'))

print('\n==========Right shift==========')
c = a >> 2
print('Nilai',a,'biner adalah         =',format(a,'09b'))
print('Nilai not',a,'>>biner adalah   =',format(c,'09b'))
c = b >> 2
print('Nilai',b,'biner adalah         =',format(b,'09b'))
print('Nilai not',b,'>> biner adalah  =',format(c,'09b'))

print('=========NOT AND=========')
#Tugas buat untuk NAND
print('Nilai',a,'biner adalah            =',format(a,'08b'))
print('Nilai',b,'biner adalah            =',format(b,'08b'))
print('-----------------------------------------AND')
c = ~(a & b)
print('Nilai',a,'not and',b,'biner adalah  =',format (c,'08b'))
print('=========NOT OR=========')
#Tugas buat untuk NOR
print('Nilai',a,'biner adalah       =',format(a,'08b'))
print('Nilai',b,'biner adalah       =',format(b,'08b'))
print('-----------------------------------------AND')
c = ~(a | b)
print('Nilai',a,'not or',b,'biner adalah  =',format (c,'08b'))
print('=========NOT XOR=========')
#Tugas buat untuk NXOR
print('Nilai',a,'biner adalah       =',format(a,'08b'))
print('Nilai',b,'biner adalah       =',format(b,'08b'))
print('-----------------------------------------AND')
c = ~(a ^ b)
print('Nilai',a,'not xor',b,'biner adalah  =',format (c,'08b'))
print('\n=========NOT << 2=========')
#Tugas buat untuk c= ~(a<<2)
print('Nilai',a,'biner adalah       =',format(a,'08b'))
print('Nilai',b,'biner adalah       =',format(b,'08b'))
print('-----------------------------------------AND')
c = ~(a << 2)
print('Nilai',a,'not <<',2,'biner adalah  =',format (c,'08b'))

print('\n=========NOT >> 2=========')
print('Nilai',a,'biner adalah       =',format(a,'08b'))
print('Nilai',b,'biner adalah       =',format(b,'08b'))
print('-----------------------------------------AND')
c = ~(a >> 2)
print('Nilai',a,'not >>',2,'biner adalah  =',format (c,'08b'))
#Tugas buat untuk c= ~(a>>2)
#Tugas buat untuk c= ~(b>>2)