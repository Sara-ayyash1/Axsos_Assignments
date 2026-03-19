function logOut(elem) {
  if(elem.innerText === "Login"){
   elem.innerText = "Logout";
  }
  else
  elem.innerText = "Login";
}

function removeBtn(elem) {
  elem.style.visibility="hidden";
}

function likedAlert(){
    alert("Ninja was liked");
}