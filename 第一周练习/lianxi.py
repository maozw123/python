'''编写学员管理系统
学员信息包含：学号，姓名，性别，年龄，身高；

进入系统：提示欢迎进入学员管理系统（主界面）
1、查询学员信息S
2、增加学员信息A
3、删除学员信息D
4、修改学员信息E
5、退出Q

一、查询学员功能：
 功能1、查询所有学员信息：显示所有学员信息
 功能2、查询指定学员信息：根据输入的学号显示学员信息，学号不存在提示学员不存在


二、添加学员功能
提示用户输入学员信息，输入成功后提示添加成功。否则提示添加失败，进入程序主界面。


三、删除学员信息
提示用户“请输入要删除的学员学号”,输入学号后根据学号删除学员信息。删除成功，提示“删除成功”，进入程序主界面。删除失败提示“删除失败”要求用户重新输入学员学号：


四、修改学员信息
要求用户输入学员学号，和新的学员信息。根据用户输入的学员学号，修改该学号所对应的的学员信息。


五、退出系统
退出系统。'''''

# 定义一个字典   嵌套字典
# student_id=input("请输入学号:")
# name=input('请输入姓名:')
# sex=input('请输入性别:')
# age=input('请输入年龄:')
# height=input('请输入身高:')
student = {'1001': {'name': '张三', 'age': '18', 'sex': '男', 'height': '178'},
           '1002': {'name': '李四', 'age': '19', 'sex': '男', 'height': '177'}}
# dict2 = {}
# student_id = input('请输入学号：')
# dict2.setdefault(student_id, {})['name'] = input('请输入姓名：')
# dict2.setdefault(student_id, {})['age'] = input('请输入年龄：')
# dict2.setdefault(student_id, {})['sex'] = input('请输入性别：')
# dict2.setdefault(student_id, {})['height'] = input('请输入身高：')
# print(dict2)
# #
# student.update(dict2)
# print(student)
a = input('请输入S,A,D,E,Q\n')
# 一、查询学员功能：
#  功能1、查询所有学员信息：显示所有学员信息
#  功能2、查询指定学员信息：根据输入的学号显示学员信息，学号不存在提示学员不存在
# if a=='S':
#     s1=input('请输入1or2,（功能1查询所有学员信息，功能二查询指定学员信息）:')
#     if s1=='1':
#         for key,value in student.items():
#             print(key,value)
#     elif s1=='2':
#         student_id=(input("请输入学号:"))
#         for key,value in student.items():
#             if key==student_id:
#                 print(key,value)
#                 break
#         else:
#             print('学号不存在')

# 添加学生信息二、添加学员功能
# 提示用户输入学员信息，输入成功后提示添加成功。否则提示添加失败，进入程序主界面。
# while a == 'A':
#     dict2 = {}
#     print('要添加的学员信息')
#     student_id = input('请输入学号：')
#     if student.get(student_id):
#         print('学号存在，请重新输入')
#
#     else:
#         dict2['name'] = input('请输入姓名：')
#         dict2['age'] = input('请输入年龄：')
#         dict2['sex'] = input('请输入性别：')
#         dict2['height'] = input('请输入身高：')
#         student[student_id] = dict2
#         print('添加成功')
#         break
# print(student)

# 三、删除学员信息
# 提示用户“请输入要删除的学员学号”,输入入学号后根据学号删除学员信息。删除成功，提示“删除成功”，进入程序主界面。
# # 删除失败提示“删除失败”要求用户重新输学员学号：
# if a == 'D':
#     n = 1
#     while 1:
#         student_id = input("请输入学号:")
#         if student.get(student_id):
#             student.pop(student_id)
#             print('删除成功')
#             break
#         else:
#             print('删除失败')
# 四、修改学员信息
# 要求用户输入学员学号，和新的学员信息。根据用户输入的学员学号，修改该学号所对应的的学员信息。
# while a == 'E':
#     dict2 = {}
#     print('要修改的学员信息')
#     student_id = input('请输入要修改学号：')
#     if student.get(student_id):
#         dict2['name'] = input('请输入姓名：')
#         dict2['age'] = input('请输入年龄：')
#         dict2['sex'] = input('请输入性别：')
#         dict2['height'] = input('请输入身高：')
#         student[student_id] = dict2
#         print('修改成功')
#         break
#     else:
#         print('学号不存在，请重新输入')
# print(student)
