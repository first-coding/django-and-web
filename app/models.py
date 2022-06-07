from django.db import models

# Create your models here.


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


class manage(models.Model):
        id = models.IntegerField(primary_key=True)
        intro=models.TextField("专业介绍",default="")
        book=models.TextField("书籍",default="")
        Class=models.TextField("课程介绍",default="")
        classurl=models.TextField("课程网址",default="")
