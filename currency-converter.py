def convert_currency(im, er):
    out = im * er
    return out

def main():

    USD_VS_RMB = 6.92
    currency_str_value = input('Please enter the currency amount in units (eg: 100CNY or 100USD）:')
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_RMB
    elif unit == 'USD':
        exchange_rate = USD_VS_RMB
    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        out_money = convert_currency(in_money, exchange_rate)
        print('The converted amount is：', out_money)
    else:
        print('This currency is not supported yet.')


if __name__ == '__main__':
    main()





