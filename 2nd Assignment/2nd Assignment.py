#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy  as np
import matplotlib.pyplot as plt
import random
import matplotlib as mpl
import math
from scipy.io import wavfile
from scipy import signal


# In[39]:


# 03116718 kai 03117707
# 1o erotima
# a)

randombits = []
BPAM=[]

for i in range(0,36):       #dimiourgo tixea akoluthia 36 bits 0 i 1
    x = random.randint(0,1)
    randombits.append(x)
    BPAM.append(x)
   
A=5
print(randombits)

for n, i in enumerate(BPAM): #an to bit ine 1 prepi to platos na ine Α eno an ine 0 prepei na ine -Α
        if i == 1:
            BPAM[n] = A
            for j in range (249):   #gia na exo perissotera deigmata
                 BPAM.insert(i+j,A)
        elif i==0 :
            BPAM[n] = -A
            for j in range (249):
                BPAM.insert(i+j,-A)

t1 = np.linspace(0,7.2,9000)           

plt.plot(t1,BPAM, label = 'Κωδικοποιημένο κατά BPAM ')          #grafiki parastasi
plt.xlabel("Time (sec)")                                       
plt.ylabel("B-PAM modulation")            
plt.title("B-PAM modulation")
plt.grid() 
plt.show()

print(randombits)
          

#b)
Tb=0.2
E=math.sqrt(A**2*Tb)
ax=[-E,E]
ay=[0,0]
plt.scatter(ax,ay)
plt.xlabel("φ1(t)")              
plt.ylabel("B-PAM modulation")            
plt.title("Διάγραμμα αστερισμού BPAM")
plt.grid()
plt.show()


# In[40]:


# c-d(tipoma ton diagrammaton asterismou)
t2=np.zeros(9000)
Signalpower=A**2                                        # isxis signaltos = A^2
SNR1=6.0                                                # SNR1=Eb/N0=6db
SNR2=12.0                                               # SNR2=Eb/N0=12db
NoisePower= Signalpower/(2*math.sqrt(10.0**(SNR1/10)))  #vriskoume tin isxi tou thorivou
AWGN = np.random.normal(0,math.sqrt(NoisePower) ,9000)#dimiourgoume thorivo pou akolouthei kanoniki katanomi  
asterismos=np.random.normal(0,math.sqrt(NoisePower) ,9000)+t2  
BPAMnoise=AWGN+BPAM                                    # kai ton prosthetoume sto signal

plt.plot(t1,BPAMnoise, label = 'Δείγματα ')             # tipoma tou B-PAM diamorfosis me thorivo 6dB
plt.xlabel("Time (sec)")                                        
plt.ylabel("B-PAM modulation")            
plt.title("B-PAM modulation με θόρυβο Eb/N0=6dB")
plt.grid() 
plt.show()

plt.scatter(BPAMnoise,asterismos, label = 'Δείγματα ')      # tipoma asterismou tou B-PAM diamorfosis me thorivo 6dB    
plt.grid()                                               
plt.xlabel("In Phase Component")                                        
plt.ylabel("Quadrante Component")            
plt.title("Διάγραμμα αστερισμού B-PAM modulation με θόρυβο Eb/N0=6dB")
plt.show()

NoisePower= Signalpower/(2*math.sqrt(10.0**(SNR2/10.0)))  #idia diadikasia me pio panw alla tora me thorivo Eb/N0=12db
AWGN = np.random.normal(0,math.sqrt(NoisePower) ,9000)
BPAMnoise=AWGN+BPAM
asterismos=np.random.normal(0,math.sqrt(NoisePower) ,9000)+t2

plt.plot(t1,BPAMnoise, label = 'Δείγματα ')               # tipoma tou B-PAM diamorfosis me thorivo 12dB      
plt.xlabel("Time (sec)")                                        
plt.ylabel("B-PAM modulation")            
plt.title("B-PAM modulation με θόρυβο Eb/N0=12dB")
plt.grid()
plt.show()

plt.scatter(BPAMnoise,asterismos, label = 'Δείγματα ')        # tipoma asterismou tou B-PAM diamorfosis me thorivo 12dB   
plt.grid()                                               
plt.xlabel("In Phase Component")                                        
plt.ylabel("Quadrante Component")            
plt.title("Διάγραμμα αστερισμού B-PAM modulation με θόρυβο Eb/N0=12dB")
plt.show()


