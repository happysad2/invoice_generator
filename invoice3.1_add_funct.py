#last invoice 128

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, black
from reportlab.pdfgen import canvas
from datetime import date, timedelta

canvas = canvas.Canvas("invoice.pdf", pagesize=letter)
width, height = letter

print(height)

#store inputs from user as variables.
def key_changes():
    today_date = date.today().strftime("%B %d, %Y") 
    year = today_date[-4:]

    invoice_number = 'INV' + year + '-' + input('Invoice no, ')
    client_name = input('Client name, ')
    client_address = input('Client address, ')
    performance_date = input('Performance date, ')
    total_cost = input('Total cost, ')

    return invoice_number, client_name, client_address, total_cost, performance_date

# assigns returned values to the variables.
invoice_number, client_name, client_address, total_cost, performance_date = key_changes()

# print(invoice_number)
# print(client_name)
# print(client_address)
# print(total_cost)

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
musician_abn = "48627871659"
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

abn_width = canvas.stringWidth(f"ABN: {musician_abn}", "Helvetica", 12)
canvas.drawString(width - abn_width - left_margin, y - 3 * line_height, f"ABN: {musician_abn}")

y -= 4 * line_height + section_spacing

# Add invoice details
# invoice_number = invoice_number  # Replace this with a function to get the correct invoice number
invoice_date = date.today().strftime("%B %d, %Y")  # Get today's date
# performance_date = date(year=2023, month=7, day=15)  # Example: Performance is on July 15, 2023
due_date = (date.today() + timedelta(days=7)).strftime("%B %d, %Y")  # Get date 7 days from the invoice

canvas.drawString(left_margin, y, f"Invoice Number: {invoice_number}")
y -= line_height  # Move down for the next line
canvas.drawString(left_margin, y, f"Performance date: {performance_date}")
y -= line_height  # Move down for the next line
canvas.drawString(left_margin, y, f"Date: {invoice_date}")
y -= line_height  # Move down for the next line
canvas.drawString(left_margin, y, f"Payment Due By: {due_date}")
y -= section_spacing  # Additional spacing before the next section

y -= 1 * line_height + section_spacing
# Change customer details here....
# client_name = client_name
# client_address = client_address

canvas.setFont("Helvetica-Bold", 12)
canvas.drawString(left_margin, y, "Bill To:")
canvas.setFont("Helvetica", 12)
canvas.drawString(left_margin, y - line_height, client_name)
canvas.drawString(left_margin, y - 2 * line_height, client_address)
y -= 3 * line_height + 2 * section_spacing

# Add item details
items = [
    {"description": "Acoustic Set Performance", "amount": total_cost},
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
total = total_cost
canvas.drawString(left_margin, y - line_height, "Total:")
canvas.drawString(right_column, y - line_height, total)
y -= 2 * line_height + section_spacing

# Add Pay To information
canvas.setFont("Helvetica-Bold", 12)
pay_to = "Jack Perry"  # Pay To information defined here

# Draw "Pay To:" centered
text_width = canvas.stringWidth("Pay To:", "Helvetica-Bold", 12)
canvas.drawString((width - text_width) / 2, y, "Pay To:")
y -= line_height  # Move down for the next line

# Draw pay_to name centered
text_width = canvas.stringWidth(pay_to, "Helvetica-Bold", 12)
canvas.drawString((width - text_width) / 2, y, pay_to)
y -= line_height  # Move down for the next line

canvas.setFont("Helvetica", 12)
account_number = "12364645"
bsb = "313140"

# Draw account number centered
text = f"Account Number: {account_number}"
text_width = canvas.stringWidth(text, "Helvetica", 12)
canvas.drawString((width - text_width) / 2, y, text)
y -= line_height  # Move down for the next line

# Draw BSB centered
text = f"BSB: {bsb}"
text_width = canvas.stringWidth(text, "Helvetica", 12)
canvas.drawString((width - text_width) / 2, y, text)
y -= line_height + section_spacing  # Additional spacing before the next section

# Add "Thank you!" at the bottom of the page
bottom_thanks = line_height - 8
print('height :', height, 'bottom thanks ', bottom_thanks)
canvas.drawCentredString(width / 2, bottom_thanks, "Thanks for supporting live music!")

canvas.save()
