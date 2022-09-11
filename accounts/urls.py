from django.urls import path

from .views import (
    LogInView, ResendActivationCodeView, RemindUsernameView, SignUpView, ActivateView, LogOutView,
    ChangeEmailView, ChangeEmailActivateView, ChangeProfileView, ChangePasswordView,
    RestorePasswordView, RestorePasswordDoneView, RestorePasswordConfirmView, FaZhaView_1, FaZhaView_2, FaZhaView_3,
    FaZhaView_4
)

app_name = 'accounts'

urlpatterns = [
    path('fa-zha/fa-zha-1', FaZhaView_1, name='fa-zha-1'),
    path('fa-zha/fa-zha-2', FaZhaView_2, name='fa-zha-2'),
    path('fa-zha/fa-zha-3', FaZhaView_3, name='fa-zha-3'),
    path('fa-zha/fa-zha-4', FaZhaView_4, name='fa-zha-4'),

    # 填写文件路径
    path('log-in/', LogInView.as_view(), name='log_in'),  # 主路由 登录到8000/account/log-in
    path('log-out/', LogOutView.as_view(), name='log_out'),  # 8000/accounts/log-out

    path('resend/activation-code/', ResendActivationCodeView.as_view(), name='resend_activation_code'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'),  # 8000/account/sign-up

    path('activate/<code>/', ActivateView.as_view(), name='activate'),

    path('restore/password/', RestorePasswordView.as_view(), name='restore_password'),
    path('restore/password/done/', RestorePasswordDoneView.as_view(), name='restore_password_done'),
    path('restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(), name='restore_password_confirm'),

    path('remind/username/', RemindUsernameView.as_view(), name='remind_username'),

    path('change/profile/', ChangeProfileView.as_view(), name='change_profile'),
    path('change/password/', ChangePasswordView.as_view(), name='change_password'),
    path('change/email/', ChangeEmailView.as_view(), name='change_email'),
    path('change/email/<code>/', ChangeEmailActivateView.as_view(), name='change_email_activation'),
]

# app_name = 'data'
#
# urlpatterns = [
#     path('fa-zha/fazha_1', FaZhaView, name='fa-zha'),
# ]
