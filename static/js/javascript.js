
function changeColor(){
    colors = ['red', 'blue', 'green', 'yellow', 'black']
    x = Math.floor(Math.random() * 5) + 1
    button = document.getElementById('button')
    button.style.backgroundColor = colors[x];
   }  
