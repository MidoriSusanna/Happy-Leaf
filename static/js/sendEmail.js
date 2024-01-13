// Function to make contact form work properly
function sendMail(contactForm) {
    // Retrieve values from form elements
    let fromName = document.getElementById('form-group-input1').value;
    let fromSurname = document.getElementById('form-group-input2').value;
    let fromEmail = document.getElementById('email-input').value;
    let inquiryType = document.getElementById('inquiry-type').value;
    let message = document.getElementById('textarea-message').value;

    // Check if the privacy checkbox is checked
    var privacyCheckbox = document.getElementById('privacy-checkbox');
    var privacyAgreement = privacyCheckbox.checked;

    // Validate the privacy agreement
    if (!privacyAgreement) {
        alert("Please agree to the privacy policy before submitting the form.");
        return false; // Prevent form submission
    }
    // Use the retrieved values to populate the emailjs.send function
    emailjs.send("service_fvvbjge", "happy-leaf-template", {
        "from_name": fromName,
        "from_surname": fromSurname,
        "from_email": fromEmail,
        "inquiry_type": inquiryType,
        "message": message
    });
}