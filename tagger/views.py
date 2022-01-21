from tagger.core.iamport import IMP
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def test(request):
    res = IMP.instance().get_payment_details(
        ["imp_506226861508", "imp_573119157048", "imp_950686323114"]
    )
    return JsonResponse({"result": res})
