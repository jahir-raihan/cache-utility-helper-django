from django.db import models


class ExampleModel(models.Model):
    field = models.CharFeild(max_len=20)
