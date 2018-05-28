from django.shortcuts import render
from django.forms.models import inlineformset_factory

from formtools.wizard.views import NamedUrlSessionWizardView

from .forms import NumberOfTicketsForm, PeopleForm, OtherForm
from .models import Booking, BookingPerson


class BookingWizard(NamedUrlSessionWizardView):
    # form_list = [NumberOfTicketsForm, PeopleForm, OtherForm]

    def get_form_instance(self, step):
        return Booking()

    def get_form(self, step=None, data=None, files=None):
        form = super(BookingWizard, self).get_form(data=data, files=files)
        current_step = self.steps.current

        if current_step == 'step1':
            self.storage.set_step_data('step2', None)

        if current_step == 'step2':
            prev_data = self.storage.get_step_data('step1')
            number = prev_data.get('step1-number', '')
            factory = inlineformset_factory(
                Booking,
                BookingPerson,
                # form=ModelForm,
                # formset=BaseInlineFormSet,
                fields=('name',),
                extra=int(number),
                can_delete=False)
            if data:
                return factory(data)
            else:
                return factory()

        return form

    def done(self, form_list, form_dict, **kwargs):
        # return render(self.request, 'done.html', {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })
        # when using NamedUrlWizardView
        # user = form_dict['user'].save()

        return HttpResponseRedirect('/page-to-redirect-to-when-done/')
