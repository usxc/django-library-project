from django.db import models
import uuid

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
