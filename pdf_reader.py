from PyPDF2 import PdfReader
import UI_creator
import re

def extract_text_from_pdf(text):
    data = {
        'invoice_no': None,
        'date': None,
        'customer': None,
        'billing_address': None,
        'shipping_address': None,
        'products': [],
        'total_net': None,
        'total_vat': None,
        'total': None
    }

    # Extract invoice number
    match = re.search(r"Invoice No:\s*(\d+)", text)
    if match:
        data['invoice_no'] = match.group(1)

    # Extract invoice date
    match = re.search(r"Date:\s*([0-9/]+)", text)
    if match:
        data['date'] = match.group(1)

    # Extract billing and shipping
    billing_match = re.search(r"Invoice to:\s*(.*?)Deliver to:", text, re.DOTALL)
    shipping_match = re.search(r"Deliver to:\s*(.*?)\n\n", text, re.DOTALL)
    if billing_match:
        data['billing_address'] = billing_match.group(1).strip()
    if shipping_match:
        data['shipping_address'] = shipping_match.group(1).strip()

    # Extract product lines
    product_lines = re.findall(r"(\w+)\s+([^\n]+?)\s+(\d+)\s+£([\d.]+)", text)
    for code, desc, qty, price in product_lines:
        data['products'].append({
            'code': code,
            'description': desc.strip(),
            'quantity': int(qty),
            'unit_price': float(price)
        })

    # Extract totals
    match = re.search(r"Total Net Amount\s*£([\d.]+)", text)
    if match:
        data['total_net'] = float(match.group(1))

    match = re.search(r"Total VAT Amount\s*£([\d.]+)", text)
    if match:
        data['total_vat'] = float(match.group(1))

    match = re.search(r"Invoice Total\s*£([\d.]+)", text)
    if match:
        data['total'] = float(match.group(1))

    return data

UI_creator.ui_creator()
reader = PdfReader(UI_creator.get_file_path()) #read the file using the path from UI_creator.py
full_text = ""
# Iterate through each page and extract text
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        full_text += page_text + "\n"
print("Invoice Data:")
invoice_data=extract_text_from_pdf(full_text)


#print(invoice_data) #print the data extracted from the pdf file