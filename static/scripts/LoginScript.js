const submit = document.querySelector(".submit");
const passInput = document.querySelector(".passInput");
const userNameInput = document.querySelector(".userNameInput");
const passMessageP = document.querySelector(".passMessageP");

// function for checking if it is English or not
function isEnglish(input) {
  for (let i = 0; i < input.length; i++) {
    const charCode = input.charCodeAt(i);
    // Check if the character is within the ASCII range of English letters or numbers
    if ((charCode < 65 || charCode > 90) && (charCode < 97 || charCode > 122) && (charCode < 48 || charCode > 57)) {
      return false; // Not an English character or number
    }
  }
  return true;
}

// getting the button from the DOM
submit.addEventListener("click", (e) => {
  ValidationInputs();
});

// function for validating inputs before submiting the form
function ValidationInputs() {
  let Istrue = true;
  // checking if the value's don't be empty
  if (passInput.value == "" || userNameInput.value == "") {
    Istrue = false;
    passMessageP.textContent = "لطفا اطلاعات را کامل وارد کنید";
  }

  // checking the Length of the password to be 8 characters
  else if (passInput.value.length < 8) {
    Istrue = false;
    passMessageP.textContent = "رمز باید بیش از 8 کاراکتر باشد";
  }

  // checking if the input that we get is English or not 
  else if (!isEnglish(userNameInput.value)) {
    Istrue = false;
    passMessageP.textContent = "تمام کارکتر های نام کابری باید به صورت لاتین باشد";
  }

  // checking if the isTrue = true submit the form
  if (Istrue) {
    passInput.value = passInput.value.trim();
    userNameInput.value = userNameInput.value.trim();
    document.querySelector('form').submit();
  }
}