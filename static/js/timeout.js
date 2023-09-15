//This code was found from code institute walkthrough video, it allows popup message to appear for few seconds.

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);