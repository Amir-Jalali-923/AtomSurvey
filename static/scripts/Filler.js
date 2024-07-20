let Footer = `
    <div class="footerTop">
                    <div class="footerSec">
                        <h3>هدف ما از طراحی این سایت چیست؟</h3>
                        <p>
                            با شرکت در نظرسنجی، صدای خود را برای ما بشنوانید و تغییراتی که دوست دارید را مشخص کنید. همراه ما
                            باشید و بهترین راه‌حل‌ها را با هم پیدا کنیم!
                        </p>
                    </div>
                    <div class="footerSec">
                        <h3>دسترسی سریع</h3>
                        <ul>
                            <li><a href="">شرکت در نظرسنجی</a></li>
                            <li><a href="">درباره ی ما</a></li>
                            <li><a href="">تماس با</a></li>
                        </ul>
                    </div>
                    <div class="footerSec">
                        <h3>تماس با ما</h3>
                        <p>آدرس : تبریز / قطران به طرف ابوریحان هنرستان مصطفی خمینی</p>
                        <p>شماره تماس:4567 123 43+</p>
                    </div>
                </div>
`;

export function FooterFiller() {
    let footerOnPage = document.querySelector('footer');
    footerOnPage.innerHTML = Footer;
    console.log("Footer inserted Successfully");
}
