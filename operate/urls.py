from django.conf.urls import url

from operate import views, tests
from operate import views

urlpatterns =[
    url(r"^login/$", views.login, name="login"),
    url(r"^generateCode/$", views.generate_code, name='generatecode'),
    url(r"^login/register/$", views.register, name = 'register'),
    url(r"^smartisan/$",views.smartisan,name="smartisan"),
    url(r"^code/$", views.code, name="code"),
    url(r"^money/(\d+)/$",views.money,name="money"),
    url(r"^payment/$",views.payment,name="payment"),

]

