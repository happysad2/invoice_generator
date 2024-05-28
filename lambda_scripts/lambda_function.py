import os
import json
from datetime import date, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, black
from reportlab.pdfgen import canvas
import boto3
import style_invoice
import save_2_s3

def lambda_handler(event, context):
    print(event)
    data = json.loads(event['body'])

    invoice_number = data.get('invoice_number')
    client_name = data.get('client_name')
    client_address = data.get('client_address')
    performance_date = data.get('performance_date')
    total_cost = data.get('total_cost')
    
    #STYLE
    try:
        invoice_canvas = style_invoice.style(invoice_number, client_name, client_address, performance_date, total_cost)
        invoice_canvas.save()  # Saves to /tmp/invoice.pdf as specified in the style() function
    except Exception as e:
        print(f'Error styling the invoice: {str(e)}')

    #UPLOAD 2 S3
    # Check if the file exists before attempting to upload
    if os.path.exists("/tmp/invoice.pdf"):
        try:
            save_2_s3.s3save('/tmp/invoice.pdf', 'jack-invoice-gen', f'invoice-{invoice_number}.pdf')
            print("Invoice file created and uploaded successfully.")
        except Exception as e:
            print(f'Error saving to S3: {str(e)}')
    else:
        print("Failed to create the invoice file.")

    #RETURN LOG 'SUCCESS OR NO'
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "Upload successful"}),
        "isBase64Encoded": False
    }
