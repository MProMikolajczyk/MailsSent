import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from config_user import read_user_prop

gmail_user = read_user_prop('gmail_user')
gmail_password = read_user_prop('gmail_password')

def sent_single_mail(sent_to, subject, text, url_image = False ):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = gmail_user
    msgRoot['To'] = sent_to

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    body = """
    <div style="text-align: center; padding: 2rem">
        {text}
    </div>
    <div style="display:flex">
        <img src="cid:image1" style="margin: auto;">
    </div>
    """.format(text = text)
    
    # Jeżeli zdjęcie jest dodane
    if url_image:
        msgText = MIMEText(body, 'html')
        msgAlternative.attach(msgText)
        fp = open(url_image, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

    # Brak zdjęcia
    else:
        msgText = MIMEText(text)
        msgAlternative.attach(msgText)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, sent_to, msgRoot.as_string())
        server.close()

    except:
        raise


def sent_multi_mails( subject , text, url_image, addres_mails ):
    for i in range(len(addres_mails)):
        try:
            sent_single_mail(addres_mails[i], subject , text, url_image)
            print('Wysłano do:{a} wiadomość:{i} z {w}'.format( i=i+1, w=len(addres_mails), a=addres_mails[i] ))
            if (i+1 == len(addres_mails)):
                print('Wszytko wysłane')
        except: 
            print('Coś nie tak!!!')

