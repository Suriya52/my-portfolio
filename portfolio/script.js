document.addEventListener('DOMContentLoaded', () => {
    // Example JavaScript code to show form alert
    const form = document.querySelector('form');
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent form submission
        alert('Form submitted!'); // Show alert on form submission
    });
});