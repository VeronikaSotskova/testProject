from django.contrib.auth.models import AbstractUser
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)


class Lesson(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, related_name="lessons", related_query_name="lessons", on_delete=models.CASCADE)

    def save(self):
        if self.parent and self.parent.parent:
            raise Exception()
        super(Lesson, self).save()


class User(AbstractUser):
    viewed_lessons = models.ManyToManyField(Lesson, related_name="users", related_query_name="users",
                                            blank=True)
