from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Auction, Bid, Comment, AuctionCategories
from django import forms

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]


class NewListingForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    current_price = forms.DecimalField(label="Current Price")
    categories = forms.CharField(
        label='Choose category',
        widget=forms.Select(choices=
                            [category for category in AuctionCategories.objects.all().values_list(
                                    'category_name', 'category_name')]))
    image_url = forms.URLField(label="Image URL")


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Auction.objects.all(),
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='/login')
def create_new_listing(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewListingForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the auction from the 'cleaned' version of form data
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            current_price = form.cleaned_data["current_price"]
            image_url = form.cleaned_data["image_url"]
            category = form.cleaned_data["categories"]

            # Add the new auction to the database
            new_auction = Auction(title=title, description=description, current_price=current_price,
                                  image_url=image_url, user=request.user)
            new_auction.save()

            # Redirect user to list of auctions
            return HttpResponseRedirect(reverse("index"))
        else:
            # If the form is invalid, show message to user that form is invalid
            return HttpResponse("Invalid form")

    return render(request, "auctions/create_new_listing.html", {
                  "form": NewListingForm(),
                  })

def show_categories(request):
    return render(request, "auctions/categories.html", {
        "categories": AuctionCategories.objects.all()
    })


def show_listings(request):
    return render(request, "auctions/index.html", {
        "listings": Auction.objects.all(),
    })