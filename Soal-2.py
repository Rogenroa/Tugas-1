Jari_jari_lingkaran = int(input("Jari-jari lingkaran : "))
Py = float(22 / 7)
Luas_Lingkaran = Py*Jari_jari_lingkaran*Jari_jari_lingkaran
Format_Luas_Lingkaran = "{:.2f}".format(Luas_Lingkaran)

print("Luas lingkaran dengan jari-jari " + str(Jari_jari_lingkaran) + " cm adalah " + (str(Luas_Lingkaran) + " cm\u00b2"))
#print(str(Luas_Lingkaran) + " cm\u00b2")
print("Luas lingkaran dengan jari-jari " + str(Jari_jari_lingkaran) + " cm adalah " + (str(Format_Luas_Lingkaran) + " cm\u00b2"))
