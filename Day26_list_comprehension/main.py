
numbers = [1, 2, 3]
new_list = []
for n in numbers:
	add_1 = n + 1
	new_list.append(add_1)
print(new_list)

new_list2 = [n + 1 for n in numbers]
print(new_list2)

new_list3 = [n * 2 for n in range(1, 4)]
print(new_list3)

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
short_names = [name.upper() for name in names if len(name) < 5]
print(short_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
answer = [n * n for n in numbers]
print(answer)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
answer = [n for n in numbers if n % 2 == 0]
print(answer)

new_list = []
with open("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day26_list_comprehension/file1.txt") as file1:
	new_list = [n for n in file1.readlines()]

compare_list = []
with open("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day26_list_comprehension/file2.txt") as file2:
	compare_list = [n for n in file2.readlines()]

answer = [int(n) for n in new_list if n in compare_list]
print(answer)
