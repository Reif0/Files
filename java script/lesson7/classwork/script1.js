let user = {
    name: prompt('enter name:'),
    surName: prompt('enter surname:'),
    id: prompt('enter id')
}

let nameChange = confirm('do you want chage name?')
if (nameChange === true){
    console.log(user.name = prompt('new name'))
}

console.log(user)