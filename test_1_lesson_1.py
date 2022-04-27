meters = int(input('number 1 - meters in 6WT   ')) # ситуация из моих научных разработок
if meters < 395:
    m = 2
else:
    m = 0
desaturation = int(input('number 2 - min saturation in 6WT   '))
if desaturation < 90:
    ds = 3
else:
    ds = 0
cianos = int(input('number 1 - cianosis:  '))
if cianos == 1:
    c = 1
else:
    c = 0
dispnoe = int(input('number 2 - dispnoe mMRC, scor:  '))
if dispnoe > 2:
    dp = 1
else:
    dp = 0
oedema = int(input('number 3 - oedema:  '))
if oedema == 1:
    o = 4
else:
    o = 0
interruption = int(input('number 3 - heart interruption:  '))
if interruption == 1:
    i = 1
else:
    i = 0
if m + ds + c + dp + o + i >= 5:
    print('CHF is high probability - higher 79%')
else:
    print('CHF is not probability')
