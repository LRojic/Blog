const themeToggle = document.getElementById("theme-toggle");
const themeIcon = themeToggle.querySelector("i");
const savedTheme = localStorage.getItem("blog-theme");

if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
}

function updateThemeControl() {
    const isDarkMode = document.body.classList.contains("dark-mode");
    themeIcon.className = isDarkMode ? "fa-regular fa-sun" : "fa-solid fa-moon";
    themeToggle.setAttribute("aria-pressed", isDarkMode);
    themeToggle.setAttribute(
        "aria-label",
        isDarkMode ? "Activar modo claro" : "Activar modo oscuro"
    );
}

updateThemeControl();
themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    const isDarkMode = document.body.classList.contains("dark-mode");
    localStorage.setItem("blog-theme", isDarkMode ? "dark" : "light");
    updateThemeControl();
});
