import decimal

changeList = [0, 0, 0, 0, 0, 0, 0, 0]

def chop_to_n_decimals(x, n):
    # rounds x to n decimals (works better for inputs like 0.005 than standard round func)
    d = decimal.Decimal(repr(x))
    targetdigit = decimal.Decimal("1e%d" % -n)
    chopped = d.quantize(targetdigit, decimal.ROUND_HALF_UP)
    return float(chopped)

def makingChange(inputVal, index, amount):
    num = int(inputVal / amount)
    changeList[index] = num
    inputVal -= (num * amount)
    if(amount < 1):
        inputVal = chop_to_n_decimals(inputVal, 2)
    return inputVal

def makeChange(amount = []):
    if((isinstance(amount, int) or isinstance(amount, float)) and (amount < 99.995 and amount >= 0.0)):
        roundedAmount = chop_to_n_decimals(amount, 2)
        roundedAmount = makingChange(roundedAmount, 0, 20)
        roundedAmount = makingChange(roundedAmount, 1, 10)
        roundedAmount = makingChange(roundedAmount, 2, 5)
        roundedAmount = makingChange(roundedAmount, 3, 1)
        roundedAmount = makingChange(roundedAmount, 4, 0.25)
        roundedAmount = makingChange(roundedAmount, 5, 0.10)
        roundedAmount = makingChange(roundedAmount, 6, 0.05)
        roundedAmount = makingChange(roundedAmount, 7, 0.01)
        return changeList
    return None
