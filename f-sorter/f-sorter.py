import os
import re


def fileSort(path = str(), *par1):
        
        liste4 = list()
        uzantilar = list()
        extensions = ['.jpg','.png','.jpeg','.tif','.tiff','.nii','.JPG','.JPEG','.TIFF','.TIF','.NII']
        
        if len(par1) > 0 :
            extensions = []
            for ele in par1: 
                z = 0
                while z < len(ele):
                    uzantilar.append(ele[z])
                    if len(liste4) == 0:
                        liste4.append('filename.endswith(\''+ele[z]+'\')')
                        
                    else:
                        liste4.append('or filename.endswith(\''+ele[z]+'\')')                        
                    
                    z +=1
                    
            #liste4.append(':')
            str1 = ""
            for d in liste4: 
                str1 += d 
            #print(str1)
                    
        
        if len(par1) == 0 :
            str1 = ""
            for f in extensions: 
                str1 += ' '+ f 
            print('Default parametreler '+'['+str1+' ]'+' taranıyor...')
            c = 0
            while c < len(extensions): 
                if len(liste4) == 0:
                    liste4.append('filename.endswith(\''+extensions[c]+'\')')
                else:
                    liste4.append('or filename.endswith(\''+extensions[c]+'\')')
                c +=1
            #print(liste4)
            

            #liste4.append(':')
            str1 = ""
            for s in liste4: 
                str1 += s 
            #print(str1)
            
        
        #komutt = '.endswith(\'.png\')'
        
        def atoi(text):
            return int(text) if text.isdigit() else text
        def natural_keys(text):
            return [ atoi(c) for c in re.split('(\d+)',text) ]
        
        
        dosya_icindeki_uzantilar = list()
        lst_tumor   = os.listdir(path) 
        """
        k = 0
        while k < len(lst_tumor):
            deger = natural_keys(lst_tumor[k])
            son_ind = list()
            m = 0
            while m < len(lst_tumor):
                if not dosya_icindeki_uzantilar:
                    dosya_icindeki_uzantilar.append(deger[-1])
                    son_ind.append(deger[-1])
                    
                    
                elif son_ind[k] != dosya_icindeki_uzantilar[k]:
                    dosya_icindeki_uzantilar.append(deger[-1])
                m += 1
                    
            k += 1
            
        """    
        liste5 = list()
        isim = str()
        img_tumor = []
        """
        t = 0
        while t < len(lst_tumor):
            tumor = dosya_icindeki_uzantilar.index(uzantilar[t])
            t +=1
        """
        for filename in lst_tumor:
           if eval(str1):
               img_tumor.append(filename)
               
           else:
               liste5 = []
               isim = ''
               for s in uzantilar: 
                   liste5.append(s)
                   isim += ' '+s
            
        if len(img_tumor) > 0:
            print('Dosyalar bulundu. Tarama Başlıyor...')
        elif len(liste5) > 1:           
            print('['+isim+' ]'+' uzantıları dosya içerisinde bulunamadı.')
        elif len(liste5)==1:
            print('['+isim+' ]'+' uzantısı dosya içerisinde bulunamadı.')       
                        
        
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
        
        #print(liste_final)
        
        return liste_final

            
                                              


                