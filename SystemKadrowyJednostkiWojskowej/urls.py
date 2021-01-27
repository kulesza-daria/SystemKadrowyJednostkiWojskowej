from django.urls import include, path
from django.contrib import admin
from polls.views import *
urlpatterns = [
    path('SystemKadrowyJednostkiWojskowej/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('zolnierze-list/', ZolnierzList.as_view()),
    path('zolnierze-create/', ZolnierzListCreate.as_view()),
    path('kontrakty-create/', KontraktyListCreate.as_view()),
]
