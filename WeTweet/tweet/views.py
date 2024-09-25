from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_backends


def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "tweet_list.html", {"tweets": tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = (
                request.user
            )  # TweetForm dosen't have user but django gets user with every request
            tweet.save()
            return redirect("tweet_list")

    else:
        form = TweetForm
    return render(request, "tweet_form.html", {"form": form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save(commit=False)
            tweet.user = (
                request.user
            )  # TweetForm dosen't have user but django gets user with every request
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)
    if tweet.photo:
        truncated_photo_name = (
            tweet.photo.name[:10] + "..."
            if len(tweet.photo.name) > 10
            else tweet.photo.name
        )
    return render(request, "tweet_form.html", {"form": form})


def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")

    return render(request, "tweet_confirm_delete.html", {"tweet": tweet})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            backend = get_backends()[0]
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            login(request, user, backend=user.backend)

            return redirect("tweet_list")
    else:
        form = UserRegistrationForm()

    return render(request, "registration/register.html", {"form": form})


def search(request):
    query = request.GET.get("query", "")
    tweets = []

    if query:

        users = User.objects.filter(username__icontains=query)
        if users.exists():

            tweets = Tweet.objects.filter(user__in=users)
        else:

            tweets = Tweet.objects.filter(text__icontains=query)

    params = {"tweets": tweets, "query": query}
    return render(request, "search.html", params)


def logged_out(request):
    return render(request, "registration/logged_out.html")
