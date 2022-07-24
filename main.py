# n = int(input("Son kirit: "))
# m = n % 3
# z = 0
# while n > 1 and m == 0 or n == 1:
#     if n == 1:
#         print(f'bu son 3 ning {z} - darajasi')
#         break
#     z += 1
#     m = n % 3
#     n = n / 3
# if n < 1 and m != 0 or n != 1:
#     print('bu son 3 ning darajasi emas')



# def square():
#     a = int(input())
#     b = int(input())
#     return a*b
# print(square())

        

 
# n, m, l = map(int, input().split())
# f = 0
# for i in range(n, m + 1):
#     s = 0
#     v = str(i)
#     z = len(v)
#     z = int(z)
#     for j in range(z):
#         k = i % 10
#         s = s + k
#         i = i // 10
#     if s == l:
#         f += 1
# print(f)
    
#     j = str(i)
#     for k in range(len(j)):
#         s += int(j[k])

#     d = sum(s)
#     if s == l:
#         f += 1
# print(f)



# class Book:

#     nashriyot = 'HilolNashr'

#     def __init__(self, name, page, muallif, color):
#         self.name = name
#         self.page = page
#         self.muallif = muallif
#         self.color = color

#     def birthday_year(self, pages):
#         return pages - self.page

# class Notebook(Book):

#     def __init__(self, name, page, muallif, color, age, phone):
#         super().__init__(name, page, muallif, color)
#         self.age = age
#         self.phone = phone

#     def names(self):
#         return self.name


# b = Book('Islom tarixi', 613, 'Shayx MuhammadYusuf', 'red')
# c = Notebook('Dunyoni anglash', 343, 'Imom G\'azzoliy', 'oq', 78, +998902447298)

# print(b.birthday_year(1004))
# print(c.names())



# class Shaxs:

#     def __init__(self, lname, fname, byear, gender, address, phone):
#         self.lname = lname
#         self.fname = fname
#         self.byear = byear
#         self.gender = gender
#         self.address = address
#         self.phone = phone


#     def shaxs_data(self):
#         return f'''Mening ismim {self.fname}. Familiyam esa {self.lname}. Men {self.byear} yilda tug\'ilganman. Jinsim {self.gender}. Men {self.address}da tug'ilganman. Murojaat uchun {self.phone}. Tashrif uchun katta rahmat!'''


# class Talaba(Shaxs):

#     def __init__(self, lname, fname, byear, gender, address, phone, group, course, unver, facultety):
#         super().__init__(lname, fname, byear, gender, address, phone)
#         self.group = group
#         self.course = course
#         self.unver = unver
#         self.facultety = facultety
#         self.data = []

#     def talaba_data(self):
#         dat = super().shaxs_data()
#         date = dat + f' Men {self.unver} unversitetining {self.facultety} fakulteti {self.group}-guruh talabasiman. Hozirgi kunda {self.course}-kursda o\'qiyman.'
#         return date

    


# class Student(Talaba):

#     def __init__(self, data = []) -> None:
#         self.data = data

#     def add(self, objekt):
#         self.data.append(objekt)

#     def get_info(self):
#         return [talaba.__dict__ for talaba in self.data]

#     def remove(self, talabalar, phone):
#         for talaba in talabalar:
#             if talaba.phone == phone:
#                 print(len(talabalar))
#                 talabalar.remove(talaba)
#         return [talaba.__dict__ for talaba in talabalar]
            






# def search(talabalar, lname, fname):
#     for talaba in talabalar:
#         if talaba.lname == lname and talaba.fname == fname:
#             return talaba.talaba_data()
        

# o1 = Talaba('Khodjakulov', 'Zafar', 2003, 'erkak', 'Qashqadaryo', 902447298, '213-21', 2, "TATU", "KIF")
# o2 = Talaba('Abdullayev', 'Azizbek', 2004, 'erkak', 'Qashqadaryo', 902447221, '213-21', 2, "TATU", "KIF")
# o3 = Talaba('Nosirjonov', 'Mardon', 2003, 'erkak', 'Andijon', 902447208, '690-21', 2, "TATU", "Econimic")
# o4 = Talaba('Normaxmadov', 'Ravshan', 2003, 'erkak', 'Farg\'ona', 902442198, '113-21', 2, "TATU", "DIF")
# o5 = Talaba('Ismailov', 'Jahongir', 2003, 'erkak', 'Toshkent', 902447214, '233-21', 2, "Milliy", "Arxitekturniy")
# o6 = Talaba('Shukurov', 'Begzod', 2003, 'erkak', 'Toshkent', 902127298, '754-21', 2, "Sharqshunoslik", "jurnalistika")
# st = Student()
# st.add(o1)
# st.add(o2)
# st.add(o3)
# st.add(o4)
# st.add(o5)
# st.add(o6)
# talabalar = [o1, o2, o3, o4, o5, o6]
# for talaba in talabalar:
#     print(type(talaba.lname))
#     print('\n__________------------------_________________\n')
# print(search(talabalar, 'Shukurov', 'Begzod'))
# print(o1.talaba_data())
# print(st.get_info())
# print(dir(st))

# print(st.remove(talabalar, 902447298))





# tx = open('matn.txt', 'w')
# x = tx.read(20)
# tx.seek(0)
# s = tx.readlines(58)
# tx.seek(0)
# z = tx.readline()
# tx.seek(0)
# n = tx.readable()
# print(x)
# print(s)
# print(z)
# print(n)
# f = tx.writable()
# print(f)


# with open('matn.txt', 'w+') as f:
#     f.write('salom barcha kursdoshlar')
#     f.seek(0)
#     a = f.read()
#     b = a.upper()
#     print(b)

# def check_byear(str):
#     with open('pi_million_digits.txt', 'r') as f:
#         if str in f.read():
#             return f'Bu ma\'lumot mavjud'
#         return f'Mavjud emas'
# print(check_byear('30072003'))