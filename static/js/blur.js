//This js file handles the background when user clicks on search field.
//Learnt to apply blurry background here https://www.w3schools.com/howto/howto_css_blurred_background.asp

const searchfield = document.getElementById('query');
const heroImage = document.querySelector('.hero-image');
  

searchfield.addEventListener('focus', function() {
    heroImage.classList.add('blury');
});
  

searchfield.addEventListener('focusout', function() {
    heroImage.classList.remove('blury');
});