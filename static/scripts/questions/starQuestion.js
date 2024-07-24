document.addEventListener('DOMContentLoaded', () => {
    let isSelected = false;
    const stars = document.querySelectorAll('.stars span');
    const ratingValue = document.getElementById('rating-value');
    const errorMessage = document.getElementById('error-message');
    const nextButton = document.getElementById('next-button');
    const questionNum = Number(document.getElementById('questionNUmber').textContent);


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
        ratingValue.textContent = value;
        document.getElementById('rating-input').value = value;
    }

    nextButton.addEventListener('click', () => {
        if (!isSelected) {
            errorMessage.textContent = "Please select a star rating.";
        } else {
            errorMessage.textContent = "";
            document.querySelector('form').submit(); // Uncomment to submit the form
        }
    });

    // Adjust main height on load and resize
    window.addEventListener('load', () => {
        document.querySelector('main').style.height = window.innerHeight - 50 + 'px';
    });
    window.addEventListener('resize', () => {
        document.querySelector('main').style.height = window.innerHeight + 'px';
    });

    function ProgressChange() {
        let current = document.getElementById('currentQue').textContent;
        let progressBar = document.querySelector('.progress-bar');
        progressBar.style.width = Number(current) * 100 / questionNum + "%";
    }
    ProgressChange()
});
