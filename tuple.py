tupleku = (40,50,10,30,50,60,90)
print (f"tupleku:{tupleku}")
tuplemu = (54, 7.4, False, 'Hello world', [32,'xyz'])
print (f'tuplemu:{tuplemu}')
print (f'mengambil tuple berdasarkan index ke 3: {tupleku[2]}')
print (f'mengambil tuple dari belakang dengan index 2: {tupleku[-2]}')
print (f'mengambil tuple dengan blank: {tupleku[4:]}')

tuple_gabung = tupleku + tuplemu
print (f'hasil penggabungan: {tuple_gabung}')
