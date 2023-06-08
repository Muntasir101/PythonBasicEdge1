def summation(number1, number2):
    return number1 + number2


def is_prime_custom(num):
    if num < 0:
        raise Exception("wrong input number")
    try:
        if num == 1 or num == 0:
            raise Exception("not a prime number or a composite number")
        sr_num = int(num ** 0.5 + 1)
        tem = sr_num
        for i in range(sr_num):
            if (num % tem) == 0:
                break
            tem -= 1
        if tem == 1:
            return True
        else:
            return False
    except TypeError:
        raise Exception("unknown error")
