import random
import psycopg2

""" 
lấy dữ liệu ra từ database và lưu vào biến exercise
"""
class Exercise:
    def __init__(self, id, exercise_name, description, image_link, reps_per_set, kcal_per_set, time_per_set, exercise_type, difficulty_level):
        self.id = id
        self.exercise_name = exercise_name
        self.description = description
        self.image_link = image_link
        self.reps_per_set = reps_per_set
        self.kcal_per_set = kcal_per_set
        self.time_per_set = time_per_set
        self.exercise_type = exercise_type
        self.difficulty_level = difficulty_level

    def __repr__(self):
        return f"Exercise({self.id}, {self.exercise_name}, {self.description}, {self.image_link}, {self.reps_per_set}, {self.kcal_per_set}, {self.time_per_set}, {self.exercise_type}, {self.difficulty_level})"

# Connect to the database
connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres',
    dbname='mydb'
)

try:
    with connection.cursor() as cursor:
        # Select all records from the exercise_gym table
        sql = "SELECT * FROM exercise_gym"
        cursor.execute(sql)

        # Fetch all the records
        result = cursor.fetchall()

        # Initialize an empty list to hold all the exercises
        exercises = []

        # For each record, create a new Exercise object and add it to the list
        for row in result:
            exercise = Exercise(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            exercises.append(exercise)

        # Print all the exercises
        for exercise in exercises:
            print(exercise)

finally:
    connection.close()

"""
chia bài tập trong tuần:
- 3 buổi:
  + buổi 1: Ngực (Chest), Lưng (Back group), Cổ và vai (Neck & Shoulders 3 Group)
  + buổi 2: Bắp tay (Biceps group), Chân (Leags Group), Bụng và lưng dưới (Abdomen & Lower Back Group)
  + buổi 3: full body
- 5 buổi:
  + buổi 1: Ngực (Chest)
  + buổi 2: Lưng (Back group)
  + buổi 3: Cổ và vai (Neck & Shoulders 3 Group)
  + buổi 4: Bắp tay (Biceps group), Cẳng tay (Foream Group), Bắp tay sau (Triceps group)
  + buổi 5: Chân (Leags Group), Bụng và lưng dưới (Abdomen & Lower Back Group)
- 6 buổi:
  + buổi 1: Ngực (Chest)
  + buổi 2: Lưng (Back group)
  + buổi 3: Cổ và vai (Neck & Shoulders 3 Group)
  + buổi 4: Bắp tay (Biceps group), Cẳng tay (Foream Group), Bắp tay sau (Triceps group)
  + buổi 5: Chân (Leags Group)
  + buổi 6: Bụng và lưng dưới (Abdomen & Lower Back Group
"""


# truyền vào lần lượt là calo, số lần tập luyện trong tuần, thời gian cho mỗi lần tập luyện
def choose_exercises(calo_per_each_exercise_day, number_of_exercise_per_week, time_for_exercise, muscle_group = None):
    """
        Thời gian tập luyện tối thiểu 1 buổi:
        1 tiếng -> 4 bài
        1 tiếng 30 phút -> 8 bài
        2 tiếng -> 12 bài
    """
    number_of_exercise = 0
    if time_for_exercise == 60:
        number_of_exercise = 4
    elif time_for_exercise == 90:
        number_of_exercise = 8
    else:
        number_of_exercise = 12


    """ tính toán lịch tập 
    """
    if muscle_group is None:
        if number_of_exercise_per_week == 3:
            training_plan = {
                'Buổi 1': ['Ngực (Chest)', 'Lưng (Back group)', 'Cổ và vai (Neck & Shoulders 3 Group)'],
                'Buổi 2': ['Bắp tay (Biceps group)', 'Chân (Leags Group)',
                           'Bụng và lưng dưới (Abdomen & Lower Back Group)'],
                'Buổi 3': ['full body']
            }
        elif number_of_exercise_per_week == 5:
            training_plan = {
                'Buổi 1': ['Ngực (Chest)'],
                'Buổi 2': ['Lưng (Back group)'],
                'Buổi 3': ['Cổ và vai (Neck & Shoulders 3 Group)'],
                'Buổi 4': ['Bắp tay (Biceps group)', 'Cẳng tay (Foream Group)', 'Bắp tay sau (Triceps group)'],
                'Buổi 5': ['Chân (Leags Group)', 'Bụng và lưng dưới (Abdomen & Lower Back Group)']
            }
        elif number_of_exercise_per_week == 6:
            training_plan = {
                'Buổi 1': ['Ngực (Chest)'],
                'Buổi 2': ['Lưng (Back group)'],
                'Buổi 3': ['Cổ và vai (Neck & Shoulders 3 Group)'],
                'Buổi 4': ['Bắp tay (Biceps group)', 'Cẳng tay (Foream Group)', 'Bắp tay sau (Triceps group)'],
                'Buổi 5': ['Chân (Leags Group)'],
                'Buổi 6': ['Bụng và lưng dưới (Abdomen & Lower Back Group)']
            }
        else:
            print("Invalid number of exercise per week!")
            return None
    else:
        if number_of_exercise_per_week == 3:
            training_plan = {
                'Buổi 1': muscle_group,
                'Buổi 2': muscle_group,
                'Buổi 3': muscle_group
            }
        elif number_of_exercise_per_week == 5:
            training_plan = {
                'Buổi 1': muscle_group,
                'Buổi 2': muscle_group,
                'Buổi 3': muscle_group,
                'Buổi 4': muscle_group,
                'Buổi 5': muscle_group
            }
        elif number_of_exercise_per_week == 6:
            training_plan = {
                'Buổi 1': muscle_group,
                'Buổi 2': muscle_group,
                'Buổi 3': muscle_group,
                'Buổi 4': muscle_group,
                'Buổi 5': muscle_group,
                'Buổi 6': muscle_group
            }
        else:
            print("Invalid number of exercise per week!")
            return None

    for i, (day, muscle_groups) in enumerate(training_plan.items(), start=1):
        # Lọc bài tập theo traning plan
        if 'full body' in muscle_groups:
            filtered_exercises = [ex for ex in exercises]
        else:
            filtered_exercises = [ex for ex in exercises if ex.exercise_type in training_plan[day]]

        # Lấy ra random number_of_exercise bài tập
        selected_exercises = random.sample(filtered_exercises, number_of_exercise)

        # Tính toán số set tập cho tất cả các bài
        number_set_per_exercise = round(
            calo_per_each_exercise_day / sum([x.kcal_per_set for x in selected_exercises]))

        print(f"Lịch tập buổi {i}:")
        for ex in selected_exercises:
            print(f"Tên bài tập: {ex.exercise_name} Số set tập: {number_set_per_exercise} Số rep: {ex.reps_per_set} Thời gian {number_set_per_exercise * ex.time_per_set} phút Loại bài tập: {ex.exercise_type}")





calo_per_each_exercise_day = 482
number_of_exercise_per_week = 6
time_for_exercise = 90
choose_exercises(calo_per_each_exercise_day=calo_per_each_exercise_day, number_of_exercise_per_week=number_of_exercise_per_week, time_for_exercise=time_for_exercise)


""" tính toán lượng calo theo ngày 
công thức tính sẽ bằng lượng calo mỗi lần tập * số lần tạp trong tuần rồi chia cho 7
"""

def calo_per_day():
    return round(calo_per_each_exercise_day * number_of_exercise_per_week / 7)
print("---------------")
# print("Lượng calo tiêu thự từ bài tập theo ngày" , calo_per_day())


""" Trường hợp nó muốn thay đổi bài tập 
Mình sẽ phải cho nó chọn ra các vùng trên cơ thể mà nó muốn, chẳng hạn thu được một list là muscle_group 
"""

muscle_group = ['Bắp tay (Biceps group)', 'Cẳng tay (Foream Group)', 'Bắp tay sau (Triceps group)']
choose_exercises(calo_per_each_exercise_day=calo_per_each_exercise_day, number_of_exercise_per_week=number_of_exercise_per_week, time_for_exercise=time_for_exercise, muscle_group=muscle_group)



