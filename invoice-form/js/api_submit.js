document.getElementById('invoiceForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Collect form data
    const invoiceData = {
        invoice_number: document.getElementById('invoice_number').value,
        client_name: document.getElementById('client_name').value,
        client_address: document.getElementById('client_address').value,
        performance_date: document.getElementById('performance_date').value,
        total_cost: document.getElementById('total_cost').value
    };

    // Send the data as a JSON object to the API Gateway
    fetch('https://kbelfu0tmd.execute-api.ap-southeast-2.amazonaws.com/InvGen', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(invoiceData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => console.log('Success:', data))
    .catch(error => console.error('Error:', error));
    console.log("JavaScript file loaded successfully.");
});
