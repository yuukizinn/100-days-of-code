
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
students_scores = {student:random.randint(1,100) for student in names}

passed_students = {student[0]:student[1] for student in students_scores.items() if student[1] > 60}
print(passed_students)

passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
splited_sentence = sentence.split()
answer_dict = {key:len(key) for (key) in splited_sentence}
print(answer_dict)

weather_c = {
	"Monday": 12,
	"Tuesday": 14,
	"Wednesday": 15,
	"Thursday": 14,
	"Friday": 21,
	"Saturday": 22,
	"Sunday": 24,
}
answer_dict = {key:value * 9/5 + 32 for (key, value) in weather_c.items()}
print(answer_dict)

