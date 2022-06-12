from django.db import models

# Create your models here.

class img(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.TextField("姓名",default="")
    img = models.ImageField("图片",upload_to="./book")

class economy(models.Model):
        id = models.IntegerField(primary_key=True)
        intro=models.TextField("专业介绍",default="")
        book=models.TextField("书籍",default="")
        Class=models.TextField("课程介绍",default="")
        classurl=models.TextField("课程网址",default="")


class cs(models.Model):
        id = models.IntegerField(primary_key=True)
        intro=models.TextField("专业介绍",default="")
        book=models.TextField("书籍",default="")
        Class=models.TextField("课程介绍",default="")
        classurl=models.TextField("课程网址",default="")

class english(models.Model):
        id = models.IntegerField(primary_key=True)
        intro=models.TextField("专业介绍",default="")
        book=models.TextField("书籍",default="")
        Class=models.TextField("课程介绍",default="")
        classurl=models.TextField("课程网址",default="")

class managee(models.Model):
        user_id = models.IntegerField(primary_key=True)
        intro=models.TextField("专业介绍",default="")
        book=models.TextField("书籍",default="")
        Class=models.TextField("课程介绍",default="")
        classurl=models.TextField("课程网址",default="")

class manage(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.TextField("账号", default="")
    user_pwd = models.TextField("密码", default="")


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClassUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'class_user'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




