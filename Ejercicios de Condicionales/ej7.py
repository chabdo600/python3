renta_anual = float(input('dime tu renta anual:'))
if renta_anual <= 10000:
    print('5%')
elif renta_anual <= 20000:
    print('15%')
elif renta_anual <= 35000:
    print('20%')
elif renta_anual <= 60000:
    print('30%')
elif renta_anual > 60000:
    print('45%')
else: print('error')