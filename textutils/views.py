from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    dict = {"name": "hardik", "place": "Kalka"}
    return render(request, 'index.html', dict)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def analyze(request):  # Laying pipes
    # get the text and analyze the text

    djtext = request.POST.get('text',
                             'default')  # 'text is the passed value and 'default is the defualt value if nothing is passed
    removepunc = request.POST.get('removepunc',
                                 'off')  # if removepunc is ticked then it will print on otherwise it will print off
    fullcaps = request.POST.get('fullcaps',
                               'off')  # if removepunc is ticked then it will print on otherwise it will print off
    newlineremover = request.POST.get('newlineremover',
                                     'off')  # if removepunc is ticked then it will print on otherwise it will print off
    extraspaceremover = request.POST.get('extraspaceremover',
                                        'off')  # if removepunc is ticked then it will print on otherwise it will print off
    charcounter = request.POST.get('extraspaceremover',
                                  'off')  # if removepunc is ticked then it will print on otherwise it will print off

    # checkboxex values check
    if removepunc == "on":
            punctuations = '''!@#$%^&*()~_[]{};:'"\/?.>,<'''
            analyzed = ""
            char = ""
            for index, char in enumerate(djtext):
                if djtext[index] not in punctuations:
                    analyzed += djtext[index]
            params = {"purpose": "", "analyzed_text": analyzed}
            djtext=analyzed
            # return render(request, 'analyze.html', params)

    if fullcaps == "on":
            analyzed = ""
            char = ""
            for char in str(djtext):
                analyzed = analyzed + char.upper()
            params = {"purpose": "", "analyzed_text": analyzed}
            djtext = analyzed
            # return render(request, 'analyze.html', params)

    if newlineremover == "on":
            analyzed = ""
            char = ""
            for char in djtext:
                if char != '\n' and char!="\r":
                    analyzed = analyzed + char
            params = {"purpose": "", "analyzed_text": analyzed}
            djtext = analyzed
            # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
            analyzed = ""
            char = ""
            for index, char in enumerate(djtext):
                if index == len(djtext):
                    break
                else:
                    if djtext[index] == " " and djtext[index + 1] == " ":
                        pass
                    else:
                        analyzed = analyzed + djtext[index]
            params = {"purpose": "", "analyzed_text": analyzed}
            djtext = analyzed

    if ( removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        HttpResponse("Error")

    return render(request, 'analyze.html', params)



