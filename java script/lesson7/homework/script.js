const result = document.getElementById("result")
function login() {
    let user = {
    name : prompt("enter your name"),
    surName : prompt('enter your surname')
    }
    result.innerHTML = 'hello' +" "+ user.name +" "+ user.surName +" "+ 'welcome to goa'
}



