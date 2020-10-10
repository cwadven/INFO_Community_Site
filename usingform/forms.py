from django import forms
from .models import *

class FormTest(forms.ModelForm):
    class Meta:
        model = Defaultform
        fields = ('title', 'body', 'start_at', 'end_at')
        labels = { 'title': '제목', 'body':'내용', 'start_at':'시작날짜', 'end_at':'종료날짜'}
        #help_texts = { 'title': '필수 사항 입니다!', 'body':'내용을 입력해주세요!'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control',}),
            'start_at': forms.DateInput(format='%Y/%m/%d', attrs={'type':'date', 'class':'form-control'}),
            'end_at': forms.DateInput(format='%Y/%m/%d',attrs={'type':'date', 'class':'form-control'})
        }

class ImageTest(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )
        labels = { 'image': '이미지',}
        #help_texts = { 'title': '필수 사항 입니다!', 'body':'내용을 입력해주세요!'}
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'multiple': True,
            }),
            
        }

class FilesTest(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('files', )
        labels = { 'files': '첨부파일',}
        widgets = {
            'files': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class CommentTest(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
        labels = { 'body': '댓글',}
        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control', 'rows':3, 'id':False,}),
        }

class ImportantTest(forms.ModelForm):
    class Meta:
        model = Important_board
        fields = '__all__'
        labels = {'post':'게시판선택', 'important':'중요도'}
        widgets = {
            'important': forms.TextInput(attrs={'class': 'form-control',}),
        }