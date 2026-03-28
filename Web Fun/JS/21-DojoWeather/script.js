let cityLinks = document.querySelectorAll(".city-links li a");
let acceptBtn = document.querySelector(".accept-btn");
let cookiesMsg = document.querySelector(".cookies-banner");
let selectTemp = document.querySelector(".select-temp");

cityLinks.forEach((city) => {
  city.addEventListener("click", () => {
    alert("Loading weather report...");
  });
});

acceptBtn.addEventListener("click", function () {
  cookiesMsg.remove();
});

selectTemp.addEventListener("change", function () {
  let highTemps = document.querySelectorAll(".high-temp");
  let lowTemps = document.querySelectorAll(".low-temp");
  let allTemps = [...highTemps, ...lowTemps];

  allTemps.forEach((t) => {
    let currentTempValue = parseInt(t.innerText);

    if (selectTemp.value === "Fahrenheit") {
      t.innerHTML = Math.round((currentTempValue * 9) / 5 + 32) + "&#176;";
    } else {
      t.innerHTML = Math.round(((currentTempValue - 32) * 5) / 9) + "&#176;";
    }
  });
});