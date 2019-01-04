<?php
  $conn = mysqli_connect("localhost", "root", "cwsok045");
  mysqli_select_db($conn, 'opentutorials');

  $sql = "INSERT INTO topic (title, author, description, created) VALUES('".$_POST['title']."','".$_POST['author']."','".$_POST['description']."',now())";
  $result = mysqli_query($conn, $sql);
  header('location: index_file(txt).php');
?>
