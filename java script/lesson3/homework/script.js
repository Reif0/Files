let messyArr = [88, 1, 34, 5, 71, 55, 99, 14434, 99000, 3425];
let newArr = [];

for (let i = 0; i < messyArr.length - 1; i++) {
    for (let j = i + 1; j < messyArr.length; j++) {
        if (messyArr[i] > messyArr[j]) {
            let variable = messyArr[i];
            messyArr[i] = messyArr[j];
            messyArr[j] = variable;
        }
    }
}

newArr = messyArr;
console.log(newArr);