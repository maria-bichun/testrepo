fh = 'start'
fr = 'start'

ih = input('Enter hours: ')
while fh == 'start':
    try: fh = float(ih)
    except: ih = input('Error. Please enter numeric data. Enter hours: ')

ir = input('Enter rate: ')
while fr == 'start':
    try: fr = float(ir)
    except: ir = input('Error. Please enter numeric data. Enter rate: ')

if fh <= 40:
    pay = fr * fh
else: pay = fr * 40 + fr * (fh - 40) * 1.5
print('Pay: ' + str(pay))
quit()
