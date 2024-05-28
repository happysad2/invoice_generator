from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, black
from reportlab.pdfgen.canvas import Canvas
from datetime import date, timedelta
import boto3

def style(invoice_number, client_name, client_address, performance_date, total_cost):
    
    s3 = boto3.client('s3')
    s3.download_file('jack-invoice-gen', 'quaver.png', '/tmp/quaver.png')
    
    invoice_number = str(invoice_number)
    client_name = str(client_name)
    client_address = str(client_address)
    performance_date = str(performance_date)
    total_cost = str(total_cost)
    
    # Define width, height
    width, height = letter
    invoice_canvas = Canvas("/tmp/invoice.pdf", pagesize=letter)
    
    def draw_line(y, length=460, thickness=1):
        invoice_canvas.setLineWidth(thickness)
        invoice_canvas.line((width - length) / 2, y, (width + length) / 2, y)
    
    left_margin = 50
    middle_column = 350
    right_column = width - 100
    line_height = 20
    section_spacing = 30
    
    invoice_canvas.setFont("Helvetica-Bold", 14)
    
    # Draw a quaver note at the top right using an image
    invoice_canvas.setFillColor(red)
    invoice_canvas.drawImage('/tmp/quaver.png', right_column + 10, height - 70, width=20, height=20)
    
    musician_name = "Jack Perry"
    musician_email = "jackperry13@gmail.com"
    musician_phone = "0401412059"
    musician_abn = "48627871659"
    y = height - 100
    
    invoice_canvas.setFillColor(black)
    invoice_canvas.setFont("Helvetica-Bold", 14)
    name_width = invoice_canvas.stringWidth(musician_name, "Helvetica-Bold", 14)
    invoice_canvas.drawString(width - name_width - left_margin, y, musician_name)
    
    invoice_canvas.setFont("Helvetica", 12)
    email_width = invoice_canvas.stringWidth(f"Email: {musician_email}", "Helvetica", 12)
    invoice_canvas.drawString(width - email_width - left_margin, y - line_height, f"Email: {musician_email}")
    
    phone_width = invoice_canvas.stringWidth(f"Phone: {musician_phone}", "Helvetica", 12)
    invoice_canvas.drawString(width - phone_width - left_margin, y - 2 * line_height, f"Phone: {musician_phone}")
    
    abn_width = invoice_canvas.stringWidth(f"ABN: {musician_abn}", "Helvetica", 12)
    invoice_canvas.drawString(width - abn_width - left_margin, y - 3 * line_height, f"ABN: {musician_abn}")
    
    y -= 4 * line_height + section_spacing
    invoice_canvas.drawString(left_margin, y, f"Invoice Number: {invoice_number}")
    y -= line_height
    invoice_canvas.drawString(left_margin, y, f"Performance date: {performance_date}")
    y -= line_height
    # invoice_canvas.drawString(left_margin, y, f"Date: {invoice_date}")
    # y -= line_height
    # invoice_canvas.drawString(left_margin, y, f"Payment Due By: {due_date}")
    # y -= section_spacing
    
    invoice_canvas.setFont("Helvetica-Bold", 12)
    invoice_canvas.drawString(left_margin, y, "Bill To:")
    invoice_canvas.setFont("Helvetica", 12)
    invoice_canvas.drawString(left_margin, y - line_height, client_name)
    invoice_canvas.drawString(left_margin, y - 2 * line_height, client_address)
    y -= 3 * line_height + 2 * section_spacing
    
    items = [{"description": "Acoustic Set Performance", "amount": total_cost}]
    invoice_canvas.setFont("Helvetica-Bold", 12)
    invoice_canvas.drawString(left_margin, y, "Description")
    invoice_canvas.drawString(right_column, y, "Amount")
    y -= line_height
    
    for item in items:
        invoice_canvas.drawString(left_margin, y, item["description"])
        invoice_canvas.drawString(right_column, y, item["amount"])
        y -= line_height
    
    draw_line(y, thickness=2)
    y -= line_height * 2
    
    total = total_cost
    invoice_canvas.drawString(left_margin, y - line_height, "Total:")
    invoice_canvas.drawString(right_column, y - line_height, total)
    y -= 2 * line_height + section_spacing
    
    pay_to = "Jack Perry"
    text_width = invoice_canvas.stringWidth("Pay To:", "Helvetica-Bold", 12)
    invoice_canvas.drawString((width - text_width) / 2, y, "Pay To:")
    y -= line_height
    
    text_width = invoice_canvas.stringWidth(pay_to, "Helvetica-Bold", 12)
    invoice_canvas.drawString((width - text_width) / 2, y, pay_to)
    y -= line_height
    
    account_number = "12364645"
    bsb = "313140"
    text = f"Account Number: {account_number}"
    text_width = invoice_canvas.stringWidth(text, "Helvetica", 12)
    invoice_canvas.drawString((width - text_width) / 2, y, text)
    y -= line_height
    
    text = f"BSB: {bsb}"
    text_width = invoice_canvas.stringWidth(text, "Helvetica", 12)
    invoice_canvas.drawString((width - text_width) / 2, y, text)
    y -= line_height + section_spacing
    
    bottom_thanks = line_height - 8
    invoice_canvas.drawCentredString(width / 2, bottom_thanks, "Thanks for supporting live music!")
    
    return invoice_canvas
