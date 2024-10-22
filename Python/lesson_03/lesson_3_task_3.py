from mailing import Mailing
from address import Address

to_address = Address("194358", "СПб", "ул. Композиторов", "12", "10")
from_address = Address("194355", "СПб", "ул. Хошимина", "1", "1")
mailing = Mailing(to_address, from_address, "99", "123456789")
print(mailing)
