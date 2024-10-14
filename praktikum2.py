#No 1 Evaluate the student performance
Nilai = int(input("Masukan Nilai"))
if Nilai >=0:
    if Nilai >= 90:
        print ("Excellent performance")
    elif Nilai >= 80:
        print ("Very Good performance")
    elif Nilai >= 70:
        print ("Good performance")
    elif Nilai >= 60:
        print ("Average performance")
    else:
        print ("nice try ngab! belajar lagi")


#No 2 Menemukan bilangan terbesar dari tiga bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

terbesar = max(a,b,c)
         
print ("Bilangan terbesar = ", terbesar)


#No 3 Mencetak deret fibonacci hingga n
nilai_fibonacci = int(input('Masukan nilai fibonacci : '))
def fibonacci(n):
    a, b = 0,1
    hasil = []
    while a <= n:
        hasil.append(a)
        a, b = b, a + b
    return hasil

deret_fibonacci = fibonacci(nilai_fibonacci)
print("Deret Fibonacci hingga", nilai_fibonacci, "adalah:", deret_fibonacci)


#No 4 Mencetak odd numbers up to n
nilai= int(input("Masukkan nilai: "))
for i in range(1, nilai+1, 2):
    print(i)


#No 5 Mencetakan desain pola
nilai = int(input('Masukan nilai untuk tinggi pola: '))
for i in range(1, nilai + 1):  
    print(str(i) * i)