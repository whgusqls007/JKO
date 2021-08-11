from django.db import models

# Create your models here.
class busan(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]


class Ohmynews(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]


class Wikitree(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]


class Herald(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]


class Nocut(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]


class Joongang(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]


class Yeonhap(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]


class Donga(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]


class Hangook(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]


class Joseon(models.Model):
    _id = models.BigIntegerField()
    title = models.TextField()
    mainText = models.TextField()
    category = models.TextField()
    date = models.TextField()
    url = models.TextField()
    reporter = models.TextField()

    class Meta:
        ordering = ["-date"]
