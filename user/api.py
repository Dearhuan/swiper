from lib.sms import send_sms
from lib.http import render_json
from common import error,keys
from django.core.cache import cache
from user.models import User
from user.forms import ProfileForm
from user import logics

# Create your views here.
def submit_phone(request):
    '''获取短信验证码'''
    if not request.method == 'POST':
        return render_json('request method error',error.REQUEST_ERROR)
    phone = request.POST.get('phone')
    result,msg,vcode = send_sms(phone)
    print(vcode)
    return render_json(msg)

def submit_vcode(request):
    '''通过验证码登录注册'''
    if not request.method == 'POST':
        return render_json('request method error',error.REQUEST_ERROR)
    phone = request.POST.get('phone')
    #取出发送给手机的验证码
    vcode = request.POST.get('vcode')
    print(phone)
    # print(vcode)
    #取出缓存中的验证码
    cache_code = cache.get(keys.VCODE_KEY % phone)
    print(cache_code)

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
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)
    profile = user.profile

    return render_json(profile.to_string())

def set_profile(request):
    '''修改个人资料'''
    if not request.method == 'POST':
        return render_json('request method error',error.REQUEST_ERROR)

    uid = request.session.get('uid')
    profile_form = ProfileForm(request.POST)

    if profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.id = uid
        profile.save()

        return render_json('modify success')
    else:
        return render_json(profile_form.errors,error.FORM_ERROR)


def upload_avatar(request):
    '''头像上传'''
    if not request.method == 'POST':
        return render_json('request method error',error.REQUEST_ERROR)

    avatar = request.FILES.get('avatar')
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)

    logics.upload_avatar.delay(user,avatar)
    return render_json('upload success')