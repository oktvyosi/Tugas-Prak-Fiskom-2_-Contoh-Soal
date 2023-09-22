# Benda bermassa 2 kg bergerak secara beraturan dalam lintasan melingkar berjari-jari 0,5 m dengan kecepatan 4 m/s. Perhatikan pernyataan berikut.
# Berapa gaya sentripetalnya 
# Berapa percepatan sentripetalnya 
# berapa kecepatan sudutnya 

# menentukan variabel
m = 2
R = 0.5 
v = 4 

#menghitung percepatan sentripetal
a = v**2 / R

print("percepatan sentripetal", a, "m/s^2")

#menghitung gaya sentripetal
Fsp = m * a

print("gaya sentripetal", Fsp, "Newton")

#menghitung kecepatan sudut
omega = v / R

print("kecepatan sudut", omega, "rad/s")
