#รับข้อมูล "ชื่อจริง(เป็นภาษาอังกฤษ)"จากผู้ใช้
#นับจำนวนสระในข้อความดังกล่าว

#ตัวอย่างหน้าจอ
#what is your name?:
#You have  4 vowels in your text

#name = input("what is your name?:")
name ="kevalin"
letters = list(name)
counter = 0

for char in letters:
    if char == 'a'or char =='A':
         counter = counter + 1

    elif char == 'e'or char =='E':   
         counter = counter + 1

    elif char == 'i'or char =='I':   
         counter = counter + 1  

    elif char == 'o'or char =='O':   
         counter = counter + 1   

    elif char == 'u'or char =='U':   
         counter = counter + 1  

print ("You have",counter,"vowels in your tex") 

#ท่าที่2
a=letters.count('a')
e=letters.count('e')
i=letters.count('i')
o=letters.count('0')
u=letters.count('u')

vowels = a+e+i+o+u

print("You have",counter,"vowels in your tex")
print(f"You have,(vowels)vowels in your tex")
