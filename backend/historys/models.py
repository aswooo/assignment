from django.db import models
from users.models import User


class history(models.Model):
    history_id = models.BigAutoField(primary_key=True, null=False)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_spend = models.BooleanField(null=False)    # 지출인지 수입인지
    cost = models.BigIntegerField(null=False)   # 변동된 금액
    balance = models.BigIntegerField(null=False)    # 잔고
    memo = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'history'
