from django.shortcuts import render
from category.models import *
from usingform.models import Defaultform
from django.db.models import Count
import datetime
# Create your views here.
def main_show(request):
    show_all = Category.objects.all()

    #이미지 있는 게시글 가져오기
    image_board = Defaultform.objects.filter(category__board_url_name='infoboard').filter(end_at__gte=datetime.date.today()).annotate(num_item=Count('image')).filter(num_item__gt=0).order_by("-created_at")[:5]
    
    return render(request, "main.html", {'show_all':show_all, 'image_board':image_board,})

def goto_chatbot(request):
    return render(request, "chatbot.html",{})