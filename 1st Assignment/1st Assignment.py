from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import math

#___________erotima 1_____________

#dimiourgia periodikis palmoseiras

fm=7000
ftr=fm/2
tm=1/fm
A=2
time = np.linspace(0, 4*tm, 500000, endpoint = False)
sq_triangle = (A * signal.sawtooth(2 * np.pi * ftr * time,0.5))**2
plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Τετράγωνο τριγωνικής περιοδικής παλμοσειράς')
plt.grid()
plt.plot(time, sq_triangle);
plt.show()

#____a____
cycles=4


#__i__ fs1=25fm
fs1=25*fm
ts1=1/fs1

t1 = np.arange(0,cycles*tm,ts1)
sq_triangle1 = (A * signal.sawtooth(2 * np.pi * ftr * t1,0.5))**2

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs1')
plt.plot(t1, sq_triangle1, 'ko');
plt.grid()
plt.show()


#__ii__ fs2=60fm
fs2=60*fm
ts2=1/fs2

t2 = np.arange(0,cycles*tm,ts2)
sq_triangle2 = (A * signal.sawtooth(2 * np.pi * ftr * t2,0.5))**2

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs2')
plt.plot(t2, sq_triangle2, 'co');
plt.grid()
plt.show()



#__iii__ κοινό διάγραμμα
plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας σε κοινό άξονα')
plt.plot(t2, sq_triangle2, 'co', t1, sq_triangle1, 'ko');
plt.grid()
plt.show()




#____b____
#fs=5fm
fs=5*fm
ts=1/fs

t3=np.arange(0,cycles*tm,ts)
sq_triangle3 = (A * signal.sawtooth(2 * np.pi * ftr * t3,0.5))**2


plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs=5fm')
plt.grid()
plt.plot(t3, sq_triangle3, 'co');
plt.show()




#____c____

#__i__
A=1
cycles=4
time = np.linspace(0, cycles*tm, 500000, endpoint = False)
z = A * np.sin(2 * np.pi * fm * time)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Ημιτονική παλμοσειρά z(t)')
plt.grid()
plt.plot(time, z);
plt.show()

#_i_a_i_ fs1=25fm
fs1=25*fm
ts1=1/fs1

t1=np.arange(0,cycles*tm,ts1)
z1 = A*np.sin(2*np.pi*fm*t1)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs1')
plt.grid()
plt.plot(t1, z1, 'ko');
plt.show()


#i_a_ii_ fs2=60fm
fs2=60*fm
ts2=1/fs2

t2=np.arange(0,cycles*tm,ts2)
z2 = A*np.sin(2*np.pi*fm*t2)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs2')
plt.plot(t2, z2, 'co');
plt.grid()
plt.show()


#i_a_iii κοινό διάγραμμα
plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας σε κοινό διάγραμμα')
plt.plot(t2, z2, 'co', t1, z1, 'ko')
plt.grid()
plt.show()


#i_b fs=5fm
fs=5*fm
ts=1/fs

t3=np.arange(0,cycles*tm,ts)
z3 = A*np.sin(2*np.pi*fm*t3)


plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs=5fm')
plt.grid()
plt.plot(t3, z3, 'co');
plt.show()



#__ii__
cycles=1

#de zititai
A=1
fL=1000
tL = 1/fL
time = np.linspace(0, 4*tm, 500000, endpoint = False)
q = z + A*np.sin(2*np.pi*(fm+fL)*time)


#ii_a_i fs1=25fm 
fs1=25*fm
ts1=1/fs1

t1=np.arange(0,cycles*tL,ts1)
z1 = A*np.sin(2*np.pi*fm*t1)
q1 = z1 + A*np.sin(2*np.pi*(fm+fL)*t1)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs1')
plt.plot(t1, q1, 'ko');
plt.grid()
plt.show()



#ii_a_ii fs2=60fm
fs2=60*fm
ts2=1/fs2

t2=np.arange(0,cycles*tL,ts2)
z2 = A*np.sin(2*np.pi*fm*t2)
q2 = z2 + A*np.sin(2*np.pi*(fm+fL)*t2)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs2')
plt.plot(t2, q2, 'co');
plt.grid()
plt.show()



#ii_a_iii 
#ta deigmata se koino diagramma
plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας σε κοινό διάγραμμα')
plt.plot(t2, q2, 'co', t1, q1, 'ko')
plt.grid()
plt.show()


#ii_b fs=5fm
fs=5*fm
ts=1/fs

t3=np.arange(0,cycles*tL,ts)
z3 = A*np.sin(2*np.pi*fm*t3)
q3 = z3 + A*np.sin(2*np.pi*(fm+fL)*t3)


plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs=5fm')
plt.plot(t3, q3, 'ko');
plt.grid()
plt.show()







#___________erotima 2_____________

fm=7000
ftr=fm/2
tm=1/fm
cycles=4
A=2
time = np.linspace(0, cycles*tm, 500000, endpoint = False)
sq_triangle = (A * signal.sawtooth(2 * np.pi * ftr * time,0.5))**2
plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Τετράγωνο τριγωνικής περιοδικής παλμοσειράς')
plt.grid()
plt.plot(time, sq_triangle);
plt.show()

fs1=45*fm
ts1=1/fs1

t1 = np.arange(0,cycles*tm,ts1)
sq_triangle1 = (A * signal.sawtooth(2 * np.pi * ftr * t1,0.5))**2

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Δείγματα δειγματοληψίας με fs1')
plt.plot(t1, sq_triangle1, 'ko');
plt.grid()
plt.show()


