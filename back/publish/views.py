# publish/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from publish.models import User  # 引入数据库 User 对象
from django.core.mail import send_mail, EmailMessage
from django.utils import timezone
import random

verification_codes = {}


@csrf_exempt  # 跨域设置
def register(request):  # 继承请求类
    if request.method == 'POST':  # 判断请求方式是否为 POST（此处要求为POST方式）
        username = request.POST.get('username')  # 获取请求体中的请求数据
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        email = request.POST.get('email')
        verification_code = request.POST.get('verification_code')
        isEmail = request.POST.get('isEmail')
        user = User.objects.filter(username=username)
        if user:
            return JsonResponse({'errno': 1002, 'msg': "用户名重复"})

        if password_1 != password_2:  # 若两次输入的密码不同，则返回错误码errno和描述信息msg
            # 返还给前端处理结果信息
            return JsonResponse({'errno': 1003, 'msg': "两次输入的密码不同"})

        if isEmail == 'true':
            if not verification_code:
                return JsonResponse({'errno': 1004, 'msg': "请提供验证码！"})

            verification_info = verification_codes.get(email)
            if not verification_info or verification_info['code'] != verification_code:
                return JsonResponse({'errno': 1005, 'msg': "验证码无效！"})

            current_time = timezone.now()
            expiration_time = verification_codes[email]['expiration_time']
            if current_time > expiration_time:
                return JsonResponse({'errno': 1006, 'msg': "验证码已过期！"})

            del verification_codes[email]

        # 新建 User 对象，赋值用户名和密码并保存
        new_user = User(username=username, password=password_1, email=email)
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


@csrf_exempt
def sendcode(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('email')  # 从 POST 请求参数中获取收件人邮箱地址
        if recipient_email:
            verification_code = generate_verification_code()  # 生成验证码
            subject = '验证码'
            message = f'您的验证码是：{verification_code}'
            sender_email = '1158152324@qq.com'  # 发件人邮箱地址，替换为你自己的邮箱地址
            sender_name = '验证码'  # 发件人名称，替换为你想要显示的名称

            email = EmailMessage(
                subject, message, sender_email, [recipient_email])
            email.from_email = f'{sender_name} <{sender_email}>'
            email.send()
            expiration_time = timezone.now() + timezone.timedelta(seconds=30)  # 设置验证码的有效期为两分钟
            verification_codes[recipient_email] = {
                'code': verification_code, 'expiration_time': expiration_time}
            return JsonResponse({'success': True, 'message': '验证码已发送', 'expiration_time': expiration_time.timestamp()})
        else:
            return JsonResponse({'success': False, 'message': '未提供有效的邮箱地址！'})


def generate_verification_code():
    code = ''
    for _ in range(6):
        code += str(random.randint(0, 9))
    return code
