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
        <h1><a href="index.php">Practice</a></h1>
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
            <?php
            if(empty($_GET['id'])){
              echo "Welcome";
            } else {
              $id = mysqli_real_escape_string($conn, $_GET['id']);
              $sql = "SELECT topic.id, title, user.name, description, created FROM topic LEFT JOIN user ON topic.author = user.id WHERE topic.id=".$id;
              $result = mysqli_query($conn, $sql);
              $row = mysqli_fetch_assoc($result);
              ?>
              <h2><?= htmlspecialchars($row['title'])?></h2>
              <div><?= htmlspecialchars($row['name'])?> | <?= htmlspecialchars($row['created'])?></div>
              <div><?= htmlspecialchars($row['description'])?></div><?php
            }

              ?>

              <input type="button" name="name" value="White" onclick="document.getElementById('body').className='white'">
              <input type="button" name="name" value="Black" onclick="document.getElementById('body').className='black'">
              <a href="write.php">입력</a>
          </article>


      </div>
  </body>
</html>
