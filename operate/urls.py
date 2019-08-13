from django.conf.urls import url

from operate import views, tests
from operate import views

urlpatterns =[
    url(r"^login/$", views.login, name="login"),
    url(r"^smartisan/$",views.smartisan,name="smartisan"),
    url(r"^money/(\d+)/$",views.money,name="money"),
    url(r"^payment/$",views.payment,name="payment"),
]