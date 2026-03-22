const posts = document.querySelectorAll(".post");

posts.forEach((post) => {
  const likeBtn = post.querySelector("button");
  const likeCounter = post.querySelector(".likeCounter");

  likeBtn.addEventListener("click", () => {
    likeCounter.innerText++;
  });
});
