_students={'Иван','Семен','Никита'}
_grades =[[3,4,3,5,4],[5,5,5,5],[3,4,3,2,2]]
_grade=[sum(_grades[0])/len(_grades[0]),
        sum(_grades[1])/len(_grades[1]),
        sum(_grades[2])/len(_grades[2])]
_students_sort=sorted(_students)
_jornal=dict(zip(_students_sort,_grade))
print(_jornal)