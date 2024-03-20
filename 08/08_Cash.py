#08_Cash
def total(pocket):
    total = 0
    for i in pocket:
        total += pocket[i]*int(i)
    return total

def take(pocket, money_in):
    for i in money_in:
        if i not in pocket:
            pocket[i] = money_in[i]
        else:
            pocket[i] += money_in[i]
    return pocket

def pay(pocket, amt):
    cash_out = {}
    for i in pocket:
        if amt >= i:
            cash_left = min(pocket[i]*i,amt-amt%i)
            if cash_left//i != 0:
                cash_out[i] = cash_left//i
            amt = amt-cash_left
    if amt != 0:
        return {}
    else:
        for i in cash_out:
            pocket[i] -= cash_out[i]
        return cash_out
exec(input().strip())