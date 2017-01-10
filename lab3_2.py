from lab3_1 import MyClient
import matplotlib.pyplot as plt

user_name = input('Введите id пользователя\n')
obj = MyClient(user_name)
age_list = obj.get_age_list()
keys = list(age_list.keys())
keys.sort()
for i in keys:
    print(i, ':', '#' * age_list[i])

fig, ax = plt.subplots()
rects1 = ax.bar(age_list.keys(), age_list.values(), 1)

plt.xlabel('Age')
plt.ylabel('Count')
plt.title('The histogram of Ages')

plt.subplots_adjust()
plt.show()
