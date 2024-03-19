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




// Dropdown code
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
  });
// comment drop up
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});

searchInput.addEventListner("input", e => {
    const value = e.target.value.toLoweCase()
    users.forEach(user => {
        const isVisible =
            user.name.toLoweCase().includes(value)
        user.element.classList.toggle("hide", !isVisible)
    })
})


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
  