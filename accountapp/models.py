from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    #text 한 줄, charField는 문자열, null은 없어도 되는 정보인지 물어보는 것
    text = models.CharField(max_length=255, null=False)
