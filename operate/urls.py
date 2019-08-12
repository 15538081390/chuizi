from django.conf.urls import url

from operate import views, tests

urlpatterns =[

    url(r"^login/$", views.login, name="login"),
]