from modelo.person import Person
from modelo.address import Address
from modelo.phone import Phone

if __name__ == '__main__':
    person = Person("Ana", "ana@gmail.com")
    address = Address("Rio de Janeiro", "Centro", "Rio branco 185, Sala 904")
    tel1 = Phone('cel', '1234-5678')
    tel2 = Phone('res', '8765-4321')
    phones = [tel1, tel2]

    tel1.person = person
    tel2.person = person

    address.person = person

    person.address = address
    person.phones = phones
    print(person)
    print(person.address)

    for phone in person.phones:
        print(phone)
    pass