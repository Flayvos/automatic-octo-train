tupla = ('leao', 'aguia', 'fogo', 'luz',
         'conhecimento', 'paz', 'amor', 'salvacao',
         'branco', 'ordem', 'justica', 'bem')
for x in tupla:
    print(f'\nNa palavra {x.upper()} temos', end=' ')
    for vogal in x:
        if vogal.lower() in 'aeiou':
            print(f'{vogal}', end=' ')
