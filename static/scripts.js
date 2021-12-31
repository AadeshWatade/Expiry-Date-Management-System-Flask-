// function myFunction() {
//     var x = document.getElementById("myInput");
//     if (x.type === "password") {
//       x.type = "text";
//     } else {
//       x.type = "password";
//     }
//   }

const password = document.querySelector('#pass');
const btnToggle = document.querySelector('#toggle');
const eye = document.querySelector('#eye');
btnToggle.addEventListener('click', (event) => {
    password.type = password.type == 'password' ? 'text' : 'password';
    eye.className = eye.className == 'fas fa-eye' ? 'fa fa-eye-slash' : 'fas fa-eye';
});