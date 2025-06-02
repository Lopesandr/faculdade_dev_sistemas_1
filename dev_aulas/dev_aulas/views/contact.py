from django.shortcuts import render
from django.views import View
from dev_aulas.form.contact_form import ContactForm

class ConcactView(View):
    @staticmethod
    def get(request):
        form = ContactForm()
        context = {
            'form': form
        }
        print(context)
        return render(request, 'contact/page_contact.html', context)
    
    @staticmethod
    def post(request):
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            sender = form.cleaned_data.get("sender")
            cc_myself = form.cleaned_data.get("cc_myself")

            print(f"Subject: {subject}")
            recipients = ['dessarosalopes15@gmail.com']

            if cc_myself:
                recipients.append(sender)
            
            context = {
                    'recipients' : recipients,
                    'form': form,
            }

            return render(request, 'contact/thanks.html', context)
        context = {'form': form}
        return render(request, 'contact/page_contact.html', context)