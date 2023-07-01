# publish/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from publish.models import User  # 引入数据库 User 对象


@csrf_exempt  # 跨域设置
def register(request):  # 继承请求类
    if request.method == 'POST':  # 判断请求方式是否为 POST（此处要求为POST方式）
        username = request.POST.get('username')  # 获取请求体中的请求数据
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        user = User.objects.filter(username=username)
        if user:
            return JsonResponse({'errno': 1002, 'msg': "用户名重复"})
        if password_1 != password_2:  # 若两次输入的密码不同，则返回错误码errno和描述信息msg
            # 返还给前端处理结果信息
            return JsonResponse({'errno': 1003, 'msg': "两次输入的密码不同"})
        else:
            # 新建 User 对象，赋值用户名和密码并保存
            new_user = User(username=username, password=password_1)
            new_user.save()  # 一定要save才能保存到数据库中
            return JsonResponse({'errno': 0, 'msg': "注册成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if request.session.get('id'):
            return JsonResponse({'errno': 1004, 'msg': "不能重复登录"})
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['id'] = user.id
                print(user.id)
                return JsonResponse({'errno': 0, 'msg': "登录成功"})
            else:
                return JsonResponse({'errno': 1003, 'msg': "密码错误"})
        except User.DoesNotExist:
            return JsonResponse({'errno': 1002, 'msg': "用户不存在"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def logout(requset):
    if requset.method == 'POST':
        if requset.session.get('id'):
            del requset.session['id']
            return JsonResponse({'errno': 0, 'msg': "成功退出登录"})
        else:
            return JsonResponse({'errno': 1002, 'msg': "请先登录"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
