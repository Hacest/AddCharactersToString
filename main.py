list = '''A
Lot
of
Words or numbers
Ex: item IDs'''

list_string = []
final_list = []

list_string = list.split('\n')

for id in list_string:
  final_list.append(
    "<Character to add> " + id + " <Character to add>"
  )

for id in final_list:
  print(id)