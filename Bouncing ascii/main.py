import os,time
a,b,c,d,e,n='+- |*\n'
w=d+c*18+d+n
s=a+b*18+a+n
x,y=0,0
g,h=17,7
j,k=1,1
while 1:
 if 0>x or x>g:j*=-1;x+=j
 if 0>y or y>h:k*=-1;y+=k
 os.system('cls');print (s+w*y+d+c*x+e+c*(g-x)+d+n+w*(h-y)+s);x+=j;y+=k;time.sleep(0.1)