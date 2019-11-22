import random
import string
from datetime import date
import random
from exam import *

def get_rand_day():
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day

def get_rand_string(len):
    N = len
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def get_districts():
    districts = []
    num = 10
    for i in num:
        district['name'] = get_rand_string(10)
        district['id'] = i+1
        districts.append(district)
    return districts

def get_schools(districts):
    schools = []
    num = 30
    for i in num:
        school['id'] = i+1
        district = districts[random.randint(0,len(districts)-1]
        school['district_id'] = district['id']
        school['name'] = get_rand_string(10)
        schools.append(school)
    return schools

def get_classrooms(schools):
    classrooms = []
    num = 100
    for i in num:
        classroom['id'] = i+1
        school = schools[random.randint(0,len(schools)-1]
        classroom['school_id'] = school['id']
        classroom['capacity'] = random.randint(5, 20)
        classrooms.append(school)
    return classrooms

def get_students(schools):
    students = []
    num = 30
    for i in num:
        student['id'] = i+1
        student['first_name'] = get_rand_string(10) 
        student['last_name'] = get_rand_string(10) 
        school = schools[random.randint(0,len(schools)-1]
        student['school_id'] = school['id']
        students.append(student)
    return students

def get_subjs():
    subjs = []
    num = 10
    for i in num:
        subj['description'] = get_rand_string(40)
        subj['id'] = i+1
        subj['min_grade'] = random.randint(0, 20)
        subj.append(subj)
    return subjs

def get_req_subjs(subjs):
    req_subjs = []
    for subj in subjs:
        if (random.randint(0, 2) == 0):
            req_subj['subj_id'] = subj['id']
            req_subjs.append(req_subj)
    return req_subjs

def get_student_subjs(students, subjs, req_subjs): 
    student_subjs = []
    for student in students:
        for subj in subjs:
            if (random.randint(0, 4) != 0):
                student_subj['student_id'] = student['id']
                student_subj['subj_id'] = subj['id']
                student_subjs.append(student_subj)
    return student_subjs

def get_exams(subjs):
    exams = []
    for subj in subjs:
       exam1['subj_id'] = subj['id']
       exam1['day'] = get_rand_day()
       exams.append(exam1)
       exam2['subj_id'] = subj['id']
       exam2['day'] = get_rand_day()
       exams.append(exam2)
    return exams

def fill_data():
    districts = get_districts()
    schools = get_schools(districts)
    classrooms = get_classrooms(schools)
    students = get_students(schools)
    subjs = get_subjs()
    req_subjs = get_req_subjs(subjs)
    student_subjs = get_student_subjs(students, subjs, req_subjs)
    exams = get_exams(subjs)

    #  grades, rers, student_rers, exam_distribs, student_distrib
    exam_distribs = []
    for classroom in classrooms:
        for exam in exams:
            exam_distrib = {}
            exam_distrib['id'] = len(exam_distribs) + 1
            exam_distrib['classroom_id'] = classroom['id']
            exam_distrib['exam_id'] = exam['id']
            exam_distribs.append(exam_distrib)

    student_distribs = []
    grades = []
    for student in students:
        student_subjs = {}
        for i in student_subjs:
            if (i['student_id'] == student['id']):
                student_subjs = i
                break

        student_distrib = {}
        for subj in student_subjs:
            subj_exam = {}
            dec31 = datetime.strptime('Dec 31 2019', '%b %d %Y').date()
            subj_exam['day'] = dec31
            for exam in exams:
                if (exam['subj_id'] == subj['id'] and \
                    exam['day'] <= subj_exam['day']):
                    subj_exam = exam

            exam_distrib = {}
            for i in exam_distribs:
                if (i['exam_id'] == subj_exam['id']):
                    student_distrib['student_id'] = student['id']
                    student_distrib['exam_distrib_id'] = i['id'] 

            student_distribs.append(student_distrib)

            grade = {}
            grade['student_id'] = student['id']
            grade['exam_id'] = subj_exam['id']
            grade['grade'] = random.randint(0, 100)
            grades.append(grade)




    for district in districts:
        district_add_raw(district['name'])

    for school in schools:
        school_add_raw(school['district_id'])

    for classroom in classrooms:
        classroom_add_raw(classroom['school_id'], classroom['capacity'])

    for student in students:
        student_add_raw(student['first_name'],
                        student['last_name'],
                        student['school_id'])

    for subj in subjs:
        subj_add_raw(subj['desciption'], subj['min_grade'])

    for student_subj in student_subjs:
        student_subj_add_raw(student_subj['student_id'],
                             student_subj['subj_id'])

    for req_subj in req_subjs:
        req_subj_add_raw(req_subj['subj_id'])

    for exam in exams:
        exam_add_raw(exam['subj_id'], exam['day'])

    for grade in grades:
        grade_add_raw(grade['student_id'], grade['exam_id'],
                      grade['grade'])

    for rer in rers:
        rer_add_raw(rer['description'])

    for student_rer in student_rers:
        student_rer_add_raw(student_rer['student_id'],
                            student_rer['rer_id'])

    for exam_distrib in exam_distribs:
        exam_distrib_add_raw(exam_distrib['classroom_id'],
                             exam_distrib['exam_id'])

    for student_distrib in student_distribs:
        student_distrib_add_raw(student_distrib['student_id'],
                                student_distrib['exam_distrib_id'])
