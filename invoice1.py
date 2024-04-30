#modify the below script to include the following:
#additional line and a half of spacing between payemnt due by and bill to.
#pay to needs to sit directly above relevant text.
#make description and amount bold.
#center the horizontal line.
#two lines of space between horizontal line and description and items.
# quaver needs to be red and top right above jack perry, currently off.
#add a command line input to for: venue, address, amount.
#increment invoice number by one each time, and add dates automatically.

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, black
from reportlab.pdfgen import canvas

canvas = canvas.Canvas("invoice.pdf", pagesize=letter)
width, height = letter

def draw_line(y, length=460, thickness=1):
    canvas.setLineWidth(thickness)
    canvas.line(left_margin, y, left_margin + length, y)

# Set constant positions
left_margin = 50
middle_column = 350
right_column = width - 100
line_height = 20  # Increased line height for better spacing
section_spacing = 20  # Increased section spacing

canvas.setFont("Helvetica-Bold", 14)

# Draw a quaver note at the top right using an image
quaver_image = "/Users/jackperry/Documents/GitHub/invoice_script/quaver.png"  # replace with your image file path
canvas.drawImage(quaver_image, right_column - 50, height - 50, width=20, height=20)

# Add musician details
musician_name = "Jack Perry"
musician_email = "jackperry13@gmail.com"
musician_phone = "0401 412 059"
y = height - 100

canvas.setFillColor(black)
canvas.setFont("Helvetica-Bold", 14)

# Calculate widths and adjust drawing positions for each piece of information
name_width = canvas.stringWidth(musician_name, "Helvetica-Bold", 14)
canvas.drawString(width - name_width - left_margin, y, musician_name)

canvas.setFont("Helvetica", 12)
email_width = canvas.stringWidth(f"Email: {musician_email}", "Helvetica", 12)
canvas.drawString(width - email_width - left_margin, y - line_height, f"Email: {musician_email}")

phone_width = canvas.stringWidth(f"Phone: {musician_phone}", "Helvetica", 12)
canvas.drawString(width - phone_width - left_margin, y - 2 * line_height, f"Phone: {musician_phone}")

y -= 3 * line_height + section_spacing

# Add invoice details
invoice_number = "INV2023-124"
invoice_date = "July 17, 2023"
due_date = "August 17, 2023"

canvas.drawString(left_margin, y, f"Invoice Number: {invoice_number}")
canvas.drawString(left_margin, y - line_height, f"Date: {invoice_date}")
canvas.drawString(left_margin, y - 2 * line_height, f"Payment Due By: {due_date}")
y -= 3 * line_height + section_spacing

# Add customer details
client_name = "Ballina RSL"
client_address = "1 Grant Street, Ballina, AU 2478"

canvas.setFont("Helvetica-Bold", 12)
canvas.drawString(left_margin, y, "Bill To:")
canvas.setFont("Helvetica", 12)
canvas.drawString(left_margin, y - line_height, client_name)
canvas.drawString(left_margin, y - 2 * line_height, client_address)
y -= 3 * line_height + section_spacing

# Add item details
items = [
    {"description": "Acoustic Set Performance", "amount": "$350.00"},
]

canvas.drawString(left_margin, y, "Description")
canvas.drawString(right_column, y, "Amount")
y -= line_height

for item in items:
    canvas.drawString(left_margin, y, item["description"])
    canvas.drawString(right_column, y, item["amount"])
    y -= line_height

y -= 5

# Add totals
subtotal = "$350.00"
gst = "$35.00" # GST tax of 10%
total = "$385.00"

canvas.drawString(left_margin, y - line_height, "Subtotal:")
canvas.drawString(right_column, y - line_height, subtotal)
canvas.drawString(left_margin, y - 2 * line_height, "GST (10%):")
canvas.drawString(right_column, y - 2 * line_height, gst)
canvas.drawString(left_margin, y - 3 * line_height, "Total:")
canvas.drawString(right_column, y - 3 * line_height, total)
y -= 4 * line_height + section_spacing

# Add Pay To information
pay_to = "Jack Perry"
account_number = "12364645"
bsb = "313140"

canvas.setFont("Helvetica-Bold", 12)

# Measure the width of the text
text_width = canvas.stringWidth("Pay To:", "Helvetica-Bold", 12)
canvas.drawString((width - text_width) / 2, y - 7, "Pay To:")

text_width = canvas.stringWidth(pay_to, "Helvetica-Bold", 12)
canvas.drawString((width - text_width) / 2, y - 5 * line_height, pay_to)

canvas.setFont("Helvetica", 12)

text = f"Account Number: {account_number}"
text_width = canvas.stringWidth(text, "Helvetica", 12)
canvas.drawString((width - text_width) / 2, y - 6 * line_height, text)

text = f"BSB: {bsb}"
text_width = canvas.stringWidth(text, "Helvetica", 12)
canvas.drawString((width - text_width) / 2, y - 7 * line_height, text)
y -= 5 * line_height + section_spacing

# Add "Thank you!"
canvas.setFont("Helvetica-Bold", 14)
canvas.setFillColor(black)
canvas.drawCentredString(width / 2, 50, "Thanks for supporting live music!")

canvas.save()
