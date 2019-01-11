var price1 = 1200;
var price2 = 1300;
var price3 = 1000;
var price4 = prompt("4분기 판매량 : ")
var logic =confirm("message");

var result = (price1 + price2 + price3) / 3 


if(logic == true){
    var a = price4 > result ? price4 - result + "원 추가 이익입니다 ^_^" : "손해입니다!!";
    document.write(a);
    alert("승진");
} else {
    document.write("NO")
}


