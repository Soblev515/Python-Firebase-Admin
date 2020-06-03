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

# Запись
doc_ref = db.collection(collection).document(ID)

doc = doc_ref.get()
if doc.exists:
    print(u'Document data: {}'.format(doc.to_dict()))
else:
    print(u'No such document!')