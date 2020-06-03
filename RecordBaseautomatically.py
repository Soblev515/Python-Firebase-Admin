# Программа для автоматической записи информации из IRBIS в БД Firebase
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import scrolledtext
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


window = Tk()
window.title("The translator databases")
window.geometry('720x400')
print('ok')

# Ссылка на Сервисный ключ от БД на Firebase
cred = credentials.Certificate('D:/fe/github/iOS_Library/iOS_Library/smart-library-8a179-firebase-adminsdk-c01sz-f51272754e.json')

# Подключаемся к  БД
firebase_admin.initialize_app(cred)

# Подключаемся
db = firestore.client()

# Указываем путь к TXT файлу, в котором находится экспортированная БД из IRBIS
f = open('D:/fe/github/iOS_Library/iOS_Library/Base_Irbis.TXT',encoding = 'utf-8')

#Находим сколько книг уже имеется
docs = db.collection(u'NewBook').stream()
def clicked():
    # инициализируем прогрессбар
    pr_bar = ttk.Progressbar(window, length=400, variable=provar)
    pr_bar.pack(padx=10, pady=5)
    window.update()
    pr_bar.update()
    i = 0
    one = 100/a
    print(one)
    proc = 0
    while i != a:
        book_name = ''
        window.update()
        name()
        proc += one
        provar.set(int(proc*100))
        print(proc)

def book_name (name, code):
    txt.insert(INSERT, name + ' (' + code + ')\n')


