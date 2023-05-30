from django.core.mail import send_mail
# from celery import shared_task
from decouple import config
# @shared_task
# def send_activation_code(email, activation_code):
#     activation_url = f'http://127.0.0.1:8000/v1/api/account/activate/{activation_code}'
#     message = f"""
#     Thank you for signing {activation_url}!
#     """
#     send_mail(
#         'Activate your account',
#         message,
#         'test@test.com',
#         [email, ],
#         fail_silently=False
#     )

def send_activation_code(email: str,activation_code: str):
    # message = ''
    # html = f'''
    # <h1>Для активации аккаунта, пожалуйста, нажмите на кнопку:</h1>
    # <a href='http://127.0.0.1:8000/account/activate/{activation_code}'>
    # <button>Activate</button>
    # </a>
    # '''
    activation_url = f'{config("LINK")}/account/activate/{activation_code}'
    message = f'For activate your account, following this link {activation_url}'
    send_mail("Activate account", message, "spotify@spotify.com", [email,'nil.porvani@gmail.com', ])


def reset_password(email, new_password):
    send_mail(
            subject='Сброс пароля',
            message=f'Ваш новый пароль: {new_password}',
            from_email=None,
            recipient_list=[email],
        )