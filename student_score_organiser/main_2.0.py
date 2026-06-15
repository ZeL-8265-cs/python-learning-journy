import pyinputplus as pyip, os

student = [{'Name' : 'Alice' , 'Score' : {'Chinese' : 40,
                                          'Math' : 50,
                                          'English' : 60}}]
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
os.chdir(desktop)
# student = [{'Name' : xx , 'Score' : {'Math' : 40 , 'English' : 30}
#                                                       }
#                                                               ]

# adding student
def add_student():
    studentName = pyip.inputStr(prompt='Student\'s name: ')
    chineseScore = pyip.inputFloat(prompt='Student\'s Chinese score: ')
    mathScore = pyip.inputFloat(prompt='Student\'s Math score: ')
    englishScore = pyip.inputFloat(prompt='Student\'s English score: ')
    student.append({'Name' : studentName,'Score' : {'Chinese' : chineseScore,
                                                     'Math' : mathScore,
                                                     'English' : englishScore,
                                                    'Total' : chineseScore + mathScore + englishScore}})
    print(f'All Done\n')

# check score
def check_student():

    for i in student:
        for k , v in i.items():
            if k == 'Name':
                print(f'\n{k} : {v}')
            else:
                for j , s in v.items():
                    print(f'{j} : {s}')

    print(f'All Done\n')

# delete student
def delete_student():
    if len(nameList) == 0:
        print('There is no student in your class\n')
    elif len(nameList) == 1:
        print(f'There is one student {nameList[0]} in your class. You cannot delete {nameList[0]} you are such evil\n')
    elif len(nameList) >= 2:
        deletion = pyip.inputChoice(nameList,
                     prompt = 'Who do you want to delete: ')
        for i in student:
            if i['Name'] == deletion:
                student.remove(i)
        print(f'All Done\n')

# change score
def change_score():
    change_student = pyip.inputChoice(nameList,
                                      prompt = 'Who do you want to change: ')
    change_subject = pyip.inputChoice(subjectList,
                                      prompt = 'Which subject do you want to change: ')
    new_score = pyip.inputFloat(prompt='New score: ')
    for i in student:
        if i['Name'] == change_student:
            i['Score'][change_subject] = new_score
    print(f'All Done\n')

# average score
def average_score():
    calculate_subject = pyip.inputChoice(subjectList,
                        prompt = 'Which subject(or total score) do you want to average: ')
    result = 0
    for i in student:
        for k, v in i['Score'].items():
            if k == calculate_subject:
                result += v
    average = result / len(student)
    print(f'The average score of {calculate_subject}: {average}\n')

# main loop
print('======This is a lovely score organizer======')
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
    nameList = [s['Name'] for s in student]
    subjectList = list(student[0]['Score'].keys())

    if userAction == '1':
        add_student()
    elif userAction == '2':
        check_student()
    elif userAction == '3':
        delete_student()
    elif userAction == '4':
        change_score()
    elif userAction == '5':
        average_score()
    elif userAction == '6':
        break
