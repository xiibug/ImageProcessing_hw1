import os
import sys

############ CONSTANTS
# ONLINE
STUDENTS_PER_GROUP = ('12', '22') # кол-во студентов в группе 12 или 22
TEACHER_SALARY = 35000  # руб
TAXES = 0.3  # начисления на оплату труда 30%
NDS = 0.13  # подоходный налог 13%
INTERNET = 10000  # руб за интернет
_1C = 15000  # руб 1C
OTHER_EXPENSES = 50000
#

# OFFLINE
SQUARE_PER_TEACHER = 4  # 4 кв. м. на препода
SQARE_PER_STUD = 2  # 1 кв. м. на человека и 1 кв. м. на окружение
SQUARE_COMM = 40  # 2 * 20 кв. м. общих комнат
RENT = 500  # 500 руб за кв. м. за помещения
COMMUNAL = 100  # 100 руб за кв. м. за коммунальные услуги
OTHERS_ROOMS = 0.05  # 5% на коридоры туалет и тд
#
############

# AVERAGE SALARIES в рублях
average_salaries = {
    'online': {
        'accountant': 100000,  # 2 * 50000 бухгалтеры
        'sys_admin': 60000,  # сисадмин
        'met': 70000  # 2 * 35000 методисты
    },
    'offline': {
        'security': 160000,  # 4 * 40000 охранники
        'cleaning': 40000,  # 2 * 20000 уборщицы
        'cloakroomer': 20000  # 20000 гардеробщицы
    }
}

# 6 - ти дневная рабочая неделя
# каждый препод ведет максимум 3 предмета
# 1 препод ведет 10 пар в неделю
# каждый препод ведет 2 пары в день
# 1 курс - 3 пары каждый день, 9 предметов в год
# 2 курс - 4, 13
# 3 курс - 3, 10
# 4 курс - 3, 12
# 4 группы в каждом курсе
# в среднем 2 группы у каждого препода на паре
# 1 курс - нужно 3*2=6 преподов
# 2 курс - 4*2=8
# 3 курс - 3*2=6
# 4 курс - 4*2=8
# Всего преподов:
num_prep = 30
# Всего студентов одновременно на парах в 1 день:
# (среднее кол-во человек в группе на 1 курсе + на втором + на 3 + на 4) * 2
num_stud_per_day_in_week = 0
num_stud = 0
studs = []

def main():
    global num_prep, num_stud_per_day_in_week, num_stud, studs
    ONLINE = (INTERNET + _1C) * 12
    
    for key in average_salaries['online'].keys():
        ONLINE += average_salaries['online'][key] * 12 * (1 + TAXES) * (1 + NDS)
    OFFLINE = ONLINE
    for key in average_salaries['offline'].keys():
        OFFLINE += average_salaries['offline'][key] * 12 * (1 + TAXES) * (1 + NDS)

    with open(os.path.abspath('') + '\students.txt', 'r') as f:
        for i in range(4):
            studs.append(f.readline().split('\n')[0].split(':')[1][1:].split(' '))

        for i in range(4):
            average = 0
            for j in range(4):
                if studs[i][j] not in STUDENTS_PER_GROUP:
                    raise ValueError('Number of students per group must be 12 or 22')
                num_stud += int(studs[i][j])
                average += int(studs[i][j])
            num_stud_per_day_in_week += average//4 * 2

    ONLINE += num_prep * TEACHER_SALARY * 12 * (1 + TAXES) * (1 + NDS)
    OFFLINE += num_prep * TEACHER_SALARY * 12 * (1 + TAXES) * (1 + NDS)
    OFFLINE += (num_stud_per_day_in_week * SQARE_PER_STUD + num_prep *
                SQUARE_PER_TEACHER + SQUARE_COMM) * (RENT + COMMUNAL) * (1 + OTHERS_ROOMS) * 12 + OTHER_EXPENSES
 
    print('Стоимость онлайн обучения на 1 студента за 1 год: ' + str(ONLINE//num_stud) + ' рублей')
    print('Стоимость офлайн обучения на 1 студента за 1 год: ' + str(OFFLINE//num_stud) + ' рублей')


if __name__ == '__main__':
    sys.exit(main() or 0)