use printpdf::*;
use std::fs::File;
use std::io::BufWriter;
use std::path::Path;
use std::env;

fn main() {
    let (doc, page1, layer1) = PdfDocument::new("PDF_Document_title", Mm(210.0), Mm(297.0), "Layer 1");
    let current_layer = doc.get_page(page1).get_layer(layer1);

    let font_path = Path::new("src/Lato/Lato-Regular.ttf");
    let font_file = File::open(font_path).expect("Failed to open font file");
    let font = doc.add_external_font(font_file).expect("Failed to add font");

    let company_name = "Your Company Name";
    let company_address = "Address, City, ZIP";
    let company_phone = "(123) 456-7890";
    let company_email = "info@example.com";

    let invoice_number = "001";
    let invoice_date = "July 17, 2023";
    let due_date = "August 17, 2023";

    current_layer.use_text("\n\n", 12.0, Mm(10.0), Mm(275.0), &font); // Add two line breaks
    current_layer.use_text("\n\n", 12.0, Mm(10.0), Mm(275.0), &font); // Add two line breaks
    current_layer.use_text("\n\n", 12.0, Mm(10.0), Mm(275.0), &font); // Add two line breaks
    current_layer.use_text("\n\n", 12.0, Mm(10.0), Mm(275.0), &font); // Add two line breaks

    let customer_info = "John Smith\n123 Main St, City, ZIP\n(987) 654-3210\njohn@example.com";

    let items = vec![("Item 1 Description", 2, 10.0), ("Item 2 Description", 1, 15.0)];

    let subtotal: f64 = items.iter().map(|item| item.1 as f64 * item.2).sum();
    let shipping = 5.0;
    let tax = subtotal * 0.1;
    let discount = 2.0;
    let total = subtotal + shipping + tax - discount;

    let payment_instructions = "For bank transfer, use the following account details: Account Number: 12364645, BSB: 313140";

    let notes = "Thank you!";

    current_layer.use_text(company_name, 12.0, Mm(10.0), Mm(285.0), &font);
    current_layer.use_text(company_address, 12.0, Mm(10.0), Mm(275.0), &font);
    current_layer.use_text(format!("Phone: {}", company_phone), 12.0, Mm(10.0), Mm(265.0), &font);
    current_layer.use_text(format!("Email: {}", company_email), 12.0, Mm(10.0), Mm(255.0), &font);

    current_layer.use_text(format!("Invoice Number: {}", invoice_number), 12.0, Mm(10.0), Mm(245.0), &font);
    current_layer.use_text(format!("Invoice Date: {}", invoice_date), 12.0, Mm(10.0), Mm(235.0), &font);
    current_layer.use_text(format!("Due Date: {}", due_date), 12.0, Mm(10.0), Mm(225.0), &font);

    current_layer.use_text(customer_info, 12.0, Mm(10.0), Mm(215.0), &font);

    let mut y_position = 205.0;
    for (description, quantity, price) in &items {
        current_layer.use_text(format!("{} | {} | ${}", description, quantity, price), 12.0, Mm(10.0), Mm(y_position), &font);
        y_position -= 10.0;
    }

    current_layer.use_text(format!("Subtotal: ${}", subtotal), 12.0, Mm(10.0), Mm(y_position), &font);
    y_position -= 10.0;

    current_layer.use_text(format!("Shipping: ${}", shipping), 12.0, Mm(10.0), Mm(y_position), &font);
    y_position -= 10.0;

    current_layer.use_text(format!("Tax (10%): ${}", tax), 12.0, Mm(10.0), Mm(y_position), &font);
    y_position -= 10.0;

    current_layer.use_text(format!("Discount: -${}", discount), 12.0, Mm(10.0), Mm(y_position), &font);
    y_position -= 10.0;

    current_layer.use_text(format!("Total: ${}", total), 12.0, Mm(10.0), Mm(y_position), &font);
    y_position -= 10.0;

    current_layer.use_text(payment_instructions, 12.0, Mm(10.0), Mm(y_position), &font);
    y_position -= 10.0;

    current_layer.use_text(notes, 12.0, Mm(10.0), Mm(y_position), &font);

    let current_dir = env::current_dir().unwrap();
    let file_path = current_dir.join("Invoice.pdf");
    let file_path_str = file_path.to_string_lossy().to_string();

    match doc.save(&mut BufWriter::new(File::create(Path::new(&file_path_str)).unwrap())) {
        Ok(_) => println!("Successfully saved the invoice to: {}", file_path_str),
        Err(err) => eprintln!("Failed to save the invoice: {}", err),
    }
}




