<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <title>Login Tip Sender</title>

        <link rel="stylesheet" href="css/style.css">
  </head>

  <body>

    <form action="/login" method="post">
    <div align="center">

    </div>
      <div class="group">
        <input type="text" name="username" placeholder="Username" required><span class="highlight"></span><span class="bar"></span>

      </div>
      <div class="group">
        <input type="password" name="password" placeholder="Password" required><span class="highlight"></span><span class="bar"></span>

      </div>
    <button type="submit" class="button buttonBlue">Login
    <div class="ripples buttonRipples"><span class="ripplesCircle"></span></div>

  </button>
     <footer>
  <font color="red"> {{message}} </font>
  </footer>
</form>

  </body>
</html>
