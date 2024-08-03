document.addEventListener('DOMContentLoaded', () => {
    // Add to Cart button functionality can be implemented here
    const buttons = document.querySelectorAll('.product-item button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            alert('Item added to cart!');
        });
    });
});
