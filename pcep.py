#                                       STRING(matn) VA UNICODE
print('Hello World!') #Hello World!
print('Hello \tWorld!') #Hello   World!
print('Hello \nWorld!') #Hello 
                        #World!


#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------


# upper() va lower() metodlari:
# upper() metodi matndagi har bir harfni katta harfga o'zgartiradi. 

ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())               # AHAD QAYUM


# lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.

ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())                # ahad qayum


#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------


# title() va capitalize() metodlari
# title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi. 

ism_sharif = 'james bond'
print(ism_sharif.title())           #James Bond


#capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.

ism_sharif = 'james bond'
print(ism_sharif.capitalize())          #James bond

#Metodlarni faqat o'zgaruvchilarga emas, balki to'g'ridan-to'g'ri matnga ham qo'llash mumkin (aslida o'zgaruvchi ham matnning (yoki boshqa ma'lumotning) manzili xolos)

print('james bond'.upper())         #JAMES BOND

#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------

                                        # DEF FUNKSIYASI(Nomli)

def gapir():
    print("Assalomu aleykum!")

gapir()

def xisobla(x, y):
    print(f"Siz bergan misol: {x} + {y}, \nBizning javobimiz: {x + y}")

xisobla(3, 10)

def salomlash():
    x = input("Iltimos, Ismingizni kiriting: ")
    y = input("Iltimos, Familiyangizni kiriting: ")
    z = input("Sizga qaysi fan kerak?: ")
    o = input("Sizga qaysi soatlar to'g'ri keladi?: ")
    print(f"Assalomu Aleykum {y} {x}. \nBizning kursimizga xush kelibsiz! \nSizni {z} faniga soat {o} ga yozib qo'ydik! \nDarsni ertadan boshlashingiz mumkin!")

salomlash()

                                        # TRY - EXCEPT 

yosh = input("Yoshingizni kiriting: ")

try:
    yosh = int(yosh)
    print(f"Siz {2026 - yosh} yilda tug'ilgansiz.")

except: 
    print("Siz butun son kiritmadingiz. \nIltimos butun son kiriting!") 


                                    # Lambda (nomsiz funksiya)

    # Raqamlar
    x = lambda a: a + 20
    print(x(5))             #25



#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------


# Sinov
# turni_aniqla(10)      # Integer
# turni_aniqla(3.14)    # Float
# turni_aniqla("Salom") # String
# turni_aniqla(True)    # Boolean