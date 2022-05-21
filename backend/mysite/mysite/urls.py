from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('', include('myapp.urls')),
    path('nlp-app-api/', get_schema_view(
        title="NLP APP"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui')
]
