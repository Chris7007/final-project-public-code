from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)



'''
***************************************************************************************#*******
***************          ABOUT - Class for handling the about page            *****************
***********************************************************************************************
'''
class AboutView(TemplateView, ContextMixin):
    template_name= "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get avatar for navbar
        if self.request.user.is_authenticated is True:
            try:
                context['avatar'] = UserProfile.objects.get(user__id = self.request.user.id).avatar
            except:
                logger.warning("No  user profile fur this user") 
        return context
    


'''
***********************************************************************************************
********                REPORT - Function for handling the report page                 ********
***********************************************************************************************
'''
@login_required(login_url='/login/')
@user_passes_test(isVerifiedCheck, login_url='/email_verification/')
def report(request, pk):
    
    # get current user and demo title and avatar
    user = request.user
    try:
        demo = Demos.objects.get(pk = pk)
    except:
        messages.error(request, 'The requested demo to report does not exist.', extra_tags='alert alert-danger')
        return HttpResponseRedirect(reverse("index")) 
    avatar = UserProfile.objects.get(user__id=user.id).avatar

    # if a form is posted, validate against model and save or display error if invalid
    if request.method == 'POST' and "report_form" in request.POST:
        report_form = ReportForm(request.POST, request.FILES,)
        if report_form.is_valid():
            # Save form if valid, don't commit yet because need to add userid and demoid
            report = report_form.save(commit=False)
            report.user_id_report = user
            report.demo_id_report = demo
            report.user_pk = user.id
            report.demo_pk = demo.id
            report.save() # saves report to DB
            messages.success(request, 
                            'Thank you, you have successfully submitted your report',
                            extra_tags='alert alert-success')
            return HttpResponseRedirect(reverse("index"))
        else:
            logger.warning("report form error")
            messages.error(request, 
                        'Please correct the identified error(s).', 
                            extra_tags='alert alert-danger')  
    # if no form posted return blank form to template page
    else:
        report_form = ReportForm
    
    # render form to template page (with populated fields and errors if applicable)
    return render(request, 'report.html', {
        'report_form': report_form, 'demoid' : pk, 'demo_title' : demo.title, 'avatar' : avatar
    })


