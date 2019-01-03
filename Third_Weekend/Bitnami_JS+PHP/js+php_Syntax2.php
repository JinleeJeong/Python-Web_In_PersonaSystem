<!DOCTYPE html>
<html>
<head>
     <meta charset="utf-8">
</head>
<body>
  <?php
    $password = $_GET["password"];
    $id = $_GET["id"];
    if($id == "Daniel" && $password == "1111"){
        echo "주인님 환영합니다";

    } else if($id == "Daniel" && $password != "1111"){
        echo "비밀번호를 확인하세요.?";
      }
        else if($id != "Daniel" && $password == "1111"){
            echo "아이디를 확인하세요.?";
          }
            else{
              echo "다시 확인해주세요.";
            }
   ?>
</body>
</html>
