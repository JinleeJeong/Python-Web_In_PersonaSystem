<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>반복문</title>
  <style>
  ul{
  list-style-type: circle;
  border:skyblue 2px solid;
  }
  </style>
</head>
<body>

  <h1>javascript</h1>
  <ul>
  <script>
    num = 1;
    while(num<=10){
    document.write("<li>9*"+num+"="+9*num+"</li><br />");
    num = num + 1;
    }
  </script>
  </ul>

  <h1>php</h1>

  <ul>
  <?php
  $num = 1;
  while ($num <= 10) {
  echo "<li> 9*".$num."=". 9*$num."<br /></li>";
  $num = $num + 1;
  }
  ?>

  </ul>
</body>
</html>
