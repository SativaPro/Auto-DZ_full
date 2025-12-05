from address import Address
from mailing import Mailing

to_address = Address("123456", "г. Москва", "ул. Ленина", "д. 10", "кв. 15")
from_address = Address("654321", "г. Воронеж", "ул. Пушкина", "д. 5", "кв. 3")

mailing = Mailing(to_address, from_address, 250, "TRACK0000-1")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
