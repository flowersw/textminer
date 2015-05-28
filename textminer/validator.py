import re



def binary(number):
    return re.match(r"[01]+", number)

def binary_even(number):
    return re.match(r"[02468]+$", number)


def hex(number):
    return re.match(r"\A[0-9A-Fa-f]+\Z", number)


def word():




def words():



def phone_numbers():


def money():




def zip():



def date():


#Hard mode

def hard_date():



def email():



def address():



