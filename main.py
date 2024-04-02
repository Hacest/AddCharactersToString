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
    "<아이템 생성 치트> " + id + ""
  )

for id in final_list:
  print(id)