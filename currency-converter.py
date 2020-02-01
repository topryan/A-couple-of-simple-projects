USD_VS_RMB = 6.92
currency_str_value = input('请输入带单位的货币金额（如：100CNY或者100USD）:')
unit = currency_str_value[-3:]

if unit == 'CNY':
    rmb_str_value = currency_str_value[:-3]
    rmb_value = eval(rmb_str_value)
    usd_value = rmb_value / USD_VS_RMB
    print('美元金额（USD）是:', usd_value)

elif unit == 'USD':
    usd_str_value = currency_str_value[:-3]
    usd_value = eval(usd_str_value)
    rmb_value = usd_value * USD_VS_RMB
    print('人民币金额（CNY）是:', rmb_value)

else:
    print('很遗憾，我们尚不支持该种货币！')
