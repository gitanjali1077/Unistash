

function hide( evt , course){
  var tab= document.getElementsByClassName("tab");
        tab[0].style.display = "none";
 
var course= document.getElementById(course);
    course.style.display="block";
  

}

var i=0;
function sidebar(){

var m=document.getElementsByClassName("menuDisplayed");
if(i%2==0)
 {
m[0].style.display="block";
this.i=1;
}
else
{
m[0].style.display="none";
i=0;
}

}
$(window).resize(bod);


function bod(){
 
var mq=window.matchMedia(" (min-width: 650px)");
if(mq>650){
  m=document.getElementsByClassName("menuDisplayed");
   
m[0].style.display="block";
i=0;
return;
}

 
}


function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}


function sem(evt ,sem,branch){
semes = document.getElementsByClassName(branch);
  for (i = 0; i < semes.length; i++) {
        semes[i].style.display = "none";
    } 
 document.getElementById(sem).style.display = "block";

}
