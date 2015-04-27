from django.core.management.base import BaseCommand

from accounts.models import User
from apps.tangthuvien.models import Topic
from apps.utils import vbb_new_reply


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('args', metavar='thread_id', nargs='+')

    def handle(self, thread_id, *args, **options):
        topic, created = Topic.objects.get_or_create(topic_id=thread_id)
        url = "http://www.tangthuvien.vn/forum/showthread.php?t=%s" % topic.topic_id
        new_reply = vbb_new_reply(url)
        new_reply = {x: int(new_reply[x][0]) for x in new_reply}

        if new_reply['page'] > topic.last_page_number or new_reply['p'] > topic.last_post_id:
            topic.last_post_id = new_reply['p']
            topic.last_page_number = new_reply['page']
            topic.save()

            user_ids = topic.topicuser_set.all().values_list('user')
            users = User.objects.filter(id__in=user_ids)
