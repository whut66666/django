from django.shortcuts import render

# Create your views here.
def index(request):
    # 在这里写入业务逻辑
    # 在这里进行数据库的操作
    return render(request,'index.html')