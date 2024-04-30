import os
import json
from datetime import date, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, black
from reportlab.pdfgen import canvas

def create_invoice(event):
    # Extract information from event
    invoice_number = event['invoice_number']
    client_name = event['client_name']
    client_address = event['client_address']
    performance_date = event['performance_date']
    total_cost = event['total_cost']

    # Set up PDF canvas
    file_path = "/tmp/invoice.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Draw content
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 750, f"Invoice Number: {invoice_number}")
    c.drawString(50, 730, f"Client Name: {client_name}")
    c.drawString(50, 710, f"Client Address: {client_address}")
    c.drawString(50, 690, f"Performance Date: {performance_date}")
    c.drawString(50, 670, f"Total Cost: ${total_cost}")

    # Save PDF
    c.save()

    # Read PDF content (for demonstration)
    with open(file_path, "rb") as f:
        pdf_content = f.read()

    # Encode PDF content in base64 to return as a response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/pdf",
        },
        "body": pdf_content.decode("base64"),
        "isBase64Encoded": True
    }

def lambda_handler(event, context):
    return create_invoice(json.loads(event['body']))
