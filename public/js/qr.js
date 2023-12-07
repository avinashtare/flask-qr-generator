// DOM elements
const qrText = document.getElementById("qr-text");
const createQrBtn = document.getElementById("qr-btn");
const imagesArea = document.getElementById("imageArea");

// Asynchronous function to request QR code
const requestQr = async (text) => {
    // Check if text exceeds a certain length
    if (text.length > 500) return {}; // Return empty object if text is too long

    // Fetch QR code from server
    let response = await fetch("/get-qr", {
        method: "POST", // Corrected the HTTP method to "POST"
        body: JSON.stringify({ text }),
        headers: {
            "Content-Type": "application/json",
        },
    });

    // Parse the JSON response
    response = await response.json();

    return response;
};

// Event listener for the "Create QR" button
createQrBtn.addEventListener("click", async () => {
    // Get the value from the input field
    let qrValue = qrText.value;

    // Request a QR code using the entered text
    let response = await requestQr(qrValue);

    // Check if the response contains a statusText property
    if (response.statusText) {
        // Create an image element for the QR code
        let img = document.createElement("img");
        img.src = response.base64;
        img.width = 300;

        // Append first child the image to the images area
        imagesArea.prepend(img);

        // clear input 
        qrText.value = ""
    } else {
        // Display an alert if there is a server error
        alert("Server Error");
    }
});
