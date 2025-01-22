from django.db import models

class Product(models.Model):
    """商品模型類"""
    name = models.CharField(max_length=200, verbose_name='商品名稱')
    description = models.TextField(verbose_name='商品描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='價格')
    stock = models.IntegerField(default=0, verbose_name='庫存數量')
    image = models.ImageField(upload_to='products/', verbose_name='商品圖片')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='創建時間')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新時間')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

    def __str__(self):
        return self.name 