from django.contrib.sessions.models import Session

class CheckSessionMiddleware(object):
    def process_request(self, request):
        try:
            sessid = request.COOKIES.get('sessionid')
            session = Session.objects.get(session_key=sessid)
            request.user_id = session.get_decoded().get('user')
        except Session.DoesNotExist:
            request.user_id = None

