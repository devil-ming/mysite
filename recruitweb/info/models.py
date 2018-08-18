from django.db import models

# Create your models here.
class User(models.Model):
    gender = (('male','男'),
              ('female','女'))
    uname = models.CharField(max_length=32,unique=True,verbose_name="用户名")
    usex = models.CharField(max_length=32,choices=gender,default='男',verbose_name="性别")
    upwd = models.CharField(max_length=128,verbose_name="密码")
    uemail = models.EmailField(unique=True,verbose_name="邮箱")
    c_time = models.DateTimeField(auto_now_add=True,verbose_name="注册时间")
    uphone = models.CharField(max_length=11,verbose_name="电话")
    isActive = models.BooleanField(default=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.uname

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.uname + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"

