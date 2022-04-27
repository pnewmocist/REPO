profit = int(input('enter your profit:  '))
costs = int(input('enter your costs:  '))
co_workers = int(input('enter your co-workers:  '))
if profit > costs:
    profitability = (profit / costs) * 100
    income = profit / co_workers
    print('We work with profit, Uhra!!!', '  profitability=  %.2f' % profitability, '%', '  income=  %0.2f' % income)
else:
    print('We work with costs... We`ll be hungry')

