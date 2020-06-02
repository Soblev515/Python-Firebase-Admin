import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Ссылка на Сервисный ключ от БД на Firebase
cred = credentials.Certificate('D:/fe/smart-library-1-firebase-adminsdk-g8x7r-2d069f053c.json')

# Подключаемся к  БД
firebase_admin.initialize_app(cred)

# Подключаемся
db = firestore.client()

print('Введите ID книги. до знака \ пишем ББК после ИН')
ID = input()

print('Введите имя книги')
name = input()

print('Введите ID автора')
IDauthor = input()

print('Введите ФИО автора, без пробелов')
Author = input()

print('Введите год издания')
date = input()

print('Введите издателя')
publisher = input()

#Запись
doc_ref = db.collection(u'NewBook').document(ID)
doc_ref.set({
    u'Name': name,
    u'IDauthor': IDauthor,
    u'Author': Author,
    u'date': date,
    u'publisher': publisher
})
