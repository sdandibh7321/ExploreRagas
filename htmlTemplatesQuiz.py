from string import Template

HTML_TEMPLATE_Q = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Raga Quiz</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
      <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
      <style>
      body {
        font: 20px Montserrat, sans-serif;
        line-height: 1.8;
        color: #f5f6f7;
      }
      p {
        font-size: 16px;
      }
      .margin {
        margin-bottom: 20px;
      }
      .bg-1 {
        background-color: #2a6655;
        color: #ffffff;
      }
      .bg-2 {
        background-color: #474e5d; /* Dark Blue */
        color: #ffffff;
      }
      .bg-3 {
        background-color: #ffffff; /* White */
        color: #555555;
      }
      .bg-4 {
        background-color: #2f2f2f; /* Black Gray */
        color: #fff;
      }
      .container-fluid {
        padding-top: 40px;
        padding-bottom: 70px;
        overflow: hidden;
        max-width: 100%;
        max-height: 100%

      }

      #submit {
        width: 6em;
        height: 3em;
        font-size: 12px;
      }

      .navbar {
        padding-top: 15px;
        padding-bottom: 15px;
        border: 0;
        border-radius: 0;
        margin-bottom: 0;
        font-size: 12px;
        letter-spacing: 5px;
      }
      .navbar-nav  li a:hover {
        color: #1abc9c !important;
      }

      label {
        font-size:12px;
        display:block;
      }

      .card {
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        border-radius: 5px;
        background-color: #ffffff; /* White */
        color: #555555;
        max-width: 70%;
        overflow: hidden;
        height: 250px;
        padding-bottom: 1%;
        margin: auto;
      }

      </style>
    </head>
    <body>

    <!-- Navbar -->
    <nav class="navbar navbar-default">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Raga Quiz</a>
        </div>
      </div>
    </nav>

    <form action='/evaluate' method='POST'>

      <div class="container-fluid bg-1 text-center">
        <h3 class="margin">What Raga is this?</h3>
        <div class="card">
        <p></p>
          <p class="margin">Click play: </p>
              <iframe name="sndtrk" width="60" height="30" src= ${alap} frameborder="0"></iframe>
          <label for="ansField">Answer here: </label>
          <textarea id="ansField" name="answerField" rows="1" cols="13"></textarea>
          <p></p>
          <input type="submit" id="submit" value="Submit"/>
        </div>
        <p></p>
      </div>

    </form>

    <!-- Footer -->
    <footer class="container-fluid bg-4 text-center">
      <p>Samapriya Dandibhotla</p>
    </footer>

    </body>
    </html>

""")



HTML_TEMPLATE_A = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Raga Quiz</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
      <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
      <style>
      body {
        font: 20px Montserrat, sans-serif;
        line-height: 1.8;
        color: #f5f6f7;
      }
      p {
        font-size: 16px;
      }
      .margin {
        margin-bottom: 20px;
      }
      .bg-1 {
        background-color: #1abc9c; /* light blue */
        color: #ffffff;
      }
      .bg-2 {
        background-color: #474e5d; /* Dark Blue */
        color: #ffffff;
      }
      .bg-3 {
        background-color: #ffffff; /* White */
        color: #555555;
      }
      .bg-4 {
        background-color: #2f2f2f; /* Black Gray */
        color: #fff;
      }
      .container-fluid {
        padding-top: 70px;
        padding-bottom: 70px;
        overflow: hidden;
        max-width: 100%;
      }

      #next {
        color:black;
      }

      .navbar {
        padding-top: 15px;
        padding-bottom: 15px;
        border: 0;
        border-radius: 0;
        margin-bottom: 0;
        font-size: 12px;
        letter-spacing: 5px;
      }
      .navbar-nav  li a:hover {
        color: #1abc9c !important;
      }

      label {
        font-size:12px;
        display:block;
      }

      .card {
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        border-radius: 5px;
        background-color: #ffffff; /* White */
        color: #555555;
        width: 600px;
        height: 300px;
        padding-bottom: 1%;
        margin: auto;
      }

      </style>
    </head>
    <body>

    <!-- Navbar -->
    <nav class="navbar navbar-default">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Raga Quiz</a>
        </div>
      </div>
    </nav>

    <form action='/alapanaQuiz' method='POST'>

      <div class="container-fluid bg-2 text-center">
        <h1 class="margin">${result}</h1>
        <p></p>
        <h3>The ragam was ${rag}</h3>
        <p></p>
        <h4>${num} correct</h4>
        <input type="submit" id="next" value="Next"/>
        <p></p>
        <br></br>
      </div>

    </form>

    <!-- Footer -->
    <footer class="container-fluid bg-4 text-center">
      <p>Samapriya Dandibhotla</p>
    </footer>

    </body>
    </html>

""")

HTML_TEMPLATE_DONE = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Raga Quiz</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
      <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
      <style>
      body {
        font: 20px Montserrat, sans-serif;
        line-height: 1.8;
        color: #f5f6f7;
      }
      p {
        font-size: 16px;
      }
      .margin {
        margin-bottom: 20px;
      }
      .bg-1 {
        background-color: #1abc9c; /* Green */
        color: #ffffff;
      }
      .bg-2 {
        background-color: #474e5d; /* Dark Blue */
        color: #ffffff;
      }
      .bg-3 {
        background-color: #ffffff; /* White */
        color: #555555;
      }
      .bg-4 {
        background-color: #2f2f2f; /* Black Gray */
        color: #fff;
      }
      .bg-5 {
        background-color: #513769; /* Dark Purple */
        color: #ffffff;
      }
      .bg-6 {
        background-color: #255423; /* Green */
        color: #fff;
      }
      .bg-7 {
        background-color: #1e1d3d; /* dark blue */
        color: #fff;
      }

      .container-fluid {
        padding-top: 70px;
        padding-bottom: 70px;
        overflow: hidden;
        max-width: 100%;
      }

      #playAgain, #exit {
        display: inline-block;
        color:black;
      }

      .navbar {
        padding-top: 15px;
        padding-bottom: 15px;
        border: 0;
        border-radius: 0;
        margin-bottom: 0;
        font-size: 12px;
        letter-spacing: 5px;
      }
      .navbar-nav  li a:hover {
        color: #1abc9c !important;
      }

      label {
        font-size:12px;
        display:block;
      }

      .card {
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        border-radius: 5px;
        background-color: #ffffff; /* White */
        color: #555555;
        width: 500px;
        height: 300;
        padding-bottom: 1%;
        margin: auto;
      }

      </style>
    </head>
    <body>

    <!-- Navbar -->
    <nav class="navbar navbar-default">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Raga Quiz</a>
        </div>
      </div>
    </nav>

      <div class="container-fluid bg-7 text-center">
        <h1>THANKS FOR PLAYING!</h1>
        <p></p>
        <h3>Score: ${num}/5</h3>
        <p></p>
        <p></p>
        <form action='/again' method='POST'>
        <input type="submit" id="playAgain" value="Play Again?"/>
        </form>
        <p></p>
        <form action='/return' method='POST'>
        <input type="submit" id="exit" value="Exit"/>
        </form>

        <br></br>
      </div>

    <!-- Footer -->
    <footer class="container-fluid bg-4 text-center">
      <p>Samapriya Dandibhotla</p>
    </footer>

    </body>
    </html>

""")
