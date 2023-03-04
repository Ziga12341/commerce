# add additional models auction listings, bids, comments, and auction categories

from django.contrib.auth.models import AbstractUser
from django.db import models

# user should have information about auctions they have created
# user can add an auction to their “Watchlist.”


class User(AbstractUser):
    pass


class AuctionCategories(models.Model):
    category_name = models.CharField(max_length=64)


class Auction(models.Model):
    """
    A model for an auction listing. Each auction listing has a title, description, current bid, image URL, and category.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(AuctionCategories, blank=True, related_name="auctions")
    closed_at = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)


class Bid(models.Model):
    # for each auction, there should be a list of bids
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")


class Comment(models.Model):
    # se nanaša na auction
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="watchlist")
    added_to_watchlist = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)