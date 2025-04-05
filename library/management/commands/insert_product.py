from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from accounts.models import Profile
import random
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fake = Faker()
    #
    # def handle(self, *args, **options):
    #     for _ in range(6):
    #
    pass