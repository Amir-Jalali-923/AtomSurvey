document.addEventListener('DOMContentLoaded', () => {
    let isSelected = false;
    const stars = document.querySelectorAll('.stars span');
    const ratingValue = document.getElementById('rating-value');
    const errorMessage = document.getElementById('error-message');
    const nextButton = document.getElementById('next-button');

    stars.forEach(star => {
        star.addEventListener('click', () => {
            isSelected = true;
            const value = star.getAttribute('data-value');
            updateRating(value);
        });
    });

    function updateRating(value) {
        stars.forEach(star => {
            if (star.getAttribute('data-value') <= value) {
                star.classList.add('selected');
            } else {
                star.classList.remove('selected');
            }
        });
        ratingValue.textContent = value + '.0';
    }

    nextButton.addEventListener('click', () => {
        if (!isSelected) {
            errorMessage.textContent = "Please select a star rating.";
        } else {
            errorMessage.textContent = "";
            alert('Form submitted successfully!');
            // document.querySelector('form').submit(); // Uncomment to submit the form
        }
    });

    // Example for the progress bar
    let currentNumber = document.getElementById('current');
    let progressBar = document.querySelector('.progress-bar');
    progressBar.style.width = Number(currentNumber.textContent) * 5 + "%";

    // Adjust main height on load and resize
    window.addEventListener('load', () => {
        document.querySelector('main').style.height = window.innerHeight - 50 + 'px';
    });
    window.addEventListener('resize', () => {
        document.querySelector('main').style.height = window.innerHeight + 'px';
    });
});
