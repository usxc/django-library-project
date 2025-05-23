from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    student_id = models.CharField(max_length=8, unique=True, blank=False, null=False, verbose_name="学籍番号") # 必須入力
    first_name = models.CharField(max_length=60, blank=False, null=False, verbose_name="名") # 必須入力
    last_name = models.CharField(max_length=60, blank=False, null=False, verbose_name="姓") # 必須入力
    email = models.EmailField(unique=True, blank=True, null=True, verbose_name="メールアドレス") # 任意入力
    username = models.CharField(max_length=60, unique=True, blank=True, null=True, verbose_name="ユーザー ネーム") # 任意入力
    
    USERNAME_FIELD = student_id

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        ordering = ['student_id']

    def __str__(self):
        display_name = f"{self.last_name}{self.first_name}".strip()
        return f"{self.student_id}_{display_name}"
    
    def get_full_name(self):
        full_name = f"{self.last_name}{self.first_name}".strip()
        return full_name
    
    def get_short_name(self):
        return self.first_name