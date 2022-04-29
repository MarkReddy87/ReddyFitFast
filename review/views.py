""" Add relevant imports below """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm


def review_list(request):
    """ A view to show all reviews """
    reviews = Review.objects.all()
    context = {
       'reviews': reviews,
    }

    return render(request, 'review/reviews.html', context)


def add_review(request):
    """ review view """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('review'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'review/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def review_detail(request, review_id):
    """ A view to show individual review details """

    review = get_object_or_404(Review, pk=review_id)

    context = {
        'review': review,
    }

    return render(request, 'review/review_detail.html', context)
