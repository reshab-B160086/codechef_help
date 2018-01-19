t1 = int(raw_input())

while t1!=0:
      a=0
      n,k = map(int,raw_input().split())
      c =0   
      e=0
      for i in range(0,n):
        t,d = map(int,raw_input().split())
        if k!=0 and e == 0:
          k = k-t
          if  c == 0 and k==0:
              
             c=1
          elif c == 1 :
               a = a+t*d
          elif k < 0:
               e = 1
               a = a+(t+k)*d
        else:
             a=a+t*d
      print a 
      t1 -=1
