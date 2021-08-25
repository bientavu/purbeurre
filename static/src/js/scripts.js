//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    // new SimpleLightbox({
    //     elements: '#portfolio a.portfolio-box'
    // });


    // Add or delete favorites

//     function favorites(attr) {
//
//     }
//
//     $('.favorites').on('click', function () {
//         favorites($(this).attr("id"));
//     });
//
// });

    // $(document).ready(function () {
    //     $("#{ product.id }").submit(function (event) {
    //         event.preventDefault();
    //         $.ajax({
    //             type: "POST",
    //             url: "/search_results/",
    //             data: {
    //                 'product_to_substitute': $('{ searched_product.id }'),
    //                 'substitute_product': $('{ product.id }')
    //                 // 'video': $('#').val() // from form
    //             },
    //             success: function () {
    //                 $('#add-to-favorites').html("<h2>C'est parti !</h2>")
    //             }
    //         });
    //         return false;
    //     });
    // });

    $("#add-to-favorites").on('click', function (event) {
            $.ajax({
                type: "POST",
                url: "/add_favorites/",
                data: {
                    'substitute_product': $(this).attr('class'),
                    'product_to_substitute': $("#searched_product > h2").attr('id')
                },
                success: function () {
                    $('#add-to-favorites').html("<h2>C'est parti !</h2>")
                }
            });
            return false;
        });

});
