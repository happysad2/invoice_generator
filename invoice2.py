#thanks for supporting live music should be at the bottom of the page.
#pay to details should be after the total colume sitting between that and the thanks for supporting live music which sits at the bottom

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, black
from reportlab.pdfgen import canvas
from datetime import date, timedelta

canvas = canvas.Canvas("invoice.pdf", pagesize=letter)
width, height = letter

def draw_line(y, length=460, thickness=1):
    canvas.setLineWidth(thickness)
    canvas.line((width - length) / 2, y, (width + length) / 2, y)  # Updated to center the line

# Set constant positions
left_margin = 50
middle_column = 350
right_column = width - 100
line_height = 20  # Increased line height for better spacing
section_spacing = 30  # Increased section spacing

canvas.setFont("Helvetica-Bold", 14)

# Draw a quaver note at the top right using an image
quaver_image = "/Users/jackperry/Documents/GitHub/invoice_script/quaver.png"  # replace with your image file path
canvas.setFillColor(red)
canvas.drawImage(quaver_image, right_column + 10, height - 70, width=20, height=20)

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
invoice_number = "INV2023-125"  # Replace this with a function to get the correct invoice number
invoice_date = date.today().strftime("%B %d, %Y")  # Get today's date
due_date = (date.today() + timedelta(days=30)).strftime("%B %d, %Y")  # Get date 30 days from today

canvas.drawString(left_margin, y, f"Invoice Number: {invoice_number}")
canvas.drawString(left_margin, y - line_height, f"Date: {invoice_date}")
canvas.drawString(left_margin, y - 2 * line_height, f"Payment Due By: {due_date}")
y -= 3 * line_height + section_spacing

# Add customer details
client_name = "Hotel Ravesis"
client_address = "118 Campbell Parade, Bondi Beach, NSW, 2026"

canvas.setFont("Helvetica-Bold", 12)
canvas.drawString(left_margin, y, "Bill To:")
canvas.setFont("Helvetica", 12)
canvas.drawString(left_margin, y - line_height, client_name)
canvas.drawString(left_margin, y - 2 * line_height, client_address)
y -= 3 * line_height + 2 * section_spacing

# Add item details
items = [
    {"description": "Acoustic Set Performance", "amount": "$350.00"},
]

canvas.setFont("Helvetica-Bold", 12)  # Make Description and Amount bold
canvas.drawString(left_margin, y, "Description")
canvas.drawString(right_column, y, "Amount")
y -= line_height

canvas.setFont("Helvetica", 12)
for item in items:
    canvas.drawString(left_margin, y, item["description"])
    canvas.drawString(right_column, y, item["amount"])
    y -= line_height

y -= line_height * 2  # Add two lines of space before the line
draw_line(y, thickness=2)
y -= line_height * 2  # Add two lines of space after the line

# Add totals
subtotal = "$200.00"
# gst = "$35.00" # GST tax of 10%
total = "$200.00"

canvas.drawString(left_margin, y - line_height, "Subtotal:")
canvas.drawString(right_column, y - line_height, subtotal)
canvas.drawString(left_margin, y - 2 * line_height, "GST (10%):")
canvas.drawString(right_column, y - 2 * line_height, gst)
canvas.drawString(left_margin, y - 3 * line_height, "Total:")
canvas.drawString(right_column, y - 3 * line_height, total)
y -= 4 * line_height + section_spacing

# Your previous code remains the same until the total section

# Add Pay To information
canvas.setFont("Helvetica-Bold", 12)
pay_to = "Jack Perry" # Pay To information defined here
text_width = canvas.stringWidth("Pay To:", "Helvetica-Bold", 12)
canvas.drawString((width - text_width) / 2, y - 2 * line_height, "Pay To:")

text_width = canvas.stringWidth(pay_to, "Helvetica-Bold", 12)
canvas.drawString((width - text_width) / 2, y - 3 * line_height, pay_to)

canvas.setFont("Helvetica", 12)
account_number = "12364645"
bsb = "313140"

text = f"Account Number: {account_number}"
text_width = canvas.stringWidth(text, "Helvetica", 12)
canvas.drawString((width - text_width) / 2, y - 4 * line_height, text)

text = f"BSB: {bsb}"
text_width = canvas.stringWidth(text, "Helvetica", 12)
canvas.drawString((width - text_width) / 2, y - 5 * line_height, text)
y -= 2 * line_height + section_spacing

# Add "Thank you!" at the bottom of the page
canvas.setFont("Helvetica-Bold", 14)
canvas.setFillColor(black)
y = 150  # or any suitable number to position the text at the bottom
canvas.drawCentredString(width / 2, 30, "Thanks for supporting live music!")


canvas.save()



