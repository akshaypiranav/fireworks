from django.shortcuts import render
import smtplib
from django.http import JsonResponse

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .models import Crackers
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    if request.method == 'POST':
        mail = request.POST['email']
        mobile = request.POST['mobile']
        message_body = request.POST['message']
        print(mail, mobile, message_body)

        sender_email = "akshaypiranavb@gmail.com"
        receiver_email = "akshaypiranavb@gmail.com"
        subject = "Customer contact"
        body = "Customer Message : " + message_body +'\n'+'Customer mobile number : '+mobile+'\n'+'Customer Email : '+mail 

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        smtp_server = "smtp.gmail.com" 
        smtp_port = 587  
        smtp_username = "akshaypiranavb@gmail.com"  
        smtp_password = "ddld flec vggd ovve"

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
    data=Crackers.objects.all()

    return render(request, "index.htm",{'data':data})

@csrf_exempt  # Note: CSRF exemption is applied for simplicity. For production, implement CSRF protection.
def mail(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        print(data)
        rows = data.get('rows', [])
        detail=data.get('detail',{})

        cusDetail = f"Customer Name : {detail.get('name', '')}\nCustomer Email : {detail.get('email', '')}\nCustomer Contact : {detail.get('contact', '')}"
        print(cusDetail)
        # Process the received data
        value=''
        total=0
        count=1
        for row in rows:
            value += f"{count} : {row['name']}, Quantity: {row['quantity']}, Amount: {row['amount']}\n"
            count+=1
            total+=row['amount']
        print(value)
        print(total)
        sender_email = "akshaypiranavb@gmail.com"
        receiver_email = "akshaypiranavb@gmail.com"
        subject = "Customer Order"
        body = "Customer Detail"+'\n'+str(cusDetail)+'\n'+'Ordered Products'+"\n"+value+'\n'+"Total Amount : "+str(total)

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        smtp_server = "smtp.gmail.com" 
        smtp_port = 587  
        smtp_username = "akshaypiranavb@gmail.com"  
        smtp_password = "ddld flec vggd ovve"

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})

