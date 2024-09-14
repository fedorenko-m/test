import firebase_admin
from firebase_admin import credentials, firestore

# Инициализация приложения Firebase
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
db = firestore.client()

# Обработчик триггеров Firestore
def firestore_trigger(event, context):
    print(f'Изменение в документе Firestore: {event["value"]["fields"]}')