def name():
    fcode = ''
    fISBN = ''
    fname = ''
    fauthor = ''
    favailable = False
    fcopyright = ''
    fseries = {}
    fsecond_author = {}
    ftags = {}
    fpublisher = ''
    fdate = ''
    fbib = ''
    fprice = ''
    fcontent = {}
    fbib_code = ''
    fpersonalia = {}
    fcountry = ''
    finventory = ''
    flanguage = ''
    fsize = ''
    fprinting = ''
    k=0
    d=0
    c=0
    p=0
    m=0
    for line in f:
        result = list(line)

        #находим уникальный шифр книги+
        if (result[1] + result[2] + result[3] == '903'):

            i = 6
            a = len(line) - 1

            while i != a:
                if result[i] == '/':
                    fcode += '|'
                    i += 1
                fcode += result[i]
                i += 1

        #находим конец списка+
        if(result[1]+result[2]+result[3] == '***'):
            break

        #Сведения об экземплярах, ID библиотеки
        if (result[1] + result[2] + result[3] == '910'):
            if result[8] == 0:
                favailable = True
            i=11
            a = len(line)
            inventory = ''
            while i != a:
                if result[i] == '^':
                    i+=1
                    while result[i] != 'D':
                        i+=1
                        if i == a:
                            break
                    i+=1
                    while i != a:
                        if i == a:
                            break
                        if result[i] == '^':
                            break
                        fbib_code += result[i]
                        i+=1
                if i == a:
                    break
                if result[i] == '^':
                    break
                inventory += result[i]
                i+=1
            finventory = str(inventory)

        #находим издателя+
        if(result[1]+result[2]+result[3] == '210'):
            i = 8
            a = len(line)-1
            while i != a:
                if result[i] == '^':
                    i+=2
                    fpublisher += '('
                    while i != a:
                        if result[i] == '^':
                            fpublisher += ')'
                            i+= 2
                            while i != a:
                                fdate += result[i]
                                i+=1
                            break
                        fpublisher += result[i]
                        i+=1
                    break
                fpublisher+= result[i]
                i+=1

        #находим название книги+
        if(result[1]+result[2]+result[3] == '200'):
            i = 8
            a = len(line)
            while i != a:
                if result[i] == '^':
                    break
                fname+= result[i]
                i+=1

        #Название библиотеки+
        if(result[1]+result[2]+result[3] == '902'):
            i = 8
            a = len(line)
            while i != a:
                fbib+= result[i]
                i+=1

        #находим имя автора+
        if(result[1]+result[2]+result[3] == '700'):
            i = 8
            a = len(line)
            while i != a-1:
                if result[i] == '^':
                    fauthor += ' '
                    i+=1
                    while result[i] != '^':
                        i+=1
                    i+=2
                    if (i == a):
                        break
                    if (result[i] == '^'):
                        break
                    while i != a:
                        fauthor += result[i]
                        i+=1
                        if (i==a):
                            break
                        if(result[i] == '^'):
                            break
                if i==a:
                    break
                if(result[i] == '^'):
                    break
                fauthor += result[i]
                i+=1

        #Авторский знак
        if (result[1] + result[2] + result[3] == '908'):
            i = 6
            a = len(line)
            while i != a:
                fcopyright += result[i]
                i+=1

        #Объем и тираж+
        if (result[1] + result[2] + result[3] == '215'):
            i = 8
            a = len(line)
            while i != a - 1:
                if result[i] == ',':
                    fsize += ' '
                    i += 1
                    while result[i] + result[i+1] != '^X':
                        i += 1
                        if result[i] + result[i+1] == '^Z':
                            break
                        if (i+2 == a):
                            break
                    if (i == a):
                        break
                    i += 2
                    while i != a:
                        fprinting += result[i]
                        i += 1
                        if (i == a):
                            break
                        if (result[i] == '^'):
                            break
                if i == a:
                    break
                if (result[i] == '^'):
                    break
                fsize += result[i]
                i += 1

        #Содержание
        if (result[1] + result[2] + result[3] == '330'):
            i = 8
            a = len(line)
            content = ''
            while i != a:
                content += result[i]
                i += 1
            fcontent[c] = str(content)
            c += 1
        if (result[1] + result[2] + result[3] == '924'):
            i = 6
            a = len(line)
            content = ''
            while i != a:
                if result[i] == ' ':
                    content += '_'
                    i+=1
                content += result[i]
                i += 1
            fcontent[c] = content
            c += 1

        #Персоналия
        if (result[1] + result[2] + result[3] == '600'):
            i = 8
            a = len(line)
            personalia = ''
            while i != a:
                personalia += result[i]
                i += 1
            fpersonalia[d] = str(personalia)
            d += 1

        #другие люди, ответственные за книгу+
        if (result[1] + result[2] + result[3] == '702'):
            if result[9] == '^':
                i = 15
            else:
                i = 12
            a = len(line)
            second = ''
            while i != a - 1:
                if result[i] == '^':
                    i+=2
                    second += ' '
                    while result[i] != '^':
                        if i == a:
                            break
                        if (result[i] == '^'):
                            break
                        second += result[i]
                        if (result[i+1] == '^'):
                            i+=3
                            second += ' '
                            while result[i] != '^':
                                second += result[i]
                                i += 1
                                if i == a:
                                    break
                            break
                        i += 1

                if i==a:
                    break
                if (result[i] == '^'):
                    break
                second += result[i]
                i += 1
            fsecond_author[k] = str(second)
            k+=1

        #страна издания+
        if(result[1] + result[2] + result[3] == '102'):
            i = 6
            fcountry = result[i] + result[i + 1]

        #Серия+
        if (result[1] + result[2] + result[3] == '225'):
            i = 8
            a = len(line)
            series = ''
            while i != a:
                if result[i] == '^':
                    break
                series += result[i]
                i+=1
            fseries[m] = str(series)
            m+=1

        #Язык+
        if (result[1] + result[2] + result[3] == '101'):
            i = 6
            flanguage = result[i] + result[i + 1] + result[i+2]

        #Теги+
        if (result[1] + result[2] + result[3] == '606'):
            i = 8
            a = len(line) - 1
            TAG = ''
            while i != a:
                if result[i] == '^':
                    ftags[p] = TAG
                    i+= 2
                    p+=1
                    TAG = ''
                TAG += result[i]
                i+=1
            ftags[p] = TAG
            p+=1
        if (result[1] + result[2] + result[3] == '610'):
            i = 6
            a = len(line) - 1
            TAG = ''
            while i != a:
                TAG += result[i]
                i+=1
            ftags[p] = TAG
            p+=1

        #ISBN, Цена
        if (result[1] + result[2] + result[3] == '10:'):
            i = 7
            a = len(line)
            if (result[6] == 'D'):
                while i != a:
                    fprice += result[i]
                    i+=1
            while i != a:
                if (result[i] == '^'):
                    i += 2
                    while i != a:
                        fprice += result[i]
                        i+=1
                if i == a:
                    break
                fISBN += result[i]
                i += 1

    #Выделяем ББК из спец. кода
    BBK = ''
    for ch in fcode:
        if ch == '|':
            break
        BBK += ch

    #Формируем пакет данных на отправку
    data = {
        u'name': fname,
        u'BBK': BBK,
        u'ISBN': fISBN,
        u'Inventory_number': finventory,
        u'Size': fsize,
        u'Printing': fprinting,
        u'price': fprice,
        u'id_user': '',
        u'available': favailable,
        u'author': fauthor,
        u'id_author': fcopyright,
        u'library': fbib,
        u'id_library': fbib_code,
        u'date': fdate,
        u'publisher': fpublisher,
        u'description': '',
        u'country': fcountry,
        u'language': flanguage,
        u'score': 0

    }
    book_name(fname, fcode)
    print(fcode,fISBN, fname, fauthor,fseries, fpublisher, fdate, fcountry, flanguage, fbib)

    doc = db.collection(u'NewBook').document(fcode)

    #Отправляем данные
    if db.collection('NewBook').document(fcode).get().exists == True:
        doc.update(data)
    else:
        doc.set(data)
    #Дополняем данные данными-массивами
    #Добавляем "вторых лиц""
    o = 0
    while o !=k:
        doc.update({u'second_author': firestore.ArrayUnion([fsecond_author[o]])})
        o+=1

    #Добавляем Серии
    o=0
    while o !=m:
        doc.update({u'Series': firestore.ArrayUnion([fseries[o]])})
        o+=1

    #Содержания
    o = 0
    while o != c:
        doc.update({u'Content': firestore.ArrayUnion([fcontent[o]])})
        o += 1

    o = 0

    #Персоналия
    while o != d:
        doc.update({u'personalia': firestore.ArrayUnion([fpersonalia[o]])})
        o += 1

    #Добавляем Теги
    o = 0
    while o != p:
        doc.update({u'Tags': firestore.ArrayUnion([ftags[o]])})
        o += 1


#Тест
#ГЦ для записи
a = len(f.readlines())
f.close


# документ типа TXT из которой будем считывать БД IRBIS
f = open('D:/fe/github/iOS_Library/iOS_Library/Base_Irbis.TXT',encoding = 'utf-8')

#инициализируем кнопку
btn = Button(window, text="Start", command = clicked)
btn.pack()

# инициализируем список
txt = scrolledtext.ScrolledText(window, width=50, height=1)
txt.pack(padx = 175, pady = 10)

provar = IntVar()
provar.set(0)

window.mainloop()
