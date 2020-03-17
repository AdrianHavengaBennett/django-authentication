from django.conf.urls import url, include
from accounts import views as accounts_views
from accounts import url_reset

urlpatterns = [
    url(r"^logout/$", accounts_views.logout, name="logout"),
    url(r"^login/$", accounts_views.login, name="login"),
    url(r"^register/$", accounts_views.registration, name="registration"),
    url(r"^profile/$", accounts_views.user_profile, name="profile"),
    url(r"^reset-password/", include(url_reset)),
]
