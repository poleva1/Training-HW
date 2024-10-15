from smartphone import Smartphone

catalog = []

phone1 = Smartphone('Oppo', 'A5', '+79991111111')
phone2 = Smartphone('Oppo', 'A7', '+79992222222')
phone3 = Smartphone('Xiaomi', 'Poco', '+79993333333')
phone4 = Smartphone('Samsung', 'A24', '+79994444444')
phone5 = Smartphone('Apple', 'iPhone 15Pro', '+79995555555')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'Марка: {phone.brand} - Модель: {phone.model}. Номер: {phone.number}')
