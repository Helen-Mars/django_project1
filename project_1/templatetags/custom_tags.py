from django import template
from ..models import UserProfile

register = template.Library()


@register.inclusion_tag('user_profile_list.html')
def show_user_profiles():
    user_profiles = UserProfile.objects.all()
    return {'user_profiles': user_profiles}
