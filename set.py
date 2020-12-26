s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}

# menggabungkan set
set_gabungan = s1.union(s2,s3)
#print (f'hasil penggabungan: {set_gabungan}')

# irisan set
set_irisan = s1.intersection(s2, s3)
#set_irisan = s1.intersection(s2)
print (f'hasil irisan: {set_irisan}')

# selisih
#set_selisih = s1.difference(s2)
set_selisih = s1.difference(s2,s3)
print  (f'hasil selisih: {set_selisih}')

# setangkup
beda_setangkup = s1.symmetric_difference(s2)
print (f'beda setangkup: {beda_setangkup}')
