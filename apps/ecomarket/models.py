from django.db import models


class Category(models.Model):
    image = models.ImageField(upload_to='category/', verbose_name="Изображения")
    name = models.CharField(max_length=30, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    image = models.ImageField(upload_to="product/", verbose_name="Изображения")
    name = models.CharField(max_length=30, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Корзина"

    def __str__(self):
        return f"{self.product}"


class CartItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} - {self.quantity}"


class Info(models.Model):
    image = models.ImageField(upload_to="info/", verbose_name="Изображения")
    text = models.TextField()
    whatsapp_contact = models.CharField(max_length=20, blank=True, null=True)
    inst_contact = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.text}"
