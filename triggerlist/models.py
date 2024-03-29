from django.db import models
from django.contrib.auth.models import User

TRIGGER_DATE = (
    (0, "Pick a year and quarter"),
    (1, "2024-Q1"),
    (2, "2024-Q2"),
    (3, "2024-Q3"),
    (4, "2024-Q4"),
    (5, "2024-H1"),
    (6, "2024-H2"),
    (7, "2025-Q1"),
    (8, "2025-Q2"),
    (9, "2025-Q3"),
    (10, "2025-Q4"),
    (11, "2025-H1"),
    (12, "2025-H2"),
)

# Create your models here.


# The model to add a trigger
class Trigger(models.Model):
    stock_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    trigger_date = models.IntegerField(choices=TRIGGER_DATE, default=0)
    trigger_headline = models.CharField(max_length=200)
    summary = models.TextField()
    website_link = models.CharField(max_length=200,)
    pr_link = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.stock_name


# The model for comments
class Comment(models.Model):
    trigger = models.ForeignKey(
        Trigger, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
