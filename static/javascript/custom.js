//when the user scroll the page ,execute myFunction
window.onscroll = function(){
    myFunction()
};
//get the navbar
var navbar = document.getElementById("navbar");
//get the offset position of the navbar
var sticky = navbar.offsetTop;

function myFunction(){
    if(window.pageYOffset >= sticky){
        navbar.classList.add("sticky")
    }
    else{
        navbar.classList.remove("sticky");
    }
}