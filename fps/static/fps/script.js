document.addEventListener('DOMContentLoaded', function() {
    const aboutLink = document.querySelector('a[href="/about/"]');
    aboutLink.addEventListener('click', function(e) {
        e.preventDefault();
        document.getElementById('about').scrollIntoView({ behavior: 'smooth' });
    });
});



