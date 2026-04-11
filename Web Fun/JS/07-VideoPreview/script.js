const videos = document.querySelectorAll(".myVideo");

videos.forEach(function (video) {
  video.onmouseover = function () {
    video.style.cursor = "pointer";
    video.muted = true;
    video.play();
  };

  video.onmouseout = function () {
    video.pause();
  };
});
