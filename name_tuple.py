from collections import namedtuple

Barang = namedtuple('Barang',['nama_barang','harga_jual','garansi_vendor']) #bisa menggunakan tuple atau list
barang1 = Barang('keyboard',500, True)
print (f'barang1: {barang1}')
barang2 = Barang(garansi_vendor=False, harga_jual=80, nama_barang='mouse')
print (f'barang2: {barang2}')
# mengambil name tuple berdasarkan index
#print (barang1[1])
# mengambil name tuple berdasarkan nama
print (f'{barang1.nama_barang} : {barang1.harga_jual} ribu rupiah')


print ('\n')




