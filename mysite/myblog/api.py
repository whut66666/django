from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.contrib.auth.hashers import check_password,make_password

from django.contrib.auth import authenticate
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
    username = resquest.POST['username']
    password = resquest.POST['password']
    print(username,password)
    # print(resquest.POST)
    # 查询用户数据库
    user = User.objects.filter(username=username)
    if len(user)>0:
        auth_user = authenticate(username=username,password=password)
        if auth_user:
            token = Token.objects.update_or_create(user=user[0])
            token = Token.objects.get(user=user[0])
            print(token.key)
            data={
                'token':token.key
            }
            return Response(data)
        else:
            return Response('pwderr')
    else:
        return Response('nouser')

@api_view(['GET','POST'])
def toRegister(resquest):
    username = resquest.POST['username']
    password = resquest.POST['password']
    password2 = resquest.POST['password2']
    print(username,password,password2)
    # 判断用户是否存在
    user = User.objects.filter(username=username)
    if user:
        return Response('same')
    else:
        # 函数对密码加密
        newPwd = make_password(password,username)
        newUser = User(username=username,password=newPwd)
        newUser.save()
        return Response('success')
    return Response('ok')