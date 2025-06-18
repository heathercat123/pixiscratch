from django.http import HttpResponse
import json


def account_nav(request):
    """
    TODO: Make this dump userprofiles.userprofile like in ScratchR2
    """
    response = HttpResponse(json.dumps({}, indent=3))
    return response
