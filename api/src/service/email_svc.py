import os
import platform
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email.utils import formatdate

USERNAME_SMTP = os.environ.get("USERNAME_SMTP", "AKIAQIS5BR74W3OJUQDP")

PASSWORD_SMTP = os.environ.get(
    "PASSWORD_SMTP", "BEXWjHW63jWNIaZHpK5eiP2XkCaKk4fdc2v73LYLgVlD"
)

FROM_EMAIL = os.environ.get("FROM_EMAIL", "admin@simplychinese.ca")
HOST = os.environ.get("HOST", "email-smtp.us-east-1.amazonaws.com")
PORT = os.environ.get("PORT", 587)


def send(
    to_list,
    subject,
    text,
    sender=FROM_EMAIL,
    cc_list=None,
    bcc_list=None,
    files=None,
    format="html",
    server=HOST,
    port=PORT,
    footer=False,
    priority=3,
    env_in_title=False,
):
    assert isinstance(to_list, list)

    env_name = os.environ.get("ENV_NAME", "Unknown")
    try:
        machine_name = os.uname().nodename
    except AttributeError:
        # os.uname doesn't work on Windows
        machine_name = platform.uname().node

    email_footer = (
        "<br/>" * 5
        + f"""
        <hr/>
        <div>Environment: {env_name} | Machine: {machine_name}</div>
        """
        if footer
        else ""
    )

    subject_prefix = f"{env_name}: " if env_in_title else ""

    subject_suffix = os.environ.get("EMAIL_SUBJECT_SUFFIX", "")

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = COMMASPACE.join(to_list)
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = f"{subject_prefix}{subject}{subject_suffix}"
    msg["X-Priority"] = str(priority)
    if cc_list:
        msg["Cc"] = COMMASPACE.join(cc_list)

    if bcc_list:
        msg["Bcc"] = COMMASPACE.join(bcc_list)

    msg.attach(MIMEText(text + email_footer, format))

    for f in files or []:
        f["content"].seek(0)
        part = MIMEApplication(f["content"].read(), f["name"])
        # After the file is closed
        part["Content-Disposition"] = 'attachment; filename="{}"'.format(f["name"])
        msg.attach(part)

    rcpt = to_list + (cc_list or []) + (bcc_list or [])
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(USERNAME_SMTP, PASSWORD_SMTP)
    smtp.sendmail(sender, rcpt, msg.as_string())
    smtp.close()
