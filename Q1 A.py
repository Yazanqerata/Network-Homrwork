l1=['HTTP','HTTPS','FTP','DNS']
l2=[80,443,21,53]
d=dict()
for k,v in zip(l1,l2):
    d[k]=v
print(d)