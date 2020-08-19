
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def analyze(request):
    params=""
    #text
    text1= request.POST.get('text','default')
    #checkbox
    cb= request.POST.get('removepunc','off')
    fulcap= request.POST.get('fullcap','off')
    liner= request.POST.get('new','off')
    space= request.POST.get('space','off')
    count= request.POST.get('count','off')

    if cb=="on":
        punc='''~!#$%^@&*()-_=+`'";:[]{}\|<>?,./'''
        analyzed=""
        for char in text1:
            if char not in punc:
                analyzed=analyzed+char

        params={'purpose':'removed punctuations','final_text':analyzed}
        text1=analyzed

    if fulcap=="on":
        analyzed= text1.upper()
        params = {'purpose': 'changed to uppercase', 'final_text': analyzed}
        text1 = analyzed

    if (liner == "on"):
        analyzed = ""
        for char in text1:
            if(char!="\n" and char!="\r"):
                analyzed=analyzed+" "+char
        params = {'purpose': 'Removed new lines', 'final_text': analyzed}
        text1 = analyzed

    if (space == "on"):
        analyzed = ""
        for index,char in enumerate(text1):
            if not(text1[index]==" " and text1[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Removed etra spaces', 'final_text': analyzed}
        text1 = analyzed

    if (count == "on"):
        no=len(text1)-text1.count(' ')
        analyzed1 = '\nNo. of char ='+str(no)
        analyzed=text1+analyzed1
        params = {'purpose': 'count character', 'final_text': analyzed}




    if(cb!="on" and fulcap!="on" and liner != "on" and space != "on" and count != "on"  ):
        return HttpResponse("Please select any operation!")

    return render(request, 'analyze.html', params)
