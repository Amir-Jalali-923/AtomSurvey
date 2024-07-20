// Showing password
let showPassword = document.getElementById('showPassword');
let input1 = document.getElementById('currentPassword');
let input2 = document.getElementById('password');
let input3 = document.getElementById('repassword');
let errorMessage = document.getElementById('errorMessage');

// Function for showing and hiding the password
showPassword.addEventListener('change', () => {  // Changed 'input' to 'change'
    if (showPassword.checked) {
        input1.type = "text";
        input2.type = "text";
        input3.type = "text";
    } else {
        input1.type = "password";
        input2.type = "password";
        input3.type = "password";
    }
});

// Function for checking the input to be valid
function checkLatin(input) {
    // Regular expression to match only Latin letters and numbers, no spaces
    const regex = /^[A-Za-z0-9]+$/;
    return regex.test(input.value); // Changed 'input' to 'input.value'
}

// Function for checking the inputs to not be empty
function checkValid(inp) {
    return inp.value !== undefined && inp.value !== ""; // Simplified the function
}
function checkLength(inp) {
    if (inp.value.length < 8)
        return false;
    else
        return true;
}
function checkPassword(inp1, inp2) {
    if (inp1.value === inp2.value)
        return true;
    else
        return false;
}
// Function for submit button
let submitButton = document.querySelector('.submitButton');
submitButton.addEventListener('click', (event) => {  // Added 'event' parameter
    let condition = true;  // Moved inside the event listener

    // Checking if the inputs are valid and not empty
    if (!checkValid(input1) || !checkValid(input2) || !checkValid(input3)) {
        errorMessage.textContent = "بعضی از فیلد ها خالی میباشد";
        errorMessage.style.color = "red";
        condition = false;
    }
    // checking the inputs values to be latin and English
    else if (!checkLatin(input1) || !checkLatin(input2) || !checkLatin(input3)) {
        errorMessage.textContent = "باید در رمز از حروف لاتین و اعداد استفاده شود";
        errorMessage.style.color = "red";
        condition = false;
    }
    else {
        errorMessage.textContent = "";
        console.log("Both inputs are valid and Latin");
    }
    // checking the passwords to be same
    if (!checkPassword(input2, input3)) {
        errorMessage.textContent = "رمز و تکرار رمز هم خوانی ندارد";
        errorMessage.style.color = "red";
        condition = false;
    }
    // checking the Length of inputs 
    if (!checkLength(input1) && !checkLength(input2) && !checkLength(input3)) {
        errorMessage.textContent = "باید رمز ها بیشتر از 8 کاراکتر باشد";
        errorMessage.style.color = "red";
        condition = false;
    }
    // Prevent form submission if condition is false
    if (condition) {
        document.querySelector('form').submit();
    } else {
        event.preventDefault(); // Added to prevent form submission on invalid input
    }
});
