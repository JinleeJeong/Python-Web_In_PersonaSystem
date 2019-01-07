<?php
    $conn = mysqli_connect("localhost", "root", "cwsok045");
    mysqli_select_db($conn, 'opentutorials');
    $result = mysqli_query($conn, "SELECT * FROM topic");

?>

<!DOCTYPE html>
<html>
<head>
     <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="http://localhost/Project/PHP_2/file_Processing/style.css">
</head>
<body id="target">
    <header>
    <img src="https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/course/94.png" alt="생활코딩">
        <h1><a href="http://localhost/Project/PHP_2/file_Processing/index_file(txt).php">JavaScript</a></h1>
  </header>
    <nav>
        <ol>
    <?php
      while($row = mysqli_fetch_assoc($result)){
      echo '<li><a href="index_file(txt).php?id='.$row['id'].'">'.$row['title'].'</a></li>'."\n";
      }
    ?>
        </ol>
    </nav>
    <div id="control">
      <a href="write.php">쓰기</a> <!-- Ajax 구현  -->

    </div>


  <article>
    <form action="process.php" method="post">
      <p>
        제목 : <input type="text" name="title">
      </p>
      <p>
        작성자 : <input type="text" name="author">
      </p>
      <p>
        본문 : <textarea name="description"></textarea>
      </p>
      <p>
        <input type="submit" name="name">
      </p>
    </form>
  </article>
</body>
</html>
