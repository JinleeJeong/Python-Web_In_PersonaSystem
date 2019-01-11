var right_id = "testing"
var right_pwd = "1111"

function login(id, pwd) {
    if(id == right_id){
        if(pwd == right_pwd)
        {
            document.write(id + "님 환영합니다.");
        }
        else {
            alert("비밀번호 확인해주세요.");
        }
    }
    else{
        alert("아이디 확인.");
    }
}

var userId = prompt("아이디 :");
var userpwd = prompt("비번 : ");

login(userId,userpwd);


