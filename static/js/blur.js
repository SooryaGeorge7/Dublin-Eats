
const searchfield = document.getElementById('query');

const heroImage = document.querySelector('.hero-image');
  

searchfield.addEventListener('focus', function() {
    heroImage.classList.add('blury');
});
  

searchfield.addEventListener('focusout', function() {
    heroImage.classList.remove('blury');
});