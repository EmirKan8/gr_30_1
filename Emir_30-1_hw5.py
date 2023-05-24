Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del Geeks['bag']
Geeks['address'] = ['ibraimova 103']
Geeks['tel'] = '+996507052018'
Geeks['Instagram'] = 'Geeks_edu'
Geeks['courses'].insert(1, 'ios', )
Geeks['courses'].insert(1, 'ux-ui', )
Geeks['courses'].insert(1, 'Основы програмирования', )
Geeks['data'] = '5 may 2018'
print(f"curses count - {len(Geeks['courses'])}")
for key, value in Geeks.items():
    print(f'{key} ==>  {value}')

print(Geeks)









