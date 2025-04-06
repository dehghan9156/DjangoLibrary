from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from accounts.models import Profile
import random
from django.utils import timezone
from library.models import Amanat,Book,Category
from datetime import datetime

User = get_user_model()
category_list = [
    "Novel",
    "History",
    "Science",
    "Religion",
    "Biography",
    "Education"
]

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        for _ in range(6):
            for name in category_list:
                category_obj, created = Category.objects.get_or_create(
                    name=name,
                    defaults={"description": self.fake.paragraph(nb_sentences=5)}
                )
                image = f"https://picsum.photos/seed/book{random.randint(1000, 9999)}/200/300"
                book_obj = Book.objects.create(
                category = category_obj,
                name = self.fake.sentence(nb_words=3),
                image = image,
                created_date = datetime.now,
                )

