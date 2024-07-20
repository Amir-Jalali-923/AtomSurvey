document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  const nameInput = document.querySelector('.name');
  const emailInput = document.querySelector('.email');
  const gcodeInput = document.querySelector('.GcodeP');
  const passwordInput = document.querySelector('.pass');
  const confirmPasswordInput = document.querySelector('.confirmation');
  const gcodeErrorP = document.querySelector('.GcodeP + p');
  const confirmationErrorP = document.querySelector('.confirmationErrorP');
  const nextButton = document.querySelector('.nextBtn');

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let isValid = true;
    let errorMessage = '';

    // Clear previous error messages
    gcodeErrorP.textContent = '';
    confirmationErrorP.textContent = '';

    // Validate name
    if (nameInput.value.trim() === '') {
      isValid = false;
      errorMessage = 'لطفا نام خود را وارد کنید.';
      nameInput.focus();
    }

    // Validate email
    if (isValid && !validateEmail(emailInput.value)) {
      isValid = false;
      errorMessage = 'لطفا یک ایمیل معتبر وارد کنید.';
      emailInput.focus();
    }

    // Validate Gcode
    if (isValid && (gcodeInput.value.length !== 10 || !/^\d{10}$/.test(gcodeInput.value))) {
      isValid = false;
      gcodeErrorP.textContent = 'کد ملی باید ۱۰ رقم باشد.';
      gcodeInput.focus();
    }

    // Validate password
    if (isValid && passwordInput.value.length < 6) {
      isValid = false;
      errorMessage = 'رمز عبور باید حداقل ۶ کاراکتر باشد.';
      passwordInput.focus();
    }

    // Validate confirm password
    if (isValid && passwordInput.value !== confirmPasswordInput.value) {
      isValid = false;
      confirmationErrorP.textContent = 'رمز عبور و تکرار آن یکسان نیستند.';
      confirmPasswordInput.focus();
    }

    if (isValid) {
      // If all validations pass, submit the form
      form.submit();
    } else if (errorMessage) {
      alert(errorMessage);
    }
  });

  function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
  }
});