# In[48]:


# e)
counter = np.zeros(16)      #midenizoume ena pinaka metriton gia ta lathi metadosis
for i in range (0, 16):
    NPpeiramatiko = (Signalpower/(10**(i/10.0)))/2.0
    Npeiramatiko = np.random.normal(0, math.sqrt(NPpeiramatiko), 9000) #paragoume to thorivou me kathe Eb/N0 kai ton prosthetoume sto signal
    BPAMpeiramatiko = BPAM + Npeiramatiko
    for j in range (0, 9000):                  # an auto p metadidete kai i pragmatiki timi exoun diaforetika tote exoume lathos
        if (BPAMpeiramatiko[j]*BPAM[j]<=0):
            counter[i]=counter[i]+1

BER = counter /9000.0         #ipologizoume to BER gia tin kathe periptosi
k = np.arange(len(BER))

plt.plot (k, BER, label='Bit Error Rate') 
plt.yscale('log') #logarithmiki klimaka
plt.grid()
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title("Bit Error Rate for BPAM modulation")
plt.show()   


# In[49]:


#2o erotima

#a
#BPSK

fc=3 # thetoume sixnotita fc=3, peritto athrisma AM

BPSKsignal=[]                  # me 9000 deigmata

t3=np.linspace(0,7.2,9000)             # dimiourgoume pinaka gia to xrono

for i in range (0, 36):          
    if randombits[i]==0:         
        phase=0                      # an to bit=0  i fasi ine 0
        for k in range (0,250):
             BPSKsignal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))       

    elif randombits[i]==1 :
        phase=np.pi                 # an to bit=1 i fasi einai π
        for k in range (0,250):
             BPSKsignal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
        
print (randombits) # akoluthia meta apo BPSK modulataion

plt.plot (t3,BPSKsignal,label = 'Δείγματα') 	
plt.xlabel("Time (sec)")              
plt.ylabel("Amplitude")            
plt.title("BPSK modulation")
plt.show()    

#QPSK

QPSKseries=[]
QPSKsignal=[]

#erotima 3a pu xriazete QPSK modulation to kanw edw
signalI=[]
signalQ=[]
signalI2=[]
signalQ2=[]
      
for i in range (0, 36,2):       #metatrepw tin akoluthia ton 36 bits se akoluthia stin opia metadidw 2 ta bit mazi
    if randombits[i]==0 and randombits[i+1]==0  :  
        QPSKseries.insert(i//2,'00') #i fasi ine 45 mires an ine 00 ta bit
        phase=np.pi/4
        for k in range (0,500):
            QPSKsignal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
            signalI.insert(i+k,A*np.cos(phase))              
            signalQ.insert(i+k,A*np.sin(phase))
            signalI2.insert(i+k,A*np.cos(phase+np.pi/4)) #p/4 QPSK modulation
            signalQ2.insert(i+k,A*np.sin(phase+np.pi/4))     
    elif randombits[i]==0 and randombits[i+1]==1  :
        QPSKseries.insert(i//2,'01') #i fasi ine 135 mires an ine 01 ta bit
        phase=np.pi*3/4
        for k in range (0,500):
            QPSKsignal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
            signalI.insert(i+k,A*np.cos(phase))              
            signalQ.insert(i+k,A*np.sin(phase))
            signalI2.insert(i+k,A*np.cos(phase+np.pi/4)) #p/4 QPSK modulation
            signalQ2.insert(i+k,A*np.sin(phase+np.pi/4))    
    elif randombits[i]==1 and randombits[i+1]==1  :
        QPSKseries.insert(i//2,'11') #i fasi ine 225 mires an ine 11 ta bit
        phase=np.pi*5/4
        for k in range (0,500):
            QPSKsignal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
            signalI.insert(i+k,A*np.cos(phase))              
            signalQ.insert(i+k,A*np.sin(phase))
            signalI2.insert(i+k,A*np.cos(phase+np.pi/4)) #p/4 QPSK modulation
            signalQ2.insert(i+k,A*np.sin(phase+np.pi/4))    
    elif randombits[i]==1 and randombits[i+1]==0  : 
        QPSKseries.insert(i//2,'10')   #i fasi ine 315 mires an ine 10 ta bit
        phase=np.pi*7/4
        for k in range (0,500):
            QPSKsignal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
            signalI.insert(i+k,A*np.cos(phase))              
            signalQ.insert(i+k,A*np.sin(phase))
            signalI2.insert(i+k,A*np.cos(phase+np.pi/4)) #p/4 QPSK modulation
            signalQ2.insert(i+k,A*np.sin(phase+np.pi/4))    

print (QPSKseries) # tipwnoume tin prokiptousa randombits simvolwn pou prokiptei apo to QPSK modulation

plt.plot (t3,QPSKsignal,label = 'Δείγματα')             # tipwnoume to signal mas pou prokiptei apo to QPSK modulation
plt.xlabel("Time (sec)")                           
plt.ylabel("Amplitude")            
plt.title("QPSK modulation")
plt.show()   

#8-PSK
        
PSK8series=[]
PSK8signal=[]

#grey code

for i in range (0, 36,3):   #metatrepw tin akoluthia ton 36 bits se akoluthia stin opia metadidw 3 ta bit mazi
    if randombits[i]==0 and randombits[i+1]==0 and randombits[i+2]==0 :
        PSK8series.insert(i//3,'000') #i fasi ine 0 mires an ine 000 ta bit
        phase=0
        for k in range (0,750):
            PSK8signal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
    elif randombits[i]==0 and randombits[i+1]==0 and randombits[i+2]==1  :
        PSK8series.insert(i//3,'001') #i fasi ine 45 mires an ine 001 ta bit
        phase=np.pi/4
        for k in range (0,750):
            PSK8signal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
    elif randombits[i]==0 and randombits[i+1]==1 and randombits[i+2]==1  :
        PSK8series.insert(i//23,'011') #i fasi ine 90 mires an ine 011 ta bit
        phase=np.pi/2
        for k in range (0,750):
            PSK8signal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
    elif randombits[i]==0 and randombits[i+1]==1 and randombits[i+2]==0  :
        PSK8series.insert(i//3,'010')   #i fasi ine 135 mires an ine 010 ta bit
        phase=np.pi*3/4
        for k in range (0,750):
            PSK8signal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
    elif randombits[i]==1 and randombits[i+1]==1 and randombits[i+2]==0  :
        PSK8series.insert(i//3,'110')   #i fasi ine 180 mires an ine 110 ta bit
        phase=np.pi
        for k in range (0,750):
            PSK8signal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
    elif randombits[i]==1 and randombits[i+1]==1 and randombits[i+2]==1  :
        PSK8series.insert(i//3,'111')   #i fasi ine 225 mires an ine 111 ta bit
        phase=np.pi*5/4
        for k in range (0,750):
            PSK8signal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
    elif randombits[i]==1 and randombits[i+1]==0 and randombits[i+2]==1  :
        PSK8series.insert(i//3,'101')   #i fasi ine 270 mires an ine 101 ta bit
        phase=np.pi*3/2
        for k in range (0,750):
            PSK8signal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
    elif randombits[i]==1 and randombits[i+1]==0 and randombits[i+2]==0  :
        PSK8series.insert(i//3,'100')   #i fasi ine 315 mires an ine 100 ta bit
        phase=np.pi*7/4
        for k in range (0,750):
            PSK8signal.insert(i+k,A*np.cos(2*np.pi*fc*t3[k]+phase))
    
print (PSK8series) # akolouthia meta apo 8-PSK modulation

plt.plot (t3,PSK8signal,label = 'Δείγματα')             # tipwnoume to signal mas pou prokiptei apo to 8-PSK modulation
plt.xlabel("Time (sec)")                           
plt.ylabel("Amplitude")            
plt.title("8-PSK modulation")
plt.show()   


# In[37]:


# erotima 3
#a Ta signalta ipologistikan sto erotima 2 opu ekana QPSK modulation

plt.plot (signalI2,signalQ2,'bo' , label = 'Δείγματα')    
plt.plot (signalI,signalQ,'rx' , label = 'Δείγματα')      
plt.xlabel("In Phase Component")                                    
plt.ylabel("Quadrante Component")                     
plt.title("π/4 -QPSK modulation")
plt.grid()
plt.show()            


# In[52]:


#b)
#snr=6 db
NoisePower= Signalpower/(2*math.sqrt(10.0**(SNR1/10.0)))  # dimiourgoume thorivo opws to erotima 1c
AWGN = np.random.normal(0,math.sqrt(NoisePower) ,9000)  
noiseI2=AWGN+signalI2
noiseI=AWGN+signalI
noiseQ=np.random.normal(0,math.sqrt(NoisePower) ,9000)+signalQ
noiseQ2=np.random.normal(0,math.sqrt(NoisePower) ,9000)+signalQ2

plt.plot (noiseI2,noiseQ2,'bo' , label = 'Δείγματα')    
plt.plot (noiseI,noiseQ,'rx' , label = 'Δείγματα')      
plt.grid()                                                  
plt.xlabel("In Phase Component")                                        
plt.ylabel("Quadrante Component")            
plt.title("Διάγραμμα αστερισμού π/4-QPSK  modulation με Eb/N0=6dB")
plt.show()

#snr=12 db
NoisePower= Signalpower/(2*math.sqrt(10.0**(SNR2/10.0)))
AWGN = np.random.normal(0,math.sqrt(NoisePower) ,9000)
noiseI2=AWGN+signalI2
noiseI=AWGN+signalI
noiseQ=np.random.normal(0,math.sqrt(NoisePower) ,9000)+signalQ
noiseQ2=np.random.normal(0,math.sqrt(NoisePower) ,9000)+signalQ2

plt.plot (noiseI2,noiseQ2,'bo' , label = 'Δείγματα')    
plt.plot (noiseI,noiseQ,'rx' , label = 'Δείγματα')     
plt.grid()                                                  
plt.xlabel("In Phase Component")                                        
plt.ylabel("Quadrante Component")            
plt.title("Διάγραμμα αστερισμού π/4-QPSK  modulation με Eb/N0=12dB")
plt.show()


# In[53]:


#3c

counter = np.zeros(36)
for i in range (0, 36):
    NPpeiramatiko = (Signalpower/(10**(i/10.0)))/2.0
    InNpeiramatiko = np.random.normal(0, math.sqrt(NPpeiramatiko), 9000)
    QuNpeiramatiko = np.random.normal(0, math.sqrt(NPpeiramatiko), 9000)
    InQPSKpeiramatiko = signalI2 + InNpeiramatiko
    QuQPSKpeiramatiko = signalQ2 + QuNpeiramatiko
    InQPSKpeiramatiko2 = signalI + InNpeiramatiko
    QuQPSKpeiramatiko2 = signalQ + QuNpeiramatiko
    for j in range (0, 9000, 2):           #ean i apostasi metaksi tou simiou pou metadidoume kai tis pragmatikis timis einai megaliteri apo tin timi sqrt(2)*A/2 exoume sfalma
        if (math.sqrt((InQPSKpeiramatiko[j]-signalI2[j])**2 + (QuQPSKpeiramatiko[j]-signalQ2[j])**2) > A/2.0*math.sqrt(2)):
            counter[i]=counter[i]+1
        if (math.sqrt((InQPSKpeiramatiko2[j+1]-signalI[j+1])**2 + (QuQPSKpeiramatiko2[j+1]-signalQ[j+1])**2) > A/2.0*math.sqrt(2)):
            counter[i]=counter[i]+1
            
BER = counter / 9000.0
k = np.arange(len(BER))

plt.plot (k, BER, label='Bit Error Rate') #tiponoume tin kampili BER gia tin metadosi me QPSK pi/4
plt.yscale('log')
plt.grid()
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title("Bit Error Rate για QPSK Modulation")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()    


# In[9]:


#di

st = "A single station could only provide coverage to half the globe, and for a world service three would be required, though more could be readily utilised. The stations would be arranged approximately equidistantly around the earth. The stations in the chain would be linked by radio or optical beams, and thus any conceivable beam or broadcast service could be provided. The technical problems involved in the design of such stations are extremely interesting, but only a few can be gone into here. Batteries of parabolic reflectors would be provided, of apertures depending on the frequencies employed."
bits2=' '.join('{0:08b}'.format(ord(x), 'b') for x in st) #8 bits per letter

print(bits2)


# In[54]:


# 4 erotima (bonus)
# a 

frequency, soundfile = wavfile.read('soundfile1_lab2.wav')
duration = 1.0*len(soundfile)/frequency  #vriskome poso diarki to wav file
t4 = np.linspace (0, duration, len(soundfile)) 

plt.plot (t4, soundfile, label='Signal')   #parousiazoume to sima
plt.grid()
plt.xlabel("Time (Sec)")
plt.ylabel("Amplitude")
plt.title("SoundFile1_lab2")
plt.show()

#b
#kvantisi 8 bits
n=8 #eukrinia kvantismou
#ypologismos vimatos kvantismou
d=(A-(-A))/(2**n-1)

#eksisosi mid-riser kvantisti
kvantismeno=d*np.floor(soundfile/d)+d/2


plt.plot(t4, kvantismeno, label='Signal')
plt.grid()
plt.xlabel("Time (Sec)")
plt.ylabel("Amplitude")
plt.title("The Signal after passing through an 8-bit Quantizer")
plt.show()


# In[55]:


#4c                  
bits = np.zeros (4*len(kvantismeno))
binary_sima = np.zeros (len(kvantismeno))
for i in range (len(kvantismeno)):
    binary_sima[i] = np.binary_repr(int(kvantismeno[i]))
Intbinary_sima = binary_sima.astype(int)        
for i in range (len(kvantismeno)):    
    bits [4*i] = Intbinary_sima[i] / 1000000
    bits [4*i+1] = (Intbinary_sima[i] % 1000000) / 10000 
    bits [4*i+2] = (Intbinary_sima[i] % 10000) / 100
    bits [4*i+3] = Intbinary_sima[i] % 100
    
# metatropi kathe stoixeiou apo dekadiko se diadiko
transsymbols = np.zeros (len(bits))
transsymbols = transsymbols.astype(int)
for i in range(len(bits)):
    transsymbols[i] = 2 * (bits[i]/10) + (bits[i] % 10)


GRAY = [0, 1, 3, 2]
transmit = np.zeros(len(transsymbols))
for i in range (len(transsymbols)):
    for j in range (0,4):
        if (transsymbols[i]==GRAY[j]):
            transmit[i]=j
            break

# dimiourgume tis in-phase kai quadrate sinistoses
QQPSK = np.zeros(len(transsymbols))  
IQPSK = np.zeros(len(transsymbols))    
for i in range (len(transsymbols)):
    QQPSK[i] = math.sqrt(2)*math.sin(transmit[i]*2*math.pi/4 + math.pi/4)
    IQPSK[i] = math.sqrt(2)*math.cos(transmit[i]*2*math.pi/4 + math.pi/4)
t2 = np.linspace (0, duration, 4*len(sima)) 
    

plt.step(t2,IQPSK, label='In Phase Component')
plt.grid()
plt.xlabel("Time (Sec)")
plt.ylabel("Amplitude")
plt.title("In Phase Component of baseband-QPSK")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.axis ([0, 0.0005, -1.1, 1.1])
plt.show()

plt.step(t2,QQPSK, label='Quadrate Component')
plt.grid()
plt.xlabel("Time (Sec)")
plt.ylabel("Amplitude")
plt.title("Quadrate Component of baseband-QPSK")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.axis ([0, 0.0005, -1.1, 1.1])
plt.show()


# In[57]:


#erotima d

#ipologizoume tin isxi tou thorivou
Signalpower = 1.0 # isxis palmoseiras = 1  afou platos = 1 V
SNR1=4
SNR2=14
Noise4 = Signalpower/(2*math.sqrt(10.0**(SNR1/10)))
Noise14 = Signalpower/(2*math.sqrt(10.0**(SNR2/10)))

#dimiourgia thorivou gia Eb/N0=4 kai 14 db
INoise4 = np.random.normal(0, math.sqrt(Noise4), len(IQPSK))
QNoise4 = np.random.normal(0, math.sqrt(Noise4), len(QQPSK))
INoise14 = np.random.normal(0, math.sqrt(Noise14), len(IQPSK))
QNoise14 = np.random.normal(0, math.sqrt(Noise14), len(QQPSK))

# ta nea simata me AGWN
FinalIQPSK4 = IQPSK + INoise4
FinalQQPSK4 = QQPSK + QNoise4
FinalIQPSK14 = IQPSK + INoise14
FinalQQPSK14 = QQPSK + QNoise14

# ta diagrammata asterismou pou zitountai sto 4e pou proekipsan sto erotima 4d
plt.plot(FinalIQPSK4, FinalQQPSK4, 'bx', label='Constellation Diagram')
mpl.rcParams['agg.path.chunksize'] = 10000
plt.grid()
plt.xlabel("In Phase Component")
plt.ylabel("Quadrate Component")
plt.title("Constellation Diagram with 4dB (Eb/N0)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

plt.plot(FinalIQPSK14, FinalQQPSK14, 'ro', label='Constellation Diagram')
mpl.rcParams['agg.path.chunksize'] = 10000
plt.grid()
plt.xlabel("In Phase Component")
plt.ylabel("Quadrate Component")
plt.title("Constellation Diagram with 14dB (Eb/N0)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


#ginetai i apokodikopoiisi tou simatos gia tis 2 times thorivou
bApodiamorfosi4 = np.zeros(len(transsymbols))
Apodiamorfosi4 = np.zeros (len(transsymbols))
for i in range (len (transsymbols)):
    if ((FinalIQPSK4[i]>0) and (FinalQQPSK4[i]>0)):
        Apodiamorfosi4[i] = 0
    elif ((FinalIQPSK4[i]<0) and (FinalQQPSK4[i]>0)):
        Apodiamorfosi4[i] = 1
    elif ((FinalIQPSK4[i]<0) and (FinalQQPSK4[i]<0)):
        Apodiamorfosi4[i] = 3
    else:
        Apodiamorfosi4[i] = 2
    bApodiamorfosi4[i] = np.binary_repr(int(Apodiamorfosi4[i]))
Intapodiamorfosi4=np.zeros(len(transsymbols))    

telikosima4=np.zeros(len(sima))
for i in range (len(sima)):
    telikosima4[i] = Apodiamorfosi4[4*i]*64+Apodiamorfosi4[4*i+1]*16+Apodiamorfosi4[4*i+2]*4+Apodiamorfosi4[4*i+3]

bApodiamorfosi14 = np.zeros(len(transsymbols))
Intapodiamorfosi14=np.zeros(len(transsymbols))
Apodiamorfosi14 = np.zeros (len(transsymbols))
for i in range (len (transsymbols)):
    if ((FinalIQPSK14[i]>0) and (FinalQQPSK14[i]>0)):
        Apodiamorfosi14[i] = 0
    elif ((FinalIQPSK14[i]<0) and (FinalQQPSK14[i]>0)):
        Apodiamorfosi14[i] = 1
    elif ((FinalIQPSK14[i]<0) and (FinalQQPSK14[i]<0)):
        Apodiamorfosi14[i] = 3
    else:
        Apodiamorfosi14[i] = 2
    bApodiamorfosi14[i] = np.binary_repr(int(Apodiamorfosi14[i]))
Intapodiamorfosi14[i]=bApodiamorfosi14[i].astype(int) 

telikosima14=np.zeros(len(sima))
for i in range (len (sima)):
    telikosima14[i] = Apodiamorfosi14[4*i]*64+Apodiamorfosi14[4*i+1]*16+Apodiamorfosi14[4*i+2]*4+Apodiamorfosi14[4*i+3]

#ipologismos Bit error rate
counter4=0
counter14=0
for i in range (len(transsymbols)):
    if (Apodiamorfosi4[i] != transsymbols[i]):
        counter4=counter4+1
    if (Apodiamorfosi14[i] != transsymbols[i]):
        counter14=counter14+1

#ipologismos ton ber
BER4 = 1.0 * counter4 / len(transsymbols)
BER14 = 1.0 * counter14 / len(transsymbols)
#tipono ta ber gia kathe timi
print ("The BER for Eb/No=4dB is: %s" %BER4)
print ("The BER for Eb/No=14dB is: %s" %BER14)

#eksagogi ton 2 apokodikopoiimenon wav file
#i sixnotita eggrafis einai kata 4 fores megaliteri logo tou oti grafoume ta bit ana diades sto sima kai oxi ana 8ades opos ta pirame apo afto
wavfile.write('C:/Users/n_pey/Downloads', 44100, telikosima4)  
wavfile.write('C:/Users/n_pey/Downloads', 44100, telikosima14)


# In[ ]:




