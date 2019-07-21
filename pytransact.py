import random
from random import randrange
def is_mastercard(cc):
    if len(cc) == 16 and cc[0] == '5' and cc.isdigit() and (cc[1]>='1' and cc[1]<='5'):
        return True
    else:
        return False


def is_valid_expiration(date):#02/23
    if len(date)==5:
        if (date[2]=="/" or date[2]==" " or date[2]=="-") and date[0].isdigit() and date[1].isdigit() and date[3].isdigit() and date[4].isdigit():
            char = date[2]
            date = date.split(char)
            date[0] = int(date[0])
            date[1] = int(date[1])
            if (date[0]>=1 and date[0]<=12) and (date[1]>=0 and date[1]<=99):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

    ...


def random_mastercard():
    rand = str((randrange(5100000000000000, 5500000000000000)))
    return rand




