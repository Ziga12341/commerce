from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new/", views.create_new_listing, name="new"),
    path("categories/", views.show_categories, name="categories"),
    path("listing/<int:listing_id>", views.show_listing, name="listing"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("categories/<str:category_name>", views.show_category, name="category"),
    path("categories", views.show_categories, name="categories"),
]