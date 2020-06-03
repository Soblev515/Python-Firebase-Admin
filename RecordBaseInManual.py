import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Ссылка на Сервисный ключ от БД на Firebase
cred = credentials.Certificate('D:/fe/smart-library-1-firebase-adminsdk-g8x7r-2d069f053c.json')

# Подключаемся к  БД
firebase_admin.initialize_app(cred)

# Подключаемся
db = firestore.client()

print('Введите название коллекции:')
collection = input()

print('Введите название документа:')
ID = input()

#Запись
doc_ref = db.collection(collection).document(ID)
print('Вводите информацию так: |Название переменной|: |Значение переменной|')
print('Вводите |break| если ввод информации закончен')
while 1!=0:
    info = input()
    if(info == "break"):
        break
    a=len(info)
    for i to len:
        name += i
        if i+1 = ":":
            i+=2            
            while i!= a:
                value += i
            break
    
    doc_ref.set({
        name: value,
    })
