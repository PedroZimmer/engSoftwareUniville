function infinity(){
    let i = 0;
    while(i < 50000) {
        console.log(i++);
    }
}

function date() {
    console.log(new Date());
}

infinity();
date();