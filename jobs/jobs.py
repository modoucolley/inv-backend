from fpdf import FPDF, HTMLMixin
import store

class PDF(FPDF, HTMLMixin):
    pass

def create_pdffile():
    pdf = PDF()
    pdf.add_page()
    product_count = store.models.Product.objects.all().count()

    pdf.write_html(f"""
    <h1>Gomindz Inventory Report</h1>
    <h3>Kairaba Avenue</h3>
    <section>
        <h2>Products - {product_count}</h2>
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
        <h2>Orders</h2>
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
    pdf.output('static/documents/Dailyreport.pdf')



from twilio.rest import Client



def send_message():

    create_pdffile()

    client.messages.create(
        from_='whatsapp:+14155238886',
        body= "Hi",
        #media_url='https://www.aims.ca/site/media/aims/2.pdf',
        media_url='https://cda6-41-223-213-220.eu.ngrok.io/static/documents/DailyReport.pdf',
        to='whatsapp:+2207677435',
        #to='whatsapp:+2203258685',
        #to='whatsapp:+2205260188',
    )