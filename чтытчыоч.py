geektech = {
    'name': 'Geektech',
    'address': 'Toktogula 175',
    'courses': {'Backend', 'Android'}
}

geeks =dict(name='GEEKS', address='Ibraimova 103')
geektech.update(geeks)
geeks = geektech.copy()
geeks['courses'].update(['Frontend', 'ios'])
print(geeks)
