from django.db import models
from utils.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return self.title


class ScoreBoard(BaseModel):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="scoreboard_subcategory")

    title = models.CharField(max_length=255)

    is_tasix = models.BooleanField(default=False)

    visitors = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title
