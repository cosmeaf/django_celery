from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'

    def handle_no_permission(self):
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': 'User not authenticated.'}, status=401)
        return super().handle_no_permission()