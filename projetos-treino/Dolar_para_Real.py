#código simples da cotação do dolar para real
#dolar na data de (03/06/2019)

d = 3.92
for r in range(0,15):
    print('US$ {:5.2f} = R$ {:5.2f}'.format(r, r*d))
