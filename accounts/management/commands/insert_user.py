from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from accounts.models import Profile
import random
from django.utils import timezone

User = get_user_model()


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        for _ in range(6):
            random_number = random.randint(1, 100)
            image_url = f"https://randomuser.me/api/portraits/women/{random_number}.jpg"

            # استفاده از get_or_create برای ایجاد یا بازیابی کاربر
            user_obj, created = User.objects.get_or_create(
                email=self.fake.email(),
                defaults={'password': 'a@/123456'}
            )

            # اگر پروفایل برای این کاربر وجود نداشته باشد، پروفایل جدید بساز
            profile, profile_created = Profile.objects.get_or_create(
                user=user_obj
            )

            if profile_created:  # اگر پروفایل جدید ایجاد شده باشد
                profile.first_name = self.fake.first_name()
                profile.last_name = self.fake.last_name()
                profile.description = self.fake.text()
                profile.image = image_url
                profile.created_date = timezone.now()
                profile.save()  # ذخیره پروفایل جدید
            else:
                # اگر پروفایل قبلاً وجود داشته باشد، می‌توان مقادیر آن را به روز کرد
                profile.first_name = self.fake.first_name()
                profile.last_name = self.fake.last_name()
                profile.description = self.fake.text()
                profile.image = image_url
                profile.created_date = timezone.now()
                profile.save()  # ذخیره تغییرات
