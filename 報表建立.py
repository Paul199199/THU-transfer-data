def personal(name,dep,*score):
    print('Student:',name)
    print('Depatment:',dep)
    total = sum(score)
    if len(score) ==0:
      print('Student:{},Depatment:{}'.format(0,0))
    else:
      print('total score:{},Balance:{}'.format(total,total/len(score)))
personal('Paul','English',85,95,70)
personal('David','Math',100,90,80,70)
personal('Vicky','Chinese')

print()

def school(name,*score,teacher):
    print('Name:',name)
    print('Score:',sum(score))
    print('Teacher:',teacher)
school('John',60,70,68,90,teacher='Peter')

print()

def student(name,*score,teacher='David'):
    print('Name:',name)
    print('Score:',sum(score))
    print('Teacher:',teacher)
student('Mary',100,95,80)

print()

