/**
 * This is so that the side navbar shows 
 * and so that the navbar displays on the right side
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize side navigation menus
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);

    var elems2 = document.querySelectorAll('.sidenav-trigger');
    var instances2 = M.Sidenav.init(elems2);
});

 // Initialize side navigation triggers
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {
        edge: 'right' // Align mobile sidenav to the right
    });

// For mobile side navigation, align to the right edge of the screen
    var elems2 = document.querySelectorAll('.sidenav-trigger');
    var instances2 = M.Sidenav.init(elems2);
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var options = {
        accordion: false, // Set to true for accordion style
        onOpenStart: function() {
        }
    };
    var instances = M.Collapsible.init(elems, options);
});