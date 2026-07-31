import pyinputplus as pyip, os, json

class Student:
    def __init__(self , name , chinese, math , english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.totalScore = chinese + math + english

class Student_Grade_Organiser:
    def __init__(self):
        self.student_list = []

    def add_student(self , student):
        self.student_list.append(student)

    def check_score(self):
        if len(self.student_list) > 0:
            for i in self.student_list:
                print(f'{i.name}: \nChinese: {i.chinese}; \nMath: {i.math}; \nEnglish: {i.english}'
                      f'\nTotal: {i.totalScore}\n'
                      f'----------')
        else:
            print('No student found\n')

    def delete_student(self):
        if len(self.student_list) == 0:
            print('There is no student in your class\n')
        elif len(self.student_list) == 1:
            print(
                f'There is one student {self.student_list[0]} in your class. You cannot delete {self.student_list[0]} you are such evil\n')
        elif len(self.student_list) >= 2:
            names = [student.name for student in self.student_list]
            deletion = pyip.inputChoice(names,
                                        prompt='Who do you want to delete: ')
            for i in self.student_list:
                if i.name == deletion:
                    self.student_list.remove(i)
                    break

        print('ALL DONE\n')

    def change_score(self):
        names = [student.name for student in self.student_list]
        change_student = pyip.inputChoice(names, prompt = 'Enter the student that you wanna change the score.')
        for i in self.student_list:
            if i.name == change_student:
                change_subject = pyip.inputChoice(['chinese' , 'math' , 'english'] ,
                                                        prompt = 'Enter the subject that you wanna change the score.')
                new_score = pyip.inputInt(
                    prompt='New score: ',
                    min=0,
                    max=100)

                if change_subject == 'chinese':
                    i.chinese = new_score
                elif change_subject == 'math':
                    i.math = new_score
                elif change_subject == 'english':
                    i.english = new_score

                i.totalScore = i.chinese + i.math + i.english
                print('All Done\n')
                return
        print('Not found\n')

    def average_score(self):
        calculate_subject = pyip.inputChoice(['chinese' , 'math' , 'english' , 'totalscore'] ,
                                             prompt = 'Enter the subject that you wanna average the score.')
        result_score = 0
        if len(self.student_list) > 0:
            for i in self.student_list:
                if calculate_subject == 'chinese':
                    result_score += i.chinese
                elif calculate_subject == 'math':
                    result_score += i.math
                elif calculate_subject == 'english':
                    result_score += i.english
                elif calculate_subject == 'totalscore':
                    result_score += i.totalScore
            average_score = result_score / len(self.student_list)
            print(f'Average score of {calculate_subject}: {average_score}')
        else:
            print('There is no student found')
            return

    def saving_data(self):
        data = []

        for student in self.student_list:
            data.append({
                "name": student.name,
                "chinese": student.chinese,
                "math": student.math,
                "english": student.english
            })

        with open("studentData.json", "w") as f:
            json.dump(data, f, indent=4)

    def loading_data(self):
        try:
            with open("studentData.json", "r") as f:
                data = json.load(f)

            self.student_list = []

            for item in data:
                student = Student(
                    item["name"],
                    item["chinese"],
                    item["math"],
                    item["english"]
                )
                self.student_list.append(student)

        except FileNotFoundError:
            self.student_list = []

# initialise data
organiser = Student_Grade_Organiser()
organiser.loading_data()

# main loop
print('=====THIS IS A STUDENT GRADE ORGANISER=====')
actionMap = ['1' , '2' , '3' , '4' , '5' , '6']
while True:
    userAction = pyip.inputChoice(actionMap,
                                  prompt='What do you want to do?\n'
                                         '1. Add student\n'
                                         '2. check score\n'
                                         '3. delete student\n'
                                         '4. Change score\n'
                                         '5. Average score\n'
                                         '6. Quit\n')
    if userAction == '1':
        adding_name = pyip.inputStr(prompt = 'Please enter the student name.')
        adding_chinese_score = pyip.inputInt(prompt = 'Chinese score: ',
                                             min=0, max=100)
        adding_math_score = pyip.inputInt(prompt = 'Math score: ',
                                          min=0, max=100)
        adding_eng_score = pyip.inputInt(prompt = 'English score: ',
                                         min=0, max=100)

        adding_information = Student(adding_name, adding_chinese_score, adding_math_score, adding_eng_score)
        organiser.add_student(adding_information)
        organiser.saving_data()
        print('Student is added!\n')

    elif userAction == '2':
        organiser.check_score()

    elif userAction == '3':
        organiser.delete_student()
        organiser.saving_data()
        print('Student is deleted!\n')

    elif userAction == '4':
        organiser.change_score()
        organiser.saving_data()
        print('Student is changed!\n')

    elif userAction == '5':
        organiser.average_score()
        print('DONE!\n')

    elif userAction == '6':
        print('Thank You!')
        organiser.saving_data()
        break
