$('#slider1, #slider2, #slider3, #slider4').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function () { 
    let id = $(this).attr('proid');
    let a = this.parentNode.children[2];
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/pluscart",
        data: {prodid:id},
        success: function (data) {
            a.innerText = data.quantity
            console.log(a)
        }
    });
});

$('.minus-cart').click(function () { 
    let id = $(this).attr('proid');
    let a = this.parentNode.children[2];
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/minuscart",
        data: {prodid:id},
        success: function (data) {
            a.innerText = data.quantity
        }
    });
});

$('.remove-cart').click(function () { 
    let id = $(this).attr('cartid');
    let elm = this
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/removecartitem",
        data: {cartid:id},
        success: function (data) {
            elm.parentNode.parentNode.parentNode.parentNode.remove()
            console.log(data.status)
        }
    });
});