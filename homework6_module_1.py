price_={'Audi': 3599,'Ford': 4499,'Vaz2110': 1299}
print(price_)
print(price_['Vaz2110'])
print(price_.get('Zaporojec'))
price_.update({'Porsche911': 9999,'Toyota': 6999})
not_avalable_=price_.pop('Ford')
print(not_avalable_)
print(price_)
my_symbols_={3.14,3.141,3.14159,'число пи',3.14159}
print(my_symbols_)
my_symbols_.update([3.141592653,(1,2,3)])
my_symbols_.discard('число пи')
print(my_symbols_)
