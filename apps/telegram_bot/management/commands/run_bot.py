from django.core.management.base import BaseCommand
from apps.telegram_bot.bot import main as run_bot

class Command(BaseCommand):
    help = 'Telegram botni ishga tushiradi'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Telegram bot ishga tushirilmoqda...'))
        run_bot()