from django.urls import path

from web.views import \
    ArticlesListView, ArticleCreateView, SourcesListView, SourceDetailsView, SourceCreateView

urlpatterns = [
    path('', ArticlesListView.as_view(), name='index'),
    path('articles/create', ArticleCreateView.as_view(), name='create article'),
    path('soursec/', SourcesListView.as_view(), name='list source'),
    path('soursec/<int:pk>', SourceDetailsView.as_view(), name='details source'),
    path('sources/create', SourceCreateView.as_view(), name='create source'),
]
