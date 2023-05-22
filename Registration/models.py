# python imports
import uuid

# django imports
from django.db import models



class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(BaseModel):
    id = models.AutoField(primary_key=True, unique=True, db_index=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    last_login_at = models.DateTimeField(null=True)


class AuthToken(BaseModel):
    token = models.CharField(max_length=100, primary_key=True, unique=True, db_index=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

