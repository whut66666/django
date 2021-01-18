from rest_framework.decorators import api_view
from rest_framework.response import Response
from myblog.models import Classes,Userinfo
from myblog.toJson import Classes_data,Userinfo_data
import json

@api_view(['GET','POST'])
def api_test(request):
    classes = Classes.objects.all()
    # classes_data = Classes_data(classes,many=True)
    # userlist = Userinfo.objects.all()
    # userinfo_data = Userinfo_data(userlist,many=True)

    # data = {
    #     'classes':classes_data.data,
    #     'userlist':userinfo_data.data
    # }
    data = {
        'classes':[]
    }
    for c in classes:
        data_item = {
            'id':c.id,
            'text':c.text,
            'userlist':[]
        }
        userlist = c.userinfo_classes.all()
        for user in userlist:
            user_data = {
                'id':user.id,
                'nickName':user.nickName,
                'headImg':str(user.headImg)
            }
            data_item['userlist'].append(user_data)
        data['classes'].append(data_item)
    return Response(data)

@api_view(['GET'])
def getMenuList(resquest):
    allClasses = Classes.objects.all()

    # 整理数据到json
    data = []
    for c in allClasses:
        # 设计单条数据的结构
        data_item = {
            'id':c.id,
            'text':c.text
        }
        data.append(data_item)
    return Response(data)

@api_view(['GET'])
def getUserList(resquest):
    # 从前端发送来的data数据用GET来进行选择
    menuId = resquest.GET['id']
    print(menuId)
    menu = Classes.objects.get(id=menuId)
    print(menu)
    userlist = Userinfo.objects.filter(belong=menu)
    print(userlist)

    # 开始整理数据列表
    data = []
    for user in userlist:
        data_item = {
            'id':user.id,
            'headImg':str(user.headImg),
            'nickName':user.nickName
        }
        data.append(data_item)
    return Response(data)


@api_view(['POST'])
def toLogin(resquest):
    # username = resquest.POST['username']
    # password = resquest.POST['password']
    # print(username,password)
    print(resquest.POST)
    return Response('ok')