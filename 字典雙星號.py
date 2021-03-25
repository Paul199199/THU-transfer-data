# 字典雙星號 **字串
def student(**score):
    print('Score:',score)
student(Tom=92,May=100,David=97)

print()
#進階雙星號運用
def subject(name,**score):
    print('Name:',name)
    print('Score:',score)
subject('Tom',Math=100,Chi=99,Eng=96)

print()

# 字典混搭運用
def school(year,*subject,**score):#此段為元組
    print('學期: ',year)
    print('必修科目有: ')
    for item in subject:
        print(item,end=',')
    print()
    for name in sorted(score):#此段為字典
        print('{0:8s}{1}'.format(name,score[name]))
    print('-'*30)
    low={k:v for k,v in score.items() if v<60}
    print('不及格有{}人'.format(len(low)))
    print(low)
school(110,'Math','Chi','Eng',John=90,May=100,David=30,Tom=50)

print()
