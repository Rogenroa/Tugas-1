a = float(input("Ujian Teori : "))
b = float(input("Ujian Praktek: "))

#a = Ujian Teori
#b = Ujian Praktek

if a >= 70 and b >= 70:
    print("Selamat, anda lulus!")
elif a >= 70 and b < 70:
    print("Anda harus mengulang ujian praktek")
elif a < 70 and b >= 70:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda tidak lulus")