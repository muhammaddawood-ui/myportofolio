from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Muhammad Dawood Alfathiin",
        "nickname": "Dawood",
        "npm": "2506610456",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An Information Systems undergraduate passionate about technology, leadership, and social interaction. I enjoy connecting with people, building collaborations, and applying tech knowledge to create positive impact."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Dawood",
        "nickname": "Dawood",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)