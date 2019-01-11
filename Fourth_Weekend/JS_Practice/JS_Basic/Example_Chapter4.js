/* var arr_1 = ['진리', '소영', '몽이'];
var arr_2 = ['상규', '유진', '강릉'];

arr_1.splice(2, 1, "a", "b");
console.log(arr_1);

var data1 = arr_2.pop();
var data2 = arr_2.shift();

arr_2.push(data2);
console.log(arr_2);

var UserName = prompt("영문 이름 : ");
var UserNum = prompt("번호 : ");

var result = UserName + UserNum.substring(0, UserNum.length-4) + "****";
document.write(result); */

var addNum = 0;
var subNum = 1000;

var auto_1 = setInterval(function() {
    addNum++; 
    console.log("addNum: " + addNum);
}, 3000);

var auto_2 = setInterval(function() {
    subNum--;
    console.log("subNum: " + subNum);
}, 3000);
