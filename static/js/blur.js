// function onFocus() {
//     document.querySelector('.hero-image').classList.add('blury');
//   }
  
// function onFocusOut() {
//     document.querySelector('.hero-image').classList.remove('blury');
//   }

const searchfield = document.getElementById('query');

const heroImage = document.querySelector('.hero-image');
  

searchfield.addEventListener('focus', function() {
    heroImage.classList.add('blury');
});
  

searchfield.addEventListener('focusout', function() {
    heroImage.classList.remove('blury');
});