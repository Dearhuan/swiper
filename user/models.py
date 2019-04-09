from django.db import models
import datetime
# Create your models here.
class User(models.Model):
    SEX = (
        ('male','男'),
        ('female','女')
    )
    phonenum = models.CharField(max_length=20,unique=True,verbose_name='手机号')
    nickname = models.CharField(max_length=32,unique=True,verbose_name='昵称')
    sex = models.CharField(max_length=8,choices=SEX,verbose_name='性别')
    birth_year = models.IntegerField(default=2000,verbose_name='出生年')
    birth_month = models.IntegerField(default=1,verbose_name='出生月')
    birth_day = models.IntegerField(default=1,verbose_name='出生日')
    avatar = models.CharField(max_length=200,verbose_name='个人形象')
    location = models.CharField(max_length=20,verbose_name='常居地')

    @property
    def age(self):
        today = datetime.date.today()
        birth_day = datetime.date(self.birth_year,self.birth_month,self.birth_day)
        time_delta = today - birth_day
        return time_delta.days // 365

    def to_string(self):
        return {
            'phonenum':self.phonenum,
            'nickname':self.nickname,
            'sex':self.sex,
            # 'birth_year':self.birth_year,
            # 'birth_month':self.birth_month,
            # 'birth_day':self.birth_day,
            'age':self.age,
            'avatar':self.avatar,
            'location':self.location,
        }
