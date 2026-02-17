import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Configuaracion de email

sender_email = "camilorodriguezlondono@gmail.com"
reciver_email = "carodriguez@xm.com.co"
password = "ogsg ydhg cmrn pxqd"

# creamos el contenido del correo

subject = "Reporte de Outlier"
body = "Eventualmente en este lugar se encontrara algun reporte de outlier"

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = reciver_email
message['Subject'] = subject

message.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com",587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)
print("Funcoino correctamente")