function getSecondsSinceStartOfDay() {
  return (
    new Date().getSeconds() +
    new Date().getMinutes() * 60 +
    new Date().getHours() * 3600
  );
}

setInterval(function () {
  var time = getSecondsSinceStartOfDay();

  var secondsDegrees = (time % 60) * 6;
  var minutesDegrees = ((time / 60) % 60) * 6;
  var hourDegrees = ((time / 3600) % 12) * 30;

  document.querySelector("#seconds").style.transform =`rotate(${secondsDegrees}deg)`;
  document.querySelector("#minutes").style.transform =`rotate(${minutesDegrees}deg)`;
  document.querySelector("#hour").style.transform = `rotate(${hourDegrees}deg)`;
}, 1000);
