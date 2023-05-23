from django.core.mail import send_mail
# from celery import shared_task

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
    message = ''
    html = f'''
    <h1>Для активации аккаунта, пожалуйста, нажмите на кнопку:</h1>
    <a href='http://127.0.0.1:8000/api/v1/account/activate/{activation_code}'>
    <button>Activate</button>
    </a>
    '''
    send_mail(
        subject='Активация аккаунта',
        message = message,
        from_email= 'ashirova158@gmail.com',
        recipient_list=[email], #recipient_list - куда или кому отпарвивть. на данную почту отправляем активационный код
        html_message=html
    )