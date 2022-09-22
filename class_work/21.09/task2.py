#todo: Задан массив
surname = ['Электроник','Сыроежкин', 'Чижиков', 'Кукушкина']

# Код на выходе должен выдавать выпадающий список следующего вида.
"""
<select>
	<option>Электроник</option>
	<option>Сыроежкин</option>
	<option>Чижиков</option>
	<option>Кукушкина</option>
</select>
"""
#конкотинация строк
#итерация цикла
#сгенерировать в цикле

surname = ['Электроник','Сыроежкин', 'Чижиков', 'Кукушкина']
x = ""
for i in surname:
	x = x + ("<option> " + i + "</option>\n")
str1 = "<select>"
str2 = "<option>\n"
str3 = "<option>"
str4 = "</select>"
print(str1, (str2 + x + str3), str4)
