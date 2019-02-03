def cashback(monthly_expenses, ): #объявление функции
    """
    >>> cashback(10_000)
    300.0
    """
    percent = 3
    result = percent * monthly_expenses / 100
    return result

def bmi (weight, hight):
    """
    >>> bmi(106, 1.68) # doctest: +ELLIPSIS
    37.55...



    # >>> bmi(120, 1.88)
    # 33.95201448619285
    """
    result = weight / (hight ** 2)
    return result

