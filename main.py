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



class Book():

    nashriyot = 'HilolNashr'

    def __init__(self, name, page, muallif, color):
        self.name = name
        self.page = page
        self.muallif = muallif
        self.color = color

    def birthday_year(self, pages):
        return pages - self.page

class Notebook(Book):

    def __init__(self, name, page, muallif, color, age, phone):
        super().__init__(name, page, muallif, color)
        self.age = age
        self.phone = phone

    def names(self):
        return self.name


b = Book('Islom tarixi', 613, 'Shayx MuhammadYusuf', 'red')
c = Notebook('Dunyoni anglash', 343, 'Imom G\'azzoliy', 'oq', 78, +998902447298)

print(b.birthday_year(1004))
print(c.names())