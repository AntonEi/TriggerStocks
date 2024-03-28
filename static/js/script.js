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

    // Initialize side navigation triggers
    var elems3 = document.querySelectorAll('.sidenav');
    var instances3 = M.Sidenav.init(elems3, {
        edge: 'right' // Align mobile sidenav to the right
    });

    // For mobile side navigation, align to the right edge of the screen
    var elems4 = document.querySelectorAll('.sidenav-trigger');
    var instances4 = M.Sidenav.init(elems4);

    var elems5 = document.querySelectorAll('.collapsible');
    var options = {
        accordion: false, // Set to true for accordion style
        onOpenStart: function() {}
    };
    var instances5 = M.Collapsible.init(elems5, options);

    var elems6 = document.querySelectorAll('select');
    var instances6 = M.FormSelect.init(elems6);

    var elems7 = document.querySelectorAll('.modal');
    var instances7 = M.Modal.init(elems7);

    var searchInput = document.querySelector('#search');
    var users = Array.from(document.querySelectorAll('.user'));
    searchInput.addEventListener("input", function(e) {
        var value = e.target.value.toLowerCase();
        users.forEach(function(user) {
            var isVisible = user.textContent.toLowerCase().includes(value);
            user.classList.toggle("hide", !isVisible);
        });
    });

    // jQuery Code
    $(document).ready(function() {
        // Function to handle trigger list filtering based on selected year and quarter
        $('#year-select, #quarter-select').change(function() {
            var selectedYear = $('#year-select').val();
            var selectedQuarter = $('#quarter-select').val();

            // Perform filtering based on selected year and quarter
            // Example: You can hide/show trigger list items based on the selected options
            // Here, we're just logging the selected options for demonstration purposes
            console.log('Selected Year:', selectedYear);
            console.log('Selected Quarter:', selectedQuarter);
        });

        // Function to handle form submission for search
        $('#searchForm').submit(function(event) {
            event.preventDefault();
            var searchTerm = $('#search').val();

            // Perform search logic here
            // Example: You can make an AJAX request to fetch search results and display them on the page
            // Here, we're just logging the search term for demonstration purposes
            console.log('Search Term:', searchTerm);
        });
    });
});
