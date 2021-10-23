nama = input('Masukkan nama anda: ')
tahun_lahir = input('Masukkan tahun kelahiran anda: ')
tahun_lahir = int(tahun_lahir)
if tahun_lahir > 1944 and tahun_lahir <= 1964:
  print(nama,'berdasarkan tahun lahir maka anda tergolong generasi Baby Boomer')
elif tahun_lahir > 1964 and tahun_lahir <= 1979:
  print(nama,'berdasarkan tahun lahir maka anda tergolong generasi X')
elif tahun_lahir > 1979 and tahun_lahir <= 1994:
  print(nama,'berdasarkan tahun lahir maka anda tergolong generasi Y (Millenials)')
elif tahun_lahir > 1994 and tahun_lahir <= 2015:
  print(nama,'berdasarkan tahun lahir maka anda tergolong generasi Z')
else:
  print('Tahun lahir anda di luar range yang tersedia')