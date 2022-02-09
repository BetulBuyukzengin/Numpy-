# -*- coding: utf-8 -*-
"""
Dataset : https://data.ibb.gov.tr/dataset/saatlik-toplu-ulasim-veri-seti

Numpy ile,
• Ocak ayındaki yolcu sayısını mean, median, standard deviation, and variance bilgileri 
• En fazla ve en az kullanılan hat bilgisi
• En fazla ve en az kullanılan ulaşım tipini
"""

import csv

#dosya=open("hourly_transportation_202001.csv")
#satirlar=csv.reader(dosya)
#for line in satirlar:
 #  print(line)
import numpy as np
import pandas as pd
ocak2021=pd.read_csv("C:/Users/betul/OneDrive/Masaüstü/hourly_transportation_202101.csv")

print("************** 2021***************")
print("ocak2021:\n")
print(ocak2021)
ort=ocak2021['NUMBER_OF_PASSENGER'].mean()
print("2021_ort(mean):")
print(ort)


standarts=ocak2021['NUMBER_OF_PASSENGER'].std()
print("2021_std:")
print(standarts)

medyan=ocak2021['NUMBER_OF_PASSENGER'].median()
print("2021_median: ")
print(medyan)

varyans=ocak2021['NUMBER_OF_PASSENGER'].var()
print("2021_varyans:")
print(varyans)

print("************** 2020***************")

ocak2020=pd.read_csv("C:/Users/betul/OneDrive/Masaüstü/hourly_transportation_202001.csv")
print("ocak2020: ")
print(ocak2020)

ort=ocak2020['NUMBER_OF_PASSENGER'].mean()

print("2020_ort(mean):")
print(ort)


standarts=ocak2020['NUMBER_OF_PASSENGER'].std()
print("2020_std:")
print(standarts)

medyan=ocak2020['NUMBER_OF_PASSENGER'].median()
print("2020_median: ")
print(medyan)

varyans=ocak2020['NUMBER_OF_PASSENGER'].var()
print("2020_varyans: ")
print(varyans)

#********************** HAT BILGILERI***************

print("ocak_2021 en çok kulanılan hat:\n")
unique,pos = np.unique(ocak2021['LINE'],return_inverse=True) 
adet = np.bincount(pos)                   
maxpos = adet.argmax()                      
print(unique[maxpos],adet[maxpos])


print("ocak_2021 en az kulanılan hat\n:")
unique,pos = np.unique(ocak2021['LINE'],return_inverse=True) 
adet = np.bincount(pos)                     
maxpos = adet.argmin()                      
print(unique[maxpos],adet[maxpos])


print("ocak_2020 en çok kullanılan :\n")
unique,pos = np.unique(ocak2020['LINE'],return_inverse=True) 
adet = np.bincount(pos)                     
maxpos = adet.argmax()
print(unique[maxpos],adet[maxpos])


print("ocak_2020 en az kulanılan hat:\n")
unique,pos = np.unique(ocak2020['LINE'],return_inverse=True) 
adet = np.bincount(pos)
maxpos = adet.argmin()                      
print(unique[maxpos],adet[maxpos])

#TRANSPORT_TYPE_DESC
# ******************************ULASIM TIPI
print("ulasım ")
unique,pos = np.unique(ocak2021['TRANSPORT_TYPE_DESC'],return_inverse=True) 
adet = np.bincount(pos)                   
maxpos = adet.argmax()               
print("ocak_2021 en çok kulanılan ulasım:")       
print(unique[maxpos],adet[maxpos])


unique,pos = np.unique(ocak2021['TRANSPORT_TYPE_DESC'],return_inverse=True) 
adet = np.bincount(pos)                     
maxpos = adet.argmin()                
print("ocak_2021 en az kulanılan ulasım:")      
print(unique[maxpos],adet[maxpos])


unique,pos = np.unique(ocak2020['TRANSPORT_TYPE_DESC'],return_inverse=True) 
adet = np.bincount(pos)                     
maxpos = adet.argmax()
print("ocak_2020 en çok kullanılan ulasım")
print(unique[maxpos],adet[maxpos])



unique,pos = np.unique(ocak2020['TRANSPORT_TYPE_DESC'],return_inverse=True) 
adet = np.bincount(pos)
maxpos = adet.argmin()          
print("ocak_2020 en az kulanılan ulasım:")            
print(unique[maxpos],adet[maxpos])
