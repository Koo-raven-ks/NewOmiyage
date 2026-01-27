from django.shortcuts import render, get_object_or_404
from .models import Omiyage

# Create your views here.


def index(request):
    return render(request, "index.html")


def overview(request):
    return render(request, "overview.html")


def list_view(request):
    omiyages = Omiyage.objects.all()
    return render(request, "list.html", {"omiyages": omiyages})


def detail(request, pk):
    omiyage = get_object_or_404(Omiyage, pk=pk)
    return render(request, "detail.html", {"omiyage": omiyage})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # ここでメール送信や保存処理（今回はprint）
        print(f"お問い合わせ: {name} ({email}) - {message}")
        return render(request, "contact.html", {"submitted": True})
    return render(request, "contact.html")
