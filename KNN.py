import csv
import math
import numpy as np

#memasukan data pada csv kedalam array
Test = list(csv.reader(open('Test_Tugas2.csv')))
Train = list(csv.reader(open('Train_Tugas2.csv')))

def hitung_distance(Train,Test): #menghitung distance dari data train dan data test pada tiap X
    hasil = math.sqrt((float(Train[0])-float(Test[0]))**2+
    (float(Train[1])-float(Test[1]))**2+
    (float(Train[2])-float(Test[2]))**2+
    (float(Train[3])-float(Test[3]))**2)
    return hasil

def hitung_K(Train): #menghitung K dari total data train
    hasil = math.ceil(math.sqrt(len(Train)))
    return hasil

def hitung_class(Data): #menghitung banyaknya frekuensi kelas dan menentukan kelas data
    Class0=0
    Class1=0
    Class2=0
    for x in range(hitung_K(Data)):    
        if Data[x][4] == '0':
            Class0+=1
        elif Data[x][4] == '1':
            Class1+=1
        elif Data[x][4] == '2':
            Class2+=1
    if Class0 > Class1 and Class0 > Class2:
        Class = 0
    elif Class1 > Class0 and Class1 > Class2:
        Class = 1
    elif Class2 > Class0 and Class2 > Class1:
        Class = 2
    return Class
    
def to2array(Data): #membuat array 1 dimensi menjadi 2 dimensi
    NewData = np.reshape(Data,(-1,1))
    return NewData

def CombineArray(Array1,Array2): #menggabungkan Array1 dengan Array2
    Data = np.append(Array1,Array2,axis = 1)
    return Data

DataClass = []
NewTest = []       
for x in range(1,len(Test)):    
    Distance = []
    NewTrain = []
    for y in range(1,len(Train)):
        Distance.append(hitung_distance(Train[y],Test[x]))
        NewTrain.append(Train[y])
        NewDistance = to2array(Distance)
    Combine = CombineArray(NewTrain,NewDistance)    
    Combine = Combine[Combine[:,5].argsort()] #mensort array dari data pada kolom ke 5(Distance) dari yang terkecil hingga terbesar
    DataClass.append(hitung_class(Combine))
    NewTest.append(Test[x])
DataClass = to2array(DataClass)
Prediksi = CombineArray(NewTest,DataClass)
write = csv.writer(open ('Predict_Tugas2.csv', 'w'), delimiter=',', lineterminator='\n')#membuat file outputan "Predict_Tugas2.csv"
write.writerow(['X1','X2','X3','X4','Class'])
for x in Prediksi : write.writerow (x)