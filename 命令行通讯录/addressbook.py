
'''
终端通讯录，可用来添加、查询、删除通讯录好友及电话。
创建一个类来表示一个人的信息。使用字典存储每个人的对象，名字作为键。
使用cpickle模块永久地把这些对象存储下来。
使用字典内建的方法添加、删除修改人员信息。
'''

import pickle as cpk 
import os

'''创建字典用来存储通讯录信息'''
personDictionary= {'name':{'relationship':'','tel':''}}
relationshipList=['家人','朋友','同事']

#人员类，包含姓名、关系、电话三个属性
class Person:
    def __init__(self,name,relationship= relationshipList[1],tel='None'):
 ##        Person.name= name
 ##        Person.relationship= relationship
 ##        Person.tel= tel
        personDictionary[name]= {'relationship':relationship,'tel':tel}
class Operation:
    def Addperson():
    	addname= input('请输入姓名：')
    	addrelationship= int(input('请选择分组(0:家人,1:朋友,2:同事):'))
    	addtel= input('请输入电话：')
    	Person(addname,relationshipList[addrelationship],addtel)
    def Addrelationship():
        pass
    def Delperson():
        name= input('请输入要删除的联系人姓名：')
        del personDictionary[name]
    def Delrelationship():
        pass
    def Search():
        name= input('请输入要查找的联系人的姓名：')
        if name in personDictionary:
            print('姓名：%s,关系：%s,电话：%s' %(name,personDictionary[name]['relationship'],personDictionary[name]['tel']))
        else:
            print('联系人不存在。')
    def Quit():
        running= False
    def SaveQuit():
        f= open(addressbookFile,'wb')
        cpk.dump(personDictionary,f)
        f.close()
        running= False
# 1.程序运行
running= True
# 2.判断通讯录文件是否存在
addressbookFile= 'addressbook.data'
# 3.如果存在，将文件读取到personDictionary字典中
if os.path.exists(addressbookFile):
    f= open(addressbookFile,'rb')
    
    personDictionary= cpk.load(f)
# 4.如果不存在，提示并创建
else:
    jCommand= input('未找到通讯录文件，是否创建？yes/no')
    if jCommand== 'yes':
        f= open(addressbookFile,'wb')
        cpk.dump(personDictionary,f)
        f.close()
    elif jCommand== 'no':
        running= False
# 5.while循环等待读取指令
while running:
    command= input('请输入指令：')
    # 6.如果指令为addperson，添加通讯录人员
    if command== 'addperson':
    	Operation.Addperson()
    	continue
    # 7.如果指令为addrelationship，添加通讯录人员关系
    elif command== 'addrelationship':
        Operation.Addrelationship()
        continue
    # 8.如果指令为delperson，删除通讯录人员
    elif command== 'delperson':
        Operation.Delperson()
        continue
    # 9.如果指令为delrelationship，删除通讯录人员关系
    elif command== 'delrelationship':
        Operation.Delrelationship()
        continue
    # 10.如果指令为search，查找通讯录人员
    elif command== 'search':
        Operation.Search()
        continue
    # 11.如果指令为quit，不保存退出程序
    elif command== 'quit':
        Operation.Quit()
        break
    # 12.如果指令为sq，保存更改并退出程序
    elif command== 'sq':
        Operation.SaveQuit()
        break
    else:
        print('未找到指令！')
        continue
