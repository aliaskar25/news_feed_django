from django.core.mail import send_mail
from news_feed.settings import EMAIL_HOST_USER
from threading import Thread


def async_email(to, title, link):
    send_mail(title,
        link, EMAIL_HOST_USER, 
        to,
        fail_silently=False
    )


def notification(to: list, title: str, link: str):
    thr = Thread(target=async_email, args=[to, title, link])
    thr.start()
    return thr