#____a____
#kvantisi 5 bits
n=5 #eukrinia kvantismou

#ypologismos vimatos kvantismou
d=(A**2-(-A**2))/(2**n-1)

#eksisosi mid-riser kvantisti
xq=d*np.floor(sq_triangle1/d)+d/2
error=xq-sq_triangle1


#from sympy.combinatorics.graycode import GrayCode
#a = GrayCode(5)

#list(a.generate_gray())
def gray_code(n):
    def gray_code_recurse (g,n):
        k=len(g)
        if n<=0:
            return

        else:
            for i in range (k-1,-1,-1):
                char='1'+g[i]
                g.append(char)
            for i in range (k-1,-1,-1):
                g[i]='0'+g[i]

            gray_code_recurse (g,n-1)

    g=['0','1']
    gray_code_recurse(g,n-1)
    return g
g = gray_code (n)



plt.figure()
plt.title("Έξοδος κβαντιστή")
plt.xlabel("Time (s)")
plt.ylabel('Επίπεδα κβαντισμού σε κώδικα Gray')
plt.legend(['kvantismeno sima'], bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0.)
plt.yticks(np.arange(0,len(g),4/30),g[1:32])
plt.grid()
plt.step(t1, xq)
plt.show()

#____b____
print('Τα 20 πρώτα δείγματα:')
print(sq_triangle1[:20])
print('Tα 20 πρώτα κβαντισμένα δείγματα:')
print(xq[:20])
print('Tα 20 πρώτα errors:')
print(error[:20])

#__i__
mo_10 = 0.
athr = 0
for i in range(10):
    athr = athr+error[i]
mo_10 = athr/10
athr = 0
for i in range(10):
    athr = athr+(error[i]-mo_10)**2
apoklisi_10 = math.sqrt(athr/9)
print('Τυπική απόκλιση για τα πρώτα 10 δείγματα=',apoklisi_10)

#__ii__
mo_20 = 0.
athr = 0
for i in range(20):
    athr = athr+error[i]
mo_20 = athr/20
athr = 0
for i in range(20):
    athr = athr+(error[i]-mo_20)**2
apoklisi_20=math.sqrt(athr/19)
print('Τυπική απόκλιση για τα πρώτα 20 δείγματα=',apoklisi_20)



#__iii__
Var_Q = (d**2)/12    #Gia f_Q(q) omoiomorfi katanomi puknotitas pithanotitas sto -D/2 ews D/2 me timi 1/D, E(q)=0 kai Var_Q=  (D^2)/12
P = np.var(sq_triangle1)
print('P=', P)
SNR_theoritiko=P/Var_Q
print('SNR Θεωρητικό',SNR_theoritiko)
SNR_peiramatiko_10=P/(apoklisi_10**2)
print('SNR πειραματικό για 10 δείγματα', SNR_peiramatiko_10)
SNR_peiramatiko_20=P/(apoklisi_20**2)
print('SNR πειραματικο για 20 δείγματα', SNR_peiramatiko_20)


#____c____
s=''.join(g)
sinbits=list(s)


xaxis= list(np.arange(0.0,0.384,0.001))
for i in range (len(xaxis)) :
    if i%10!=0 :
        xaxis[i] = None
xaxis[350] = 0.35

plt.figure()
plt.xticks(np.arange(384),xaxis[1:384])

k=0
height=7.0
t=np.linspace(k,k+1, 1, endpoint=False)
for a in sinbits :
    if  a=='1' :
        plt.bar(k,height,0.5,color='navy')
        plt.hlines(y=0.0, xmin=k+0.5, xmax=k+1, linewidth=2, color='navy')
    else :
        plt.bar(k,-height,0.5,color='navy')
        plt.hlines(y=0.0, xmin=k+0.5, xmax=k+1, linewidth=2, color='navy')
    k=k+1


plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Διάγραμμα ροής μετάδοσης με κωδικοποίηση γραμμής POLAR RZ')
plt.show()






#___________erotima 3_____________
#feron sima = z
#sima pliroforias = m

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

A = 1
fm = 7000
tm = 1/fm
cycles = 4

#Gia fs=130fm

fs=130*fm
ts=1/fs


fi = 35
ti=1/fi
t2 = np.arange(0,cycles*ti,ts)
m = np.sin(2*np.pi*fi*t2)

z=np.sin(2*np.pi*fm*t2)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Σήμα πληροφορίας m(t)')
plt.grid()
plt.plot(t2,m)
plt.show()

#a (amplitude modulation)
#diamorfomeno AM sima = c

c = A * (1+0.5*m) * z

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Διαμορφωμένο σήμα κατα ΑΜ')
plt.grid()
plt.plot(t2,c);
plt.show()

#erotima b (amplitude demodulation)

cdem = c * z

#Low pass filter
cutoff=fm*2.0/fs
a = signal.firwin(200,cutoff)
ydem = signal.lfilter( a , 1.0 , cdem)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Αποδιαμορφωμένο σήμα κατά ΑΜ')
plt.grid()
plt.plot(t2,ydem);
plt.show()

ydem=4*ydem #gia na anaktiso to arxiko platos
ydem=ydem-A*2 #kovo tin dc sinistosa

plt.xlabel('Time (s)')
plt.ylabel('Amplitude(V)')
plt.title('Τελικό αποδιαμορφωμένο σήμα')
plt.grid()
plt.ylim((-1.0,1.0))
plt.plot(t2,ydem);
plt.show()