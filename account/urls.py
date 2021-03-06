from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account' 

urlpatterns = [
    #회원가입
    path('signup/', views.signup, name='signup'),

    #로그인
    path('login/', views.login, name='login'),

    #로그아웃
    path('logout/', auth_views.LogoutView.as_view(), kwargs={'next_page': '/'}, name='logout'),

    #비밀번호 찾기
    path('find_password/', views.find_password, name='find_password'),

    #비밀번호 변경
    path('mod_password/', views.mod_password, name='mod_password'),

    #아이디삭제
    path('del_user/', views.del_user, name='del_user'),

    #회원정보 수정 requried login 추가
    path('profile/', views.profile, name='profile'),

    #회원페이지 => 내가쓴글, 쪽지보기, 즐겨찾기, 좋아요 requried login 추가
    #좋아요
    path('like_board/', views.like_board, name='like_board'),
    #즐겨찾기
    path('favorite_board/', views.favorite_board, name='favorite_board'),
    #알람차단
    path('donotalert_board/', views.donotalert_board, name='donotalert_board'),
    #알림확인
    path('alert_board/', views.alert_board, name='alert_board'),
    #알림삭제
    path('del_alert_board/<alert_id>/', views.del_alert_board, name='del_alert_board'),
    #중요게시판 생성(운영자)
    path('important_board/', views.important_board, name='important_board'),
    #중요게시판 삭제(운영자)
    path('del_important_board/<important_id>/', views.del_important_board, name='del_important_board'),
    #중요게시판 수정(운영자)
    path('mod_important_board/<important_id>/', views.mod_important_board, name='mod_important_board'),
    

    #회원탈퇴
    #비밀번호 수정
    path('ajax/<value>/<region>/', views.ajax, name='ajax'),

    #알람 글 보이기
    path('notice_ajax/', views.notice_ajax, name='notice_ajax'),
]
