$(function () {
  const MAX_PARAGRAPHS = 4;
  let counter = 0;

  let periodicCall = setInterval(function () {
    counter++;
    console.log(counter);
    if (counter <= MAX_PARAGRAPHS) {
      $("#description p:nth-of-type(" + counter + ")").toggleClass("reveal");
    }
    else {
      if (!$("a.waves-effect").hasClass("reveal")) {
        $("a.waves-effect").addClass("reveal");
      }
      clearInterval(periodicCall);
    }
  }, 2000);
});
