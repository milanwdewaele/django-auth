from functools import wraps

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def group_required(*group_names):
    def decorator(view_function):
        @wraps(view_function)
        @login_required
        def wrapped_view(request, *args, **kwargs):
            has_access = request.user.groups.filter(
                name__in=group_names
            ).exists()

            if not has_access:
                return HttpResponseForbidden(
                    "Je hebt geen toegang tot deze pagina."
                )

            return view_function(request, *args, **kwargs)

        return wrapped_view

    return decorator