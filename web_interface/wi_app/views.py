from django.shortcuts import render, HttpResponse

# Create your views here.

# INDEX VIEW: this page will contain the prompt for user-generated recordings.
def index(request):
    context = {
        "page_title": "Voice records"
    }
    return render(request, "wi_app/index.html", context)