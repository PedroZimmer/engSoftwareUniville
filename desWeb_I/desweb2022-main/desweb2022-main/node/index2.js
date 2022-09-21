function infinity() {
    let i = 0;
    setInterval(function(){
        console.log(i++);
    }, 1);
}
function date(){
    console.log(new Date());
}
infinity();
date();