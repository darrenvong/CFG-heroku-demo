$(function () {
  const NUM_TEXT_TO_REVEAL = 3;
  let num_revealed = 0;

  let periodicCall = setInterval(() => {
    if (num_revealed < NUM_TEXT_TO_REVEAL) {
      $(".init-hidden")[num_revealed].classList.add("reveal");
      num_revealed++;
    }
    else {
      // Additional delay for the dramatic gif reveal
      setTimeout(() => {
        $("#triggered").addClass("reveal");

        // Give the user some time to see the funny screen before fading out...
        setTimeout(() => {
          $(".pre-loader").css("opacity", "0");
          $(".container").toggleClass("reveal");
        }, 3000);
      }, 500);
      clearInterval(periodicCall);
    }
  }, 1000);

});
