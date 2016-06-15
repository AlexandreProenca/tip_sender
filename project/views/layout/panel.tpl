<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <title>Tip Sender</title>

        <link rel="stylesheet" href="css/style.css">
  </head>

  <body>

    <form action="" method="post" class="panel">
    <div align="center">
    <img src="images/head.png" width="300">
    </div>
    </br>
    </br>

       <div class="group">
        <input type="text" name="title" placeholder="Nome da partida na Betfair" required><span class="highlight"></span><span class="bar"></span>

      </div>
       <div class="group">
        <input type="text" name="tip" placeholder="Sugestão de aposta" required><span class="highlight"></span><span class="bar"></span>
       </div>
    <button type="submit" class="button buttonBlue">Enviar
    <div class="ripples buttonRipples"><span class="ripplesCircle"></span></div>

  </button>
     <h1> {{message}} </h1>
</form>

  </body>
</html>
