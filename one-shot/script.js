document.addEventListener('DOMContentLoaded', () => {
    // Add to Cart button functionality
    const buttons = document.querySelectorAll('.product-item button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            alert('Item added to cart!');
        });
    });
});
