a=input ("enter the matrix A:")
b=input ("enter the matrix B:")
p=len(a)
q=len(a[0])
m=len(b)
n=len(b[0])
c=[]
for i in range (p):
	if (q!=m):
		break
	d=[]
	for j in range (n):
		s=0
		for l in range(m):
			s=s+(a[i][l]*b[l][j])
		d.append(s)
c.append(d)
if (q!=m):
	print ("multiplication can't be done")
else:
	print c

