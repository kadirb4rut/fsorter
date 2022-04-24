import os
import re

def fileSort(path = str()):
        lst_tumor   = os.listdir(path)        
        
        img_tumor = []
        for filename in lst_tumor:
           if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.JPG'):
               img_tumor.append(filename)
        
                
        def atoi(text):
            return int(text) if text.isdigit() else text
        def natural_keys(text):
            return [ atoi(c) for c in re.split('(\d+)',text) ]
        
        #print(img_tumor)
        
        
        sayilar = list()
        a = 0
        #index = natural_keys(img_tumor[2])
        liste4 = list()
        for i in range(len(img_tumor)):
            index = natural_keys(img_tumor[i])
            liste2 = list()   
            for ii in range(len(index)):
                if type(index[ii]) == int:
                    liste2.append(index[ii])
                    sayi=liste2[-1]
            liste4.append(liste2)
            sayilar.append(sayi)
        sayilar.sort()
        
        liste_final = list()
        
        liste_ekle = list()
        for a in range(len(img_tumor)):
            index2 = liste4[a]
            liste_ekle.append(index2[-1])
            
        
        c = 0        
        while c < len(img_tumor):
            v = liste_ekle.index(sayilar[c])
            liste_final.append(img_tumor[v])
            c+=1
        
        print(liste_final)
        
        return liste_final









            

            
        
       
        
    
    
    




