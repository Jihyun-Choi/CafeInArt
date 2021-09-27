var fileInput1 = document.querySelector("#id_image1")
fileInput1.addEventListener('change', handleImage1);
var canvas1 = document.getElementById('imageCanvas1');
var ctx1 = canvas1.getContext('2d');

function handleImage1(e){
           var reader = new FileReader();
           reader.onload = function(event){
               var img = new Image();
               img.onload = function(){
                   canvas1.width = 300;
                   canvas1.height = 300;
                   ctx1.drawImage(img,0,0,300,300);
               };
               img.src = event.target.result;

           };
           reader.readAsDataURL(e.target.files[0]);
       }

var fileInput2 = document.querySelector("#id_image2")
fileInput2.addEventListener('change', handleImage2);
var canvas2 = document.getElementById('imageCanvas2');
var ctx2 = canvas2.getContext('2d');

function handleImage2(e){
           var reader = new FileReader();
           reader.onload = function(event){
               var img = new Image();
               img.onload = function(){
                   canvas2.width = 300;
                   canvas2.height = 300;
                   ctx2.drawImage(img,0,0,300,300);
               };
               img.src = event.target.result;

           };
           reader.readAsDataURL(e.target.files[0]);
       }

var fileInput3 = document.querySelector("#id_image3")
fileInput3.addEventListener('change', handleImage3);
var canvas3 = document.getElementById('imageCanvas3');
var ctx3 = canvas3.getContext('2d');
function handleImage3(e){
           var reader = new FileReader();
           reader.onload = function(event){
               var img = new Image();
               img.onload = function(){
                   canvas3.width = 300;
                   canvas3.height = 300;
                   ctx3.drawImage(img,0,0,300,300);
               };
               img.src = event.target.result;

           };
           reader.readAsDataURL(e.target.files[0]);
       }

var fileInput4 = document.querySelector("#id_image4")
fileInput4.addEventListener('change', handleImage4);
var canvas4 = document.getElementById('imageCanvas4');
var ctx4 = canvas4.getContext('2d');
function handleImage4(e){
           var reader = new FileReader();
           reader.onload = function(event){
               var img = new Image();
               img.onload = function(){
                   canvas4.width = 300;
                   canvas4.height = 300;
                   ctx4.drawImage(img,0,0,300,300);
               };
               img.src = event.target.result;

           };
           reader.readAsDataURL(e.target.files[0]);
       }