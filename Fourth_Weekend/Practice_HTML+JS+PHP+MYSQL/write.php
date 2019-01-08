<?php
require("./config.php");
require("./db.php");
$conn = db_init($config["host"], $config["duser"], $config["dpw"], $config["dname"]);
?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <link rel="stylesheet" type="text/css" href="./practice.css">
    <meta charset="utf-8">
    <title></title>
  </head>
  <body id ="body">
      <header>
        <h1>Practice</h1>
      </header>
      <nav>
        <ol>
        <?php
        $sql = "SELECT * FROM `topic`";
        $result = mysqli_query($conn, $sql);

        while($row = mysqli_fetch_assoc($result)){
          echo '<li><a href="index.php?id='.$row['id'].'">'.htmlspecialchars($row['title']).'</a></li>'."\n";
        }
         ?>
       </ol>
      </nav>
      <div id="content">
          <article>
            <form class="" action="process.php" method="post">
              <p>
              <label for ="title">제목 :</label>
              <input id = "title" type="text" name="title">
              </p>
              <p>
              <label for ="author">글쓴이 :</label>
              <input id = "author" type="text" name="author">
              </p>
              <p>
              <label for ="description">내용 :</label>
              <textarea id = "description" name="description" rows="8" cols="50"></textarea>
              </p>
              <p>
                <input type="submit" value="전송">
              </p>
            </form>
          </article>

          <input type="button" name="name" value="White" onclick="document.getElementById('body').className='white'">
          <input type="button" name="name" value="Black" onclick="document.getElementById('body').className='black'">
      </div>
  </body>
</html>
