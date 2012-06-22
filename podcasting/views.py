from django.http import HttpResponse
from django.utils import simplejson
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404

from podcasting.models import Episode, Show, MainCategory, SubCategory


class ShowListView(ListView):
    queryset = Show.objects.onsite()


class ShowDetailView(DetailView):
    queryset = Show.objects.onsite()


class EpisodeListView(ListView):
    def get_queryset(self):
        return Episode.objects.published().filter(show__slug=self.kwargs["show_slug"])


class EpisodeDetailView(DetailView):
    def get_queryset(self):
        return Episode.objects.published().filter(show__slug=self.kwargs["show_slug"])


def sub_categories_per_main_category(request, main_category_id, show_id):
    """Return the sub categories per main category as JSON. Tag if sub_category
    is already chosen by show. Used in Admin as a filter for selecting the sub
    categories."""

    main_category = get_object_or_404(MainCategory, pk=main_category_id)
    sub_categories = SubCategory.objects.filter(
        main_category=main_category)

    if int(show_id) > 0:
        show = get_object_or_404(Show, pk=show_id)
        sub_categories_per_show = show.sub_categories.all()
        sub_categories_data = [(s.pk, s.name, s in sub_categories_per_show) \
            for s in sub_categories]
    else:
        sub_categories_data = [(s.pk, s.name, False) for s in sub_categories]

    # Note, simplejson.dumps does not know the type
    # django.db.models.query.ValuesListQuerySet
    return HttpResponse(simplejson.dumps(sub_categories_data),
                        mimetype='application/javascript')
