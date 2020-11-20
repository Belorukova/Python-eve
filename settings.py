MONGO_HOST = 'localhost' # Сервер MongoDb
MONGO_PORT = 27017 # Порт MongoDb
MONGO_DBNAME = 'Shop' # Имя базы данных
MONGO_USERNAME = 'user' # Пользователь
MONGO_PASSWORD = 'password' # Пароль


RESOURCE_METHODS = ['GET', 'POST', 'DELETE'] # Включение методов для ресурсов (коллекций)
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE'] # Включение методов для элемента ресурса (коллекции)

X_DOMAINS = '*' # Домены (IP), с которых разрешена работа с приложением (* - все домены)
X_HEADERS = ['Content-Type', 'Accept', 'If-Match', 'Authorization', 'Cache-Control', 'Pragma', 'Expires'] # Разрешенные заголовки

# Описание документов
DOMAIN = {

    'products': { # Документ Продукция
        
        'schema': # Описание схемы
        {
            'title': # Описание поля
            {
                'type': 'string', # Тип поля
                'required': True # Обязательны
                'unique': True # Уникальный
            },
            'description': { 'type': 'string' },
            'price': { 'type': 'double', 'required': True }
        }
        
        # Настройка позволяет получать продукт не по id, а по полю title
        'additional_lookup': {
            'url': "regex('[\w]+')",
            'field': 'title',
        },

    },
