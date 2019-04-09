from django.http import HttpResponse,JsonResponse
from lib.sms import send_sms
from lib.http import render_json
from common import error,keys
from django.core.cache import cache
from user.models import User

# Create your views here.
def submit_phone(request):
    '''获取短信验证码'''
    if not request.method == 'POST':
        return render_json('request method error',error.REQUEST_ERROR)
    phone = request.POST.get('phone')
    result,msg = send_sms(phone)
    return render_json(msg)

def submit_vcode(request):
    '''通过验证码登录注册'''
    if not request.method == 'POST':
        return render_json('request method error',error.REQUEST_ERROR)
    phone = request.POST.get('phone')
    #取出发送给手机的验证码
    vcode = request.POST.get('vcode')
    print(vcode)
    #取出缓存中的验证码
    cache_code = cache.get(keys.VCODE_KEY % phone)
    #对比验证码
    if vcode == cache_code:
        # users = User.objects.get(phonenum=phone)
        # if not users:
        #     User.objects.create(phonenum=phone,nickname=phone)
        user,_ = User.objects.get_or_create(phonenum=phone,nickname=phone)
        request.session['uid'] = user.id
        return render_json(user.to_string())
    else:
        return render_json('vcode error',error.VCODE_ERROR)


def get_profile(request):
    '''获取个人资料'''
    pass
def set_profile(request):
    '''修改个人资料'''
    pass
def upload_avatar(request):
    '''头像上传'''
    pass
