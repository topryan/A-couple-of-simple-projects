def convert_currency(im, er):
    out = im * er
    return out

def main():

    USD_VS_RMB = 6.92
    currency_str_value = input('请输入带单位的货币金额（如：100CNY或者100USD;）:')
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
        print('转换后的金额为：', out_money)
    else:
        print('暂不支持该货币')


if __name__ == '__main__':
    main()





