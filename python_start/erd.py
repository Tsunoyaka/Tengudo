# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

# def open_or_senior(data=input):
#     result = []
#     for i in data:
#         if i[0] >= 55 and i[1] > 7:
# #             result.append('Senior')
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rick = 0
pick = 0

for i in list5:
    if not i % 2:
        rick += 1
    
    else:
        pick += 1
        
print(f'Нечетные: {pick}')
print(f'Четные: {rick}')
