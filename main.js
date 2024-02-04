// index.js
const searchInput = document.getElementById('searchInput');

searchInput.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
    const query = searchInput.value;
    // Redirect to the search-results.html page with the search query as a parameter
    window.location.href = `results.html?q=${query}`;
}});
