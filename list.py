listku = [20,40,50,10,80,50,30,40,70]
print (f'listku: {listku}')
print (f'mengambil listku berdasarkan index: {listku[-2]}')
print (f'slicing: {listku[2:5]}')
print (f'slicing dengan blank start:{listku[:5]}')
print (f'slicing dengan blank start: {listku[4:]}')
print (f'slicing dengan  3 parameter: {listku[2:8:2]}')

print ("\n")
listmu = [70,3.5,True, "Hello world",[10,'abc']]
print (f'listmu: {listmu}')
print ("----mengubah list----")
listmu[2] = 'berubah'
print (f'listmu:{listmu}')
print ("\n")
print ("----menambahkan list----")
listmu.append('data baru')
print (f'listmu:{listmu}')
print ("\n")
print ("----POP----")
var_tmp  = listmu.pop()
print (f'listmu:{listmu}')
print (f'var_tmp: {var_tmp}')
print ('\n')
print ("----menghapus list----")
listmu.remove(70)
print (f"listmu:{listmu}")

print ('\n')
print("---menggabungkan list----")
list_gabung = listku + listmu
print (f"hasil penggabungan:{list_gabung}")

