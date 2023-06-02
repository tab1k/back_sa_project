window.onscroll = function () {
  myFunction()
};

function myFunction() {
  if (document.documentElement.scrollTop > 10 && window.innerWidth > 425) {
    document.getElementById("header").className = "onscroll";
  } else {
    document.getElementById("header").className = "";
  }
}

function return_top() {
  scroll(0, $('header').position().top)
}

function tap(element) {
  $(".fa-heart-o").toggleClass("tap");
  // element.toggleClass("tap");
}

let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
  setTimeout(showSlides, 1500); // Change image every 2 seconds
}

function open_close() {
  $(".burger-links").toggleClass("top");
  $("body").toggleClass("scroll");
  // element.toggleClass("tap");
}
