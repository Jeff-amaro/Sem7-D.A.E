"""Answers an authorized AI assistant gave live, from scratch.

The assistant was given ONLY the content of `blog/models.py` (no seed data, no
questions module, no expected answers) and asked for the eight queries of the
duel. These are its answers, kept exactly as it wrote them, so they can be run
through the same checker as any other source:

    python manage.py duel --source ai_live

Compare them with the pre-baked answers in `blog/duel/ai_answers.py`
(python manage.py duel --source ai) and with the team's own answers.
"""
from datetime import date

from django.db.models import Count

from blog.models import Author, Comment, Post


def q1():
    return Post.objects.filter(published=True)


def q2():
    return Post.objects.filter(category__isnull=True)


def q3():
    return Post.objects.filter(published_at__range=(date(2026, 3, 1), date(2026, 5, 31)))


def q4():
    return Post.objects.annotate(n_comments=Count("comments")).filter(n_comments__gt=2)


def q5():
    return (
        Post.objects.filter(published=True)
        .annotate(
            n_comments=Count("comments", distinct=True),
            n_tags=Count("tags", distinct=True),
        )
        .order_by("-n_comments", "id")[:3]
    )


def q6():
    return Post.objects.filter(author__profile__country="Perú")


def q7():
    return Comment.objects.filter(post__category__name="Tecnología")


def q8():
    return Author.objects.exclude(posts__published=True)
