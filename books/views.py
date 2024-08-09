from django.views.generic import ListView
from books.models import Publisher


class PublisherListView(ListView):
    model = Publisher
