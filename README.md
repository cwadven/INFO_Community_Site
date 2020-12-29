<h1 align="center">STUDENTCARE 커뮤니티 사이트 프로젝트</h1>

원광대학교 학생들이 이용할 수 있는 커뮤니티 정보 사이트

<h3 align="center">홈페이지</h3>
<p align="center">
<img alt="studentcare" src="https://github.com/cwadven/marketing/blob/master/assets/home_page.PNG"/>
</p>

~~~
url : http://localhost:8000/
기능 :
- 게시판 목록
- infoboard의 게시판에 써져있는 글 중 사진이 있으며 아직 이벤트 기간이 종료되지 않은 것을 띄운다
~~~

<h3 align="center">게시판 목록</h3>
<p align="center">
<img alt="studentcare" src="https://github.com/cwadven/marketing/blob/master/assets/category.PNG"/>
</p>

~~~
url : http://localhost:8000/category/
기능 :
- 일반 사용자에게 게시판 목록을 보여준다.
- 관리자는 게시판을 추가, 수정, 삭제를 할 수 있다.
~~~

<h3 align="center">글 목록</h3>
<p align="center">
<img alt="studentcare" src="https://github.com/cwadven/marketing/blob/master/assets/board_list.PNG"/>
</p>

~~~
url : http://localhost:8000/게시판이름/
기능 :
- 게시판에 있는 게시글들을 보여준다.
- 관리자가 설정한 중요한 게시글을 위에 보여준다.
- 인기글을 5개 이하로 불러온다. (기준 : 좋아요 수)
- 글을 쓸 수 있다. (다중 이미지, 다중 파일 가능)
- 글을 검색할 수 있다.
~~~

<h3 align="center">infoboard 글 목록(추가기능)</h3>
<p align="center">
<img alt="studentcare" src="https://github.com/cwadven/marketing/blob/master/assets/date.PNG"/>
</p>

~~~
url : http://localhost:8000/infoboard/
기능 :
- infoboard의 이름을 가진 게시판은 이벤트 날짜 즉, 일시를 추가할 수 있는 form이 주어진다.
- 해당 날짜를 통해 '종료'라는 시각적 표현을 해준다.
~~~

<h3 align="center">글 작성</h3>
<p align="center">
<img alt="studentcare" src="https://github.com/cwadven/marketing/blob/master/assets/post.PNG"/>
</p>

~~~
url : http://localhost:8000/게시판이름/
기능 :
- 제목, 내용, 이미지, 파일 내용을 적고 작성 (infoboard:시작날짜, 종료날짜로 이벤트 기간 설정 가능)
- 다중 이미지, 다중 파일 업로드 가능 및 업로드 전, 삭제 기능 가능
~~~

<h3 align="center">글 내용</h3>
<p align="center">
<img alt="studentcare" src="https://github.com/cwadven/marketing/blob/master/assets/board.PNG"/>
</p>

~~~
url : http://localhost:8000/infoboard/1
기능 :
- 게시글 내용 조회
- 댓글 작성 가능
- 업로드 이미지 키워서 보고 다운로드 가능
- 업로드 파일 다운로드 가능
- 좋아요, 즐겨찾기 추가 가능
- 수정, 삭제 가능
- Cookie를 이용한 조회수 증가
- 누군가 댓글을 작성하면 상단의 알림 버튼 활성화 및 비활성화
~~~

<h3 align="center">회원가입</h3>
<p align="center">
<img alt="studentcare" src="https://github.com/cwadven/marketing/blob/master/assets/signup.PNG"/>
</p>

~~~
url : http://localhost:8000/account/signup/
기능 :
- 회원가입
- 아이디, 닉네임, 이메일 중복 확인
- 프로필 사진 업로드 가능
~~~


<h3 align="center">마이페이지</h3>
<p align="center">
<img alt="studentcare" src="https://github.com/cwadven/marketing/blob/master/assets/my_page.PNG"/>
</p>

~~~
url : http://localhost:8000/account/profile/
기능 :
- 회원 정보 조회
- 누군가 댓글을 작성하면 상단의 알림 버튼 비활성화 해제
- 좋아요한 게시판 출력
- 즐겨찾기한 게시판 출력
- 알림 받은 내용 조회
- 회원 탈퇴
- 관리자 : 중요게시판 설정하여 게시판 글 목록에서 맨위에 있는 중요게시판 보여주는 게시글 설정
- 회원 정보 수정
- 비밀번호 변경
~~~

#### PlayChat Ai API를 이용하여 챗봇 서비스 또한 추가 했지만 PlayChat 사이트가 문을 닫아 문제가 생겨 이용할 수 없습니다.

## 서비스 주소
**주소 :**<br>
http://readly.shop/


# 팀원 소개

---

## 기획자

**👤 연진욱**

- Github : ???
- Service : PlayChat Ai API
- 역할
    - 간단 스토리보드 구성
    - 디자인 기획
    - PlayChat AI API 추출
- 개발기간 : <br>
    - 2020년 6월 3일 ~ 2020년 7월 10일

## 디지아너

**👤 신승미**

- Github : ???
- 역할 : 
    - 디자인 UX, UI 생성
- 기술스택 : PhotoShop
- 개발기간 : <br>
    - 2020년 6월 3일 ~ 2020년 7월 10일

## 개발자

**👤 이창우 [메인 개발]**

- Github : https://github.com/cwadven
- Backend : Django
- Service : SQLite, Apache<br>
(아파치는 제 컴퓨터로...)
- 역할 :
    - Django로 WAS 구현
    - Apache로 웹서버 구현
    - PlayChat 연동
    - DB 테이블 구축
    - 스토리보드 구체화
    - 코드 구현
- Server : Apache
- 기술스택 : Django, JQuery
- 개발기간 : <br>
    - 2020년 6월 3일 ~ 2020년 7월 10일
    - 2020년 7월 10일 ~ 2020년 10월 ??일(유지보수)

**👤 고가영**

- Github : https://github.com/lunevilia
- Backend : Django
- 역할 :
    - Django 보조
- 기술스택 : Django
- 개발기간 : <br>
    - 2020년 6월 3일 ~ 2020년 7월 10일

## 환경 구축

~~~
1. python -m venv myvenv (가상환경 생성)
2. python source myvenv/Script/activates (가상환경 실행)
3. pip install -r requirements.txt (의존성 모듈 설치)
4. python manage.py collectstatic (static 파일 생성)
8. python manage.py migrate (테이블 생성)
9. python manage.py createsuper (관리자 id 생성)
10. python manage.py runserver
11. 로그인 후, 카테고리 'infoboard' url 주소 이름으로 게시판 생성
~~~