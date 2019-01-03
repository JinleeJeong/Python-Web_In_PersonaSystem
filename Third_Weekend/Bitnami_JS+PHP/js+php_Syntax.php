<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <!-- <script>
    name = "Daniel";
    document.write("10"+"10"+ '<br>');
    document.write(name + "안녕하세요. "+ '<br>');
    document.write(2==1 + '<br>');

    list = new Array("one", "two", "three");
    document.write(list[2]);
    document.write(list.length);
    </script>
    <?php
      echo "Hello World";
      echo "10"."10";
      $name = "Daniel";
      echo "안녕하세요.".$name;
      var_dump(2==1);
      $list = array("one", "two", "three");
      echo $list[2];
      echo count($list);
     ?> -->
     <form action="Project/login.php">
       <p>아이디와 비밀번호를 입력해주세요.</p>
       <input type="text" name="id" placeholder="아이디" id="user_input"><br>
       <input type="text" name="password" placeholder="비밀번호"><br>
       <input type="submit" onclick="alert(document.getElementById('user_input').value)"/>
</html>

<!-- php 숫자 "" + "" 는 덧셈 연산 So, 문자를 원하면 .을 해야한다. >> 곱하기 예제
또한 비교할 때에는 일반적으로 php에서는 var_dump를 이용한다.
Java Script
password = prompt("비밀번호"); > 창을 띄우는 script 언어
alert('') > 경고창 && prompt > 입력창
onclick, onfocus, onblur
onclick="document.getElementById('target').className='em'"

target Id인 것을 클래스 이름을 붙인다.
