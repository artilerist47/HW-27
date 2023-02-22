from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    MALE = "male"
    FEMALE = "female"
    SEX = [(MALE, "Male"), (FEMALE, "Female")]

    MODERATOR = "moderator"
    MEMBER = "member"
    UNKNOWN = "unknown"
    ROLE = [(MODERATOR, MODERATOR), (MEMBER, MEMBER), (UNKNOWN, UNKNOWN)]

    sex = models.CharField(max_length=6, choices=SEX, default=MALE)
    role = models.CharField(max_length=15, choices=ROLE, default=UNKNOWN)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"