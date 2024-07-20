// filling header and footer
import { HeaderFiller, FooterFiller } from "./Filler.js";
import { asideActivator } from "./AsideActivator.js";

// calling the footer and header filler functions
FooterFiller();
HeaderFiller();

// calling the aside codes
asideActivator();

window.addEventListener('load', () => {
    let main = document.querySelector('main');
    main.style.height = (window.innerHeight - 50) + "px";
});

let subButton = document.querySelector('form button');
subButton.addEventListener('click', (event) => {
    event.preventDefault();

    let isValid = true;
    let name = document.getElementById('name').value.trim();
    let email = document.getElementById('email').value.trim();
    let message = document.getElementById('message').value.trim();
    let errorMessage = document.querySelector('.error');


    errorMessage.textContent = '';

    if (name === '') {
        isValid = false;
        errorMessage.textContent = 'نام و نام خانوادگی اجباری است.';
    }

    if (email === '') {
        isValid = false;
        errorMessage.textContent = 'ایمیل اجباری است.';
    } else if (!validateEmail(email)) {
        isValid = false;
        errorMessage.textContent = 'ایمیل نامعتبر است.';
    }

    if (message === '') {
        isValid = false;
        errorMessage.textContent = 'پیام اجباری است.';
    }

    if (isValid) {
        alert('فرم با موفقیت ارسال شد!');
        document.querySelector('form').submit();
    }
});

// validation for email
function validateEmail(email) {
    email = email.toLowerCase().trim();

    // Basic checks for the presence of "@" and "."
    const atSymbol = email.indexOf('@');
    const dot = email.lastIndexOf('.');

    // Check for at least one "@" symbol, one "." after "@", and no "@" or "." at the start or end
    if (atSymbol > 0 && dot > atSymbol + 1 && dot < email.length - 1) {
        return true;
    }

    return false;
}
