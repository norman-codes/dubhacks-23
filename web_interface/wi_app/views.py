from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.contrib import messages

# import recording model
from .models import Recording

# Create your views here.
# RECORDING VIEW: posts the recording to the database.
def recording(request):
    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        recording = Recording.objects.create(voice_recording=audio_file)
        recording.save()
        messages.success(request, "Audio recording successfully added!")
        return JsonResponse(
            {
                "success": True
            }
        )
    context = {"page_title": "Record your response."}
    return render(request, "wi_app/recording.html", context)

# RECORDING DETAIL VIEW: displays all details of the recording.
def recording_detail(request, id):
    recording = get_object_or_404(Recording, id=id)
    context = {
        "page_title": "Audio recording details.",
        "recording": recording
    }
    return render(request, "wi_app/recording_detail.html", context)

# INDEX VIEW: this page will contain the prompt for user-generated recordings.
def index(request):
    recordings = Recording.objects.all()
    context = {
        "page_title": "Voice records",
        "recordings": recordings
    }
    return render(request, "wi_app/index.html", context)