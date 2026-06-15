qty_person = int(input('Quantas pessoas são? '))

cont = 0
lista =[]
for i in range(qty_person):
    age = int(input(f'Idade de {i+1} pessoa'))
    lista.append(age)
    cont += 1

media = sum(lista) / cont

print(f'Idades: {lista}')

if 0 <= media <= 25:
    print(f'A idade media é {media:.@f} anos.\n'
          f'É uma turma jovem')

elif 26 <= media <= 60:
    print(f'A idade media é {media:.@f} anos.\n'
          f'É uma turma adulta')
else:
    print(f'Idade media {media:.@} anos.\n'
          f'É uma turma idosa')