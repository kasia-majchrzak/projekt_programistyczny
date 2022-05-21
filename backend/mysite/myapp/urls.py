from django.urls import path
from .views import WordCloudView
from .views import TextSummaryView
from .views import TextSimilarityView


urlpatterns = [
    path('api/get-text-summary/', TextSummaryView.as_view()),
    path('api/get-word-cloud/', WordCloudView.as_view()),
    path('api/get-text-similarity/', TextSimilarityView.as_view())
]