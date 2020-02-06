from django.db import models



class Book (models.Model):

    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published = models.IntegerField()


    class Meta:
        verbose_name = ("book")
        verbose_name_plural = ("books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})