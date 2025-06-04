from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="書籍ID")
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="本のタイトル")
    author = models.CharField(max_length=60, blank=True, null=True, verbose_name="著者名")
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True, verbose_name="ISBN")
    published_date = models.DateField(blank=True, null=True, verbose_name="出版日")
    description = models.TextField(blank=True, null=True, verbose_name="概要")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="書籍")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="利用者")
    rental_date = models.DateTimeField(default=timezone.now, blank=False, null=False, verbose_name="貸出日時")
    return_due_date = models.DateTimeField(blank=True, null=True, verbose_name="返却予定日時")
    returned_at = models.DateTimeField(blank=True, null=True, verbose_name="返却日時")
    is_returned = models.BooleanField(default=False, verbose_name="返却済みフラグ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="記録作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="記録更新日時")

    def __str__(self):
        return f"{self.book.title} - {self.user.username} ({'返却済' if self.is_returned else '貸出中'})"

    def mark_as_returned(self):
        self.is_returned = True
        self.returned_at = timezone.now()
        self.save(update_fields=['is_returned', 'returned_at', 'updated_at'])
    
    class Meta:
        verbose_name = "貸出記録"
        verbose_name_plural = "貸出記録"
        ordering = ['-rental_date']