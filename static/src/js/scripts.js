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


    // Add to favorites
    $(".add-to-favorites").on('click', function (event) {
            my_div =  $(this);
            $.ajax({
                type: "POST",
                url: "/add_favorites_test/",
                data: {
                    'substitute_product': $(this).parent().attr('class'),
                    'product_to_substitute': $("#searched_product > h2").attr('id')
                },
                success: function (is_deleted) {
                        if (is_deleted === "True") {
                            my_div.children("p").replaceWith('<p class="btn btn-outline-primary bi-star w-auto"> Ajouter aux favoris</p>')
                        } else {
                            my_div.children("p").replaceWith('<p class="btn btn-primary bi-star w-auto"> Supprimer des favoris</p>')
                        }
                }
                // success: function () {
                //     my_div.children("p").text(" C'est enregistré !")
                // }
            });
            return false;
        });

});
