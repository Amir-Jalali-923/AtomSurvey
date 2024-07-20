export function asideActivator() {
    // Activating Dropdown
    const dropButton = document.querySelector('.hamburgerMenu');
    const dropdown = document.querySelector('.HeaderDropDown');
    const exitButton = document.querySelector('.exit'); // Cache the exit button

    dropButton.addEventListener('click', () => {
        dropdown.style.display = "flex";
        // No need for setTimeout here, directly apply styles
        document.body.style.overflow = "hidden";
        dropdown.style.width = `${window.innerWidth}px`; // Use template literals for clarity
        dropdown.style.transform = "translateX(0)";
        dropdown.style.opacity = "1";
    });

    // Deactivating Dropdown
    exitButton.addEventListener('click', () => {
        dropdown.style.transform = "translateX(100%)";
        document.body.style.overflow = "auto";
        // No need for setTimeout here either
        dropdown.style.opacity = "0";
        dropdown.style.display = "none";
    });
}
