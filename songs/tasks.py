# from django.core.mail import send_mail
# from celery import shared_task
# from user_account.models import User
# from datetime import date, timedelta
# from .models import Song
# from django.core.exceptions import ObjectDoesNotExist
# from datetime import date, timedelta

from django.core.exceptions import ObjectDoesNotExist
from .models import Song
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def process_song(song_id):
    try:
        song = Song.objects.get(id=song_id)
        return song
    except Song.DoesNotExist:
        raise Exception(f"Песня с идентификатором {song_id} не найдена.")

@shared_task
def send_new_song():
    songs = Song.objects.all()
    message = f"Хит дня!"
    for song in songs:
        message += f"\n{song.name}  ${song.text}"

    send_mail(
        subject="Новые песни",
        message=message,
        from_email="admin@admin.com",
        recipient_list=["nursul1997@gmail.com",],
    )



# @shared_task
# def process_song(song_id):
#     try:
#         song = Song.objects.get(id=song_id)
#         return song
#     except ObjectDoesNotExist:
#         raise Exception(f"Песня с идентификатором {song_id} не найдена.")
    
# def send_new_song():
#     day = date.today() - timedelta(days=1)
#     songs = Song.objects
#     message = f"Хит дня!"
#     for song in songs:
#         message += f"\n{song.name}  ${song.text}"


 
#     send_mail(
#         subject="Новая песня Imagine dragons",
#         message=message,
#         from_email="@aidinaashirova",
#         recipient_list=[u.email for u in User.objects.all()]
#     )

# @shared_task
# def process_song(song_id):
#    day = date.today() - timedelta(days=1)
#     # на основе переданного идентификатора песни


# @shared_task
# def send_new_song_notification(song_id):
#     # Здесь можно отправлять уведомления о новой песне
#     # на основе переданного идентификатора песни
#     pass



# @shared_task
# def send_new_song():
#     day = date.today() - timedelta(days=1)
#     songs = Song.objects.filter(created_at__gte=day)
#     message = f"Хит дня!"
#     for song in songs:
#         message += f"\n{song.name}  ${song.text}"

    # send_mail(
    #     subject="Новая песня Imagine dragons",
    #     message=message,
    #     from_email="@aidinaashirova",
    #     recipient_list=[u.email for u in User.objects.all()]
    # )