**Eng**
=====================
# Python-Firebase-Admin
----------------------------------
This repositories is help you job this Farebase server using Python.
More information in the official documentation:<https://firebase.google.com/docs/admin/setup>

# Add the SDK
----------------------------------
In first, you need to install the SDK for Python.
The Firebase Admin Python SDK is available via pip. You can install the library for all users via sudo:

>$ sudo pip install firebase-admin

Or, you can install the library for just the current user by passing the --user flag:

>$ pip install --user firebase-admin

# Initialize the SDK
----------------------------------
Once you have created a Firebase project, you can initialize the SDK with an authorization strategy that combines your service account file together with Google Application Default Credentials.

Firebase projects support Google service accounts, which you can use to call Firebase server APIs from your app server or trusted environment. If you're developing code locally or deploying your application on-premises, you can use credentials obtained via this service account to authorize server requests.

To authenticate a service account and authorize it to access Firebase services, you must generate a private key file in JSON format.

To generate a private key file for your service account:

1. In the Firebase console, open Settings > Service Accounts.

2. Click Generate New Private Key, then confirm by clicking Generate Key.

3. Securely store the JSON file containing the key.

When authorizing via a service account, you have two choices for providing the credentials to your application. You can either set the GOOGLE_APPLICATION_CREDENTIALS environment variable, or you can explicitly pass the path to the service account key in code.



**Rus**
=====================
# Python-Firebase-Admin
----------------------------------
Эти репозитории помогут вам работать с сервером Farebase с помощью Python.
Более подробная информация в официальной документации:<https://firebase.google.com/docs/admin/setup>

# Добавьте SDK
----------------------------------
Во-первых, вам нужно установить SDK для Python.
Firebase Admin Python SDK  доступен через pip. Вы можете установить библиотеку для всех пользователей через sudo:

>$ sudo pip install firebase-admin

Или же вы можете установить библиотеку только для текущего пользователя, передав флаг --user:

>$ pip install --user firebase-admin

# Инициализация пакета SDK
----------------------------------
После того как вы создали проект Firebase, вы можете инициализировать SDK с помощью стратегии авторизации, которая объединяет ваш файл учетной записи службы вместе с учетными данными приложения Google по умолчанию.

Проекты Firebase поддерживают учетные записи служб Google, которые можно использовать для вызова API-интерфейсов Firebase server с сервера приложений или из доверенной среды. Если вы разрабатываете код локально или развертываете приложение локально, вы можете использовать учетные данные, полученные с помощью этой учетной записи службы, для авторизации запросов сервера.

Для проверки подлинности учетной записи службы и разрешить ему доступ к услугам военнослужащих, необходимо создать отдельный ключевой файл в формате JSON.

Чтобы создать файл закрытого ключа для вашей учетной записи службы:

1. В консоли Firebase откройте Настройки > Учетные записи служб.

2. Нажмите кнопку Создать новый Закрытый ключ, а затем подтвердите это, нажав кнопку Создать ключ.

3. Надежно храните файл JSON, содержащий ключ.

При авторизации через учетную запись службы у вас есть два варианта предоставления учетных данных для вашего приложения. Вы можете либо задать переменную среды GOOGLE_APPLICATION_CREDENTIALS, либо явно передать путь к ключу учетной записи службы в коде.
