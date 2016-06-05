<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <title>Tip Sender</title>

        <link rel="stylesheet" href="css/style.css">
  </head>

  <body>

    <form action="" method="post">
    <div align="center">
    <img src="images/head.png" width="300">
    </div>

       <div class="group">
        <input type="text" name="nome" placeholder="Nome da partida na Betfair"><span class="highlight"></span><span class="bar"></span>

      </div>
       <div class="group">
        <input type="text" name="tip" placeholder="Dica de gols para partida"><span class="highlight"></span><span class="bar"></span>
       </div>
    <button type="submit" class="button buttonBlue">Enviar
    <div class="ripples buttonRipples"><span class="ripplesCircle"></span></div>

  </button>

</form>
  <footer>
  <h1> {{message}} </h1>
  </footer>

  </body>
</html>
