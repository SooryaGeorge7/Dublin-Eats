//This js file handles the star ratings.
//Used this document as a guide to implement star ratings in my website. https://www.codingnepalweb.com/star-rating-html-css-javascript-2/

//Import the review form 
var form = document.querySelector('.reviewform');

//Define function handle ratings for specific criterias using eventhandler
var handleRatings = (choice, criteria) => {
    var stars = document.querySelectorAll(`.${criteria} .btn i`);

    stars.forEach(star => star.classList.remove('checked'));
    
    //Determine the user's choice and add the 'checked' class so the selected stars change color
    var i;
    switch (choice) {
        case `${criteria}-first`:
            for ( i = 0; i < 1; i++) {
                stars[i].classList.add('checked');
            }
            break;
        case `${criteria}-second`:
            for ( i = 0; i < 2; i++) {
                stars[i].classList.add('checked');
            }
            break;
        case `${criteria}-third`:
            for ( i = 0; i < 3; i++) {
                stars[i].classList.add('checked');
            }
            break;
        case `${criteria}-fourth`:
            for ( i = 0; i < 4; i++) {
                stars[i].classList.add('checked');
            }
            break;
        case `${criteria}-fifth`:
            for ( i = 0; i < 5; i++) {
                stars[i].classList.add('checked');
            }
            break;
    }
    //Get the numeric value from getNumValue and update the corresponding form field/criteria values
    var val_num = getNumValue(choice);
    form[criteria].value = val_num;

};

//Function to determine value of checked stars
var getNumValue = (stringValue) => {
    let numValue;
    if (stringValue.endsWith('-first')) {
        numValue = 1;
    } else if (stringValue.endsWith('-second')) {
        numValue = 2;
    } else if (stringValue.endsWith('-third')) {
        numValue = 3;
    } else if (stringValue.endsWith('-fourth')) {
        numValue = 4;
    } else if (stringValue.endsWith('-fifth')) {
        numValue = 5;
    } else {
        numValue = 0;
    }
    return numValue;
};

//Array with the criterias from the review form.
var criterias = ['taste', 'ambience', 'customer_service', 'location', 'value_for_money'];

//Eventhandler to handle star rating when user clicks on star
criterias.forEach(criteria => {
    var stars = document.querySelectorAll(`.${criteria} .btn i`);

    stars.forEach(star => {
        star.addEventListener('click', (event) => {
            handleRatings(event.target.id, criteria);
            
        });
    });
});


//Function to update the star color and field values when user wants to edit review form
var updateStarRatings = (criteria) => {
    var stars = document.querySelectorAll(`.${criteria} .btn i`);
    var value = form[criteria].value;
  
    stars.forEach((star, index) => {
      if (index < value) {
        star.classList.add('checked');
      } else {
        star.classList.remove('checked');
      }
    });
  };
  
  
  criterias.forEach(criteria => {
    updateStarRatings(criteria);
  });



