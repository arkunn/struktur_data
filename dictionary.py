data_siswa = {'nama':'bejo',
        'UTS':80, 
        'UAS':80, 
        'lulus':True, 
        'hobi':['maen','belajar']}
data_tambahan = {'bidang minat':'data science',
        'bahasa pemrogaraman':'python'}


print (f'data siswa: {data_siswa}')
print (f'data tambahan: {data_tambahan}')
# menggabungkan dictionary
data_gabungan = {**data_siswa, **data_tambahan}
print (data_siswa['nama'])
print (data_siswa.get('UTS'))
print (data_siswa.get('alamat', 'data tidak di temukan'))

# mengambil key dan value
daftar_kunci = data_siswa.keys()
daftar_nilai = data_siswa.values()

daftar_kunci_nilai = data_siswa.items()
for k, v in daftar_kunci_nilai:
	print (f'{k} = {v}')

# merubah nilai value dictionary
data_siswa['UTS'] = 70
print (f'data siswa: {data_siswa}')
# menambahkan  key dan value
data_siswa['gender'] = 'Lelaki'
data_siswa.update({'nama':'Tejo', 'UTS':100, 'Program studi':'sistem inforamsi'})
print (f'data siswa: {data_siswa}')

# menghapus item dictionary
#data_siswa.pop('UAS')
data_pop = data_siswa.pop('alamat', 'nilai tidak di temukan')
print (f'data hasil pop: {data_pop}')
print (f'hasil penggabungan:{data_gabungan}')


