from django.shortcuts import render
from myblog.models import SiteInfo,Classes,Userinfo

# Create your views here.
def index(request):
    # 在这里写入业务逻辑
    # 在这里进行数据库的操作
    # 站点的基本信息
    siteinfo = SiteInfo.objects.all()[0]
    # 菜单分类
    classes = Classes.objects.all()
    # 全部用户
    userlist = Userinfo.objects.all()
    data = {
        "siteinfo":siteinfo,
        "classes":classes,
        "userlist":userlist
    }
    return render(request,'index.html',data)

def classes(request):
    # 站点的基本信息
    siteinfo = SiteInfo.objects.all()[0]
    # 菜单分类
    classes = Classes.objects.all()
    # 用交互获取id
    choose_id = request.GET['id']
    # 属于该课程的用户
    choosed = Classes.objects.get(id=choose_id)
    userlist = Userinfo.objects.filter(belong=choosed)
    data = {
        "siteinfo":siteinfo,
        "classes":classes,
        "userlist":userlist
    }
    return render(request,'classes.html',data)