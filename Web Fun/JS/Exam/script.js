let startBtn = document.querySelector(".start-btn");

startBtn.addEventListener("mouseover", () => {
  startBtn.style.backgroundColor = "#3b4598";
});
startBtn.addEventListener("mouseout", () => {
  startBtn.style.backgroundColor = "#284bf9";
});
///////////////////////////

let changeBtn = document.querySelector(".change-btn");

changeBtn.addEventListener("click", () => {
  let aboutContentHead = document.querySelector(".about-content h3");
  let aboutImg = document.querySelector(".about-img img");
  let aboutDesc = document.querySelector(".about-content p");

  if (changeBtn.innerText === "Make A Change") {
    aboutContentHead.innerText = "What we do";
    aboutImg.src = "images/alt-features.png";
    changeBtn.innerText = "Change Back";
    aboutDesc.innerText = `Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit aspernatur libero suscipit excepturi maiores ducimus, impedit magnam odio aut harum.  Porro dicta tempora, iste sunt asperiores totam eligendi temporibus tempore?`;
  } else {
    aboutContentHead.innerText = "What we are";
    aboutImg.src = "images/about.jpg";
    changeBtn.innerText = "Make A Change";
    aboutDesc.innerText = ` We are a forward-thinking company dedicated to providing innovative
            solutions that fuel business growth. With a foucs on modern
            technologies and strategic insights, we help businesses streamline
            their operations,enhance customer experiences, and scale
            efficiently. Whether you're looking to improve your digital presence
            optimize processes,or drive new revenue streams`;
  }
});

///////////////////////////
let addBtn = document.querySelector(".add-btn");
let servicesCards = document.querySelector(".services-cards");

addBtn.addEventListener("click", () => {
  let childCard = document.createElement("div");
  childCard.className = "card flex col align-center";

  childCard.innerHTML = ` <img src="images/features.png" alt="values-3 img" />
            <p>
             Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit aspernatur libero suscipit
              excepturi maiores ducimus, impedit magnam odio aut harum.
              Porro dicta tempora, iste sunt asperiores totam eligendi temporibus tempore?
            </p>`;
  servicesCards.appendChild(childCard);
});

/////////////////////////////
let header = document.querySelector("header");

window.addEventListener("scroll", () => {
  if(window.scrollY >80){
  header.style.position = "sticky";
  header.style.top = "0px";
  header.style.backgroundColor = "white";
  header.style.borderBottom = "2px solid #4e4e4f";
  }

});
