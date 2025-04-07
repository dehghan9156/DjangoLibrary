from library.models import Amanat

def user_amanat_status(request):
    if request.user.is_authenticated:
        amanat = Amanat.objects.filter(profile__user = request.user,status="borrowed")
    return {"amanat":amanat}