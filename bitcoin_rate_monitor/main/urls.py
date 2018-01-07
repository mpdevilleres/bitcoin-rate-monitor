from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^summary$',
        view=views.SummaryView.as_view(),
        name='summary'
    ),
    url(
        regex=r'^$',
        view=views.ProviderListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<provider>[\w.@+-]+)/$',
        view=views.ProviderDetailView.as_view(),
        name='detail'
    ),
]
