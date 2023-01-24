from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

account_sid = 'ACa3061a8c10d45fe7dad1c698fad82ff3'
authToken = '9587c5e7b8dcd9d5448203fa302b591d'
client = Client(account_sid, authToken)

def send_message():
    client.messages.create(
        from_='whatsapp:+14155238886',
        body= "Hi",
        media_url='https://www.aims.ca/site/media/aims/2.pdf',
        #media_url='https://91d7-197-255-199-14.eu.ngrok.io/static/images/gooo.pdf',
        to='whatsapp:+2207677435',
        #to='whatsapp:+2203258685',
        #to='whatsapp:+2205260188',
    )


from fpdf import FPDF, HTMLMixin
import os 

class PDF(FPDF, HTMLMixin):
    pass

def create_pdffile():
    pdf = PDF()
    pdf.add_page()
    pdf.write_html("""
    <h1>Big title</h1>
    <section>
        <h2>Section title</h2>
        <p><b>Hello</b> world. <u>I am</u> <i>tired</i>.</p>
        <p><a href="https://github.com/PyFPDF/fpdf2">PyFPDF/fpdf2 GitHub repo</a></p>
        <p align="right">right aligned text</p>
        <p>i am a paragraph <br />in two parts.</p>
        <font color="#00ff00"><p>hello in green</p></font>
        <font size="7"><p>hello small</p></font>
        <font face="helvetica"><p>hello helvetica</p></font>
        <font face="times"><p>hello times</p></font>
    </section>
    <section>
        <h2>Other section title</h2>
        <ul><li>unordered</li><li>list</li><li>items</li></ul>
        <ol><li>ordered</li><li>list</li><li>items</li></ol>
        <br>
        <br>
        <pre>i am preformatted text.</pre>
        <br>
        <blockquote>hello blockquote</blockquote>
        <table width="100%">
        <thead>
            <tr>
            <th width="30%">Product Name</th>
            <th width="70%">Product ID</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td>1</td>
            <td>10</td>
            </tr>
            <tr>
            <td>2</td>
            <td>Bob</td>
            </tr>
        </tbody>
        </table>
    </section>
    """)
    pdf.output('static/images/report.pdf')


import requests
import schedule
import time

#schedule.every().day.at('11:36').do(create_pdffile)
#schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)

