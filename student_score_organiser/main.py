import pyinputplus as pyip

student = []

def add_student():
    studentName = pyip.inputStr(prompt = 'Student Name: ')
    chineseScore = pyip.inputFloat(prompt = 'Student Chinese Score: ')
    mathScore = pyip.inputFloat(prompt = 'Student Math Score: ')
    englishScore = pyip.inputFloat(prompt = 'Student English Score: ')
    print('\n')
    student.append({'name':studentName ,
                    'Chinese':chineseScore,
                    'Math':mathScore,
                    'English':englishScore,
                    'Total':chineseScore + mathScore + englishScore})

def check_student():
    for i in student:
        for k , v in i.items():
            if k == 'name':
                print(f'\n{k} : {v}')
            else:
                print(f'{k} : {v}')
    print('\n')

def delete_student():
    deadStudent = pyip.inputStr(prompt = 'Which student you wan to delete?: ')
    for i in student:
        if i['name'] == deadStudent:
            student.remove(i)
    print('All Done\n')

def change_score():
    changeName = pyip.inputStr(prompt = 'Which student you wan to change?: ')
    changeSubject = pyip.inputChoice(['Chinese' , 'Math', 'English'],
                                     prompt = 'Which subject you wan to change?: ')
    changeTarget = pyip.inputFloat(prompt = 'New Score: ')
    for i in student:
        if i['name'] == changeName:
            i[changeSubject] = changeTarget
    print('All Done\n')

def average_score():
    targetSubject = str(input('Which subject you want to average?: '))
    result = 0
    for i in student:
        for k,v in i.items():
            if k == targetSubject:
                result += v
    average = result / len(student)
    print(f'\n{targetSubject} average score: {average}\n')

# mia loop
print('======This is a student score organiser======')
while True:
    actionMap = ['1','2','3','4','5','6']
    userAction = pyip.inputChoice(actionMap,prompt = 'What do you want to do:\n'
                                                 '1.Add student\n'
                                                 '2.Delete student\n'
                                                 '3.Change score\n'
                                                 '4.Check score\n'
                                                 '5.Calculate average score\n'
                                                 '6.Quit\n')
    if userAction == '1':
        add_student()
    elif userAction == '2':
        delete_student()
    elif userAction == '3':
        change_score()
    elif userAction == '4':
        check_student()
    elif userAction == '5':
        average_score()
    elif userAction == '6':
        break

