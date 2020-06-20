from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            print("I love you")  # 표준 출력 메시지(회색)
            self.stdout.write(self.style.SUCCESS("I love you"))  # 표준 성공 메시지(초록색)
            self.stdout.write(self.style.ERROR("I love you"))  # 표준 에러 메시지(적색)
            self.stdout.write(self.style.WARNING("I love you"))  # 표준 에러 메시지(적색)

