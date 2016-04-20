from django.apps import apps
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = ("One-time migration of a project using `django-model-publisher`"
            " DB fields to ICEKit's 'publishing' equivalents")

    def handle_noargs(self, *args, **options):
        UrlNode = apps.get_model('fluent_pages.UrlNode')
        for node in UrlNode.objects.all():
            node.publishing_linked = node.publisher_linked
            node.publishing_is_draft = node.publisher_is_draft
            node.publishing_modified_at = node.publisher_modified_at
            node.publishing_published_at = node.publisher_published_at
            node.save()