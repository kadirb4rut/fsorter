import os
import re
def fileSort(path = str(), extensions=list()):
        if len(extensions) == 0:
            extensions = ['.jpg', '.png', '.jpeg', '.tif', '.tiff', '.nii', '.JPG', '.JPEG', '.TIFF', '.TIF', '.NII']

        str1 ='filename.endswith(\'' + extensions[0] + '\')'
        for z in range(1, len(extensions)):
            str1 += ' or filename.endswith(\'' + extensions[z] + '\')'

        # def atoi(text):
        #     return int(text) if text.isdigit() else text
        # def natural_keys(text):
        #     return [ atoi(c) for c in re.split('(\d+)',text) ]

        if(path==''):
            path='./'
        path = os.listdir(path)

        list_not = list()
        img_list = []
        for filename in path:
           if eval(str1):
               img_list.append(filename)
           else:
               list_not.append(filename)
        if len(list_not) > 0:
            print(str(list_not)+' files not found.')

        digits = list()
        digits_temp = list()
        if(len(img_list)==0):
            print('no files !!!')
            return -1
        index2 = natural_keys(img_list[0])
        s1=0
        for ii3 in range(len(index2)):
            if type(index2[ii3]) == int:
                s1+=1
        if(s1==0):
            print('filename without digits !!!')
            return -1
        elif(s1==1):
            for i in range(len(img_list)):
                index = natural_keys(img_list[i])
                for ii in range(len(index)):
                    if type(index[ii]) == int:
                        list2 = str(index[ii])
                digits.append(list2)
                digits_temp.append(list2)
        elif(s1>1):
            list_zeros=list()
            for knt1 in range(1,s1):
                maxx = -1
                for i in range(len(img_list)):
                    index = natural_keys(img_list[i])
                    knt2 = 0
                    for ii2 in range(len(index)):
                        if type(index[ii2]) == int:
                            if (knt2 == knt1):
                                if (index[ii2] > maxx):
                                    maxx = index[ii2]
                            knt2+=1
                list_zeros.append(len(str(maxx)))

            for i in range(len(img_list)):
                index = natural_keys(img_list[i])
                knt3 = 0
                list2=''
                for ii in range(len(index)):
                    if type(index[ii]) == int:
                        if(knt3>0):
                            number_zeros=list_zeros[knt3-1]-len(str(index[ii]))
                            for j in range(0,number_zeros):
                                list2 += '0'
                            list2 += str(index[ii])
                        else:
                            list2 += str(index[ii])
                        knt3+=1
                digits.append(int(list2))
                digits_temp.append(int(list2))

        digits.sort()
        
        list_final = list()
        for c in range(len(img_list)):
            v = digits_temp.index(digits[c])
            list_final.append(img_list[v])

        return list_final

def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]