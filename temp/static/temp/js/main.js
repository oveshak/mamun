(function ($) {
  "use strict";

   // sticky
   var wind = $(window);
   var sticky = $('.stickybar');
   var body = $('body');
   wind.on('scroll', function () {
       var scroll = wind.scrollTop();
       if (scroll < 300) {
           sticky.removeClass('sticky-nav');
           body.removeClass('sticky-active');
       } else {
           sticky.addClass('sticky-nav');
           body.addClass('sticky-active');
       }
   });

   //click sticky-active-menu
    $('.sticky-active-menu').click(function(){
        $('.navbar-collapse').toggleClass('active-mobile-menu');
    });

    $('.sticky-active-menu').click(function(){
        $('.sticky-nav').toggleClass('active-menu');
        $('.menu-bars').toggleClass('active-bar');
    });
    $('#btn-headerCart').click(function(){
        $('#offcanvas').addClass('show');
    });
    $('.btn-closeOffcanvas').click(function(){
        $('#offcanvas').removeClass('show');
    });
    
    //Flexbox for Single page
    $(window).load(function() {
        $('.flexslider').flexslider({
            animation: "slide",
            controlNav: "thumbnails"
        });
    });
    // to top Script
     $(window).scroll(function(){
        if($(this).scrollTop() > 500){
            $('#to-top').fadeIn();
        } else{
            $('#to-top').fadeOut();
        }
    });
    $("#to-top").click(function(){
        $('html , body').animate({scrollTop :0},100);
    });

    

    // BannerCarousel Active
    $('.BannerCarousel').owlCarousel({
    loop: true,
    autoplay: true,
    autoplayTimeout: 5000,
    dots: true,
    dotsEach: false,
    lazyLoad:true,
    smartSpeed: 1000,
    autoplayHoverPause:true, 
    nav:true,
    margin: 100,
    navText: ["<i class='fas fa-angle-left'></i>", "<i class='fas fa-angle-right'></i>"],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 1
        },
        992: {
            items: 1
        },
        1000: {
            items: 1
        },
        1199: {
            items: 1
        },
        1920: {
            items: 1
        }
    }
    });

    // ProductGrid StyleOne  Active
    $('.ProductCarousel_One').owlCarousel({
        loop: true,
        autoplay: true,
        autoplayTimeout: 5000,
        dots: true,
        dotsEach: false,
        lazyLoad:true,
        smartSpeed: 500,
        nav:true,
        autoplayHoverPause:true, 
        margin: 0,
        navText: ["<i class='fas fa-angle-left'></i>", "<i class='fas fa-angle-right'></i>"],
        responsive: {
            0: {
                items: 1,
                slideBy: 1
            },
            576: {
                items: 2,
                slideBy: 2
            },
            768: {
                items: 3,
                slideBy: 3
            },
            992: {
                items: 4,
                slideBy: 4
            },
            1000: {
                items: 4,
                slideBy: 4
            },
            1199: {
                items: 4,
                slideBy: 4
            },
            1367: {
                items: 5,
                slideBy: 5
            }
        }
    });



    // ProductGrid StyleTwo  Active
    $('.ProductCarousel_Two').owlCarousel({
        loop: true,
        autoplay: true,
        autoplayTimeout: 4500,
        dots: true,
        dotsEach: false,
        lazyLoad:true,
        smartSpeed: 500,
        nav:true,
        center: true,
        autoplayHoverPause:true, 
        margin: 0,
        navText: ["<i class='fas fa-angle-left'></i>", "<i class='fas fa-angle-right'></i>"],
        responsive: {
            0: {
                items: 1,
                slideBy: 1
            },
            576: {
                items: 2,
                center: false,
                slideBy: 2
            },
            768: {
                items: 2,
                center: false,
                slideBy: 2
            },
            992: {
                items: 3,
                slideBy: 3
            },
            1000: {
                items: 3,
                slideBy: 3
            },
            1199: {
                items: 3,
                slideBy: 3
            },
            1367: {
                items: 4,
                slideBy: 4
            }
        }
    });

    // Price range Script Start
    var leftValue=document.querySelector(".left-value");
    var rightValue=document.querySelector(".right-value");
    var inputLeft = document.getElementById("input-left");
    var inputRight = document.getElementById("input-right");
    var thumbLeft = document.querySelector(".slider > .thumb.left");
    var thumbRight = document.querySelector(".slider > .thumb.right");
    var range = document.querySelector(".slider > .range");

    function setLeftValue(e) {
        var _this = inputLeft,
            min = parseInt(_this.min),
            max = parseInt(_this.max);

        _this.value = Math.min(parseInt(_this.value), parseInt(inputRight.value) - 1);

        var percent = ((_this.value - min) / (max - min)) * 100;

        thumbLeft.style.left = percent + "%";
        range.style.left = percent + "%";
        leftValue.style.left=percent + "%";
        leftValue.innerHTML=inputLeft.value;

    }
    setLeftValue();

    function setRightValue() {
        var _this = inputRight,
            min = parseInt(_this.min),
            max = parseInt(_this.max);

        _this.value = Math.max(parseInt(_this.value), parseInt(inputLeft.value) + 1);

        var percent = ((_this.value - min) / (max - min)) * 100;
        
        thumbRight.style.right = (100 - percent) + "%";
        range.style.right = (100 - percent) + "%";
        rightValue.style.right=(100-percent) + "%";
        rightValue.innerHTML=inputRight.value;
    }
    setRightValue();

    inputLeft.addEventListener("input", setLeftValue);
    inputRight.addEventListener("input", setRightValue);

    inputLeft.addEventListener("mousemove", function(e){
        leftValue.innerHTML=e.target.value;
    })
    inputRight.addEventListener("mousemove", function(e){
        rightValue.innerHTML=e.target.value;
    })


    inputLeft.addEventListener("mouseover", function(e) {
        thumbLeft.classList.add("hover");
        leftValue.innerHTML=e.target.value;
    });
    inputLeft.addEventListener("mouseout", function() {
        thumbLeft.classList.remove("hover");
    });
    inputLeft.addEventListener("mousedown", function() {
        thumbLeft.classList.add("active");
    });
    inputLeft.addEventListener("mouseup", function() {
        thumbLeft.classList.remove("active");
    });

    inputRight.addEventListener("mouseover", function() {
        thumbRight.classList.add("hover");
    });
    inputRight.addEventListener("mouseout", function() {
        thumbRight.classList.remove("hover");
    });
    inputRight.addEventListener("mousedown", function() {
        thumbRight.classList.add("active");
    });
    inputRight.addEventListener("mouseup", function() {
        thumbRight.classList.remove("active");
    });
    // Price range Script End

})(jQuery);


// Toggle Filter 
function filterToggler(){
    $("#filterWidget_wrap").addClass("active");
}
// Hide filter 
function filterHide(){
    $("#filterWidget_wrap").removeClass("active");
}
// Show Menu for Mobile devide 
function activeMenu(){
    $("#mainMenu").toggleClass("Show-menu");
    $(".menu-item").removeClass("expaned");
    $("body").toggleClass("overlay");
}
// Toggle Submenu for modile device 
function toggleSubmenu(e){
    $(".menu-item").removeClass("expaned");
    $(e).toggleClass("expaned");
}


