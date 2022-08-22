# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

# def open_or_senior(data=input):
#     result = []
#     for i in data:
#         if i[0] >= 55 and i[1] > 7:
# #             result.append('Senior')


# balance = 0

# def get_salary(amount):
#     global balance
#     balance = balance + amount

# def pay_bills(amount, log_name):
#     global balance
#     balance = balance - amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     print(f'У вас на счету {balance} сом')

# get_salary(1500000)
# pay_bills(150000, 'еда')
# get_balance()


list_ = [1, 2, 3, 4]

# def list1(x):
#     for i in x:
#         i = i + i

#     print(i)
    
# list1(list_)
# print(list1(list_))

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 

list_ = [2, 4, 6, 8]
result = list(map(lambda i: i ** 2, list_))
print(result)
res = []

for i in list_:
    k = i ** 2
    res.append(k)
print(res)

