from django.db import models
from django.contrib.auth.models import User  # Add this import

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


class sharetrigger(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="suggester")
    suggest_stock = models.CharField(max_length=200)
    suggest_date = models.IntegerField(choices=TRIGGER_DATE, default=0)
    suggest_summary = models.TextField()
    more_info = models.CharField(max_length=200)
    suggest_pr = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
