from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pika
import configparser
import json
import time
import sys

time.sleep(10)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='email.notify')

config = configparser.ConfigParser()
config.read('secret.ini')
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(config['notify']['email'], config['notify']['password'])
# server.login('rest.api.homework@gmail.com', 'your_password')


def email_callback(ch, method, properties, body: str):
    data = json.loads(body)
    msg = MIMEMultipart()
    print(body, file=sys.stderr)
    msg.attach(MIMEText(data['message'], 'plain'))
    msg['From'] = config['notify']['email']
    msg['To'] = data['To']
    # msg['Subject'] = data['Subject']
    server.sendmail(msg['From'], msg['To'], msg.as_string())


channel.basic_consume(queue='email.notify', on_message_callback=email_callback)
channel.start_consuming()
server.quit()
