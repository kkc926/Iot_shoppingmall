from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    read_cnt = models.IntegerField(blank=True, null=True, default=0)
    category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

    def __str__(self):
        return self.p_name


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    product_id = models.ForeignKey('Product', models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Qna(models.Model):
    qna_id = models.IntegerField(primary_key=True)
    qna_title = models.CharField(verbose_name='TITLE', max_length=50)
    product_id = models.ForeignKey(Product, models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    parent_id = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=45, blank=True, null=True)
    qna_create_date = models.DateTimeField(blank=True, null=True)
    qna_modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qna'

    def __str__(self):
        return self.qna_title


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    review_title = models.CharField(verbose_name='TITLE', max_length=50)
    product = models.ForeignKey('Product', models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=45, blank=True, null=True)
    file = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'

    def __str__(self):
        return self.review_title


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    product_id = models.ForeignKey('Product', models.CASCADE, blank=True, null=True)
    wish_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Inventory(models.Model):
    product_id = models.ForeignKey('Product', models.CASCADE)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=45, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

