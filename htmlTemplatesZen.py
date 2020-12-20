from string import Template

HTML_TEMPLATE_C = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Alapanas: Zen</title>
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
        background-color: #3b753d; /* light green */
        color: #fff;
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

      #next, #menu {
        color:black;
        display: inline-block;
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
        height: 350;
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
          <a class="navbar-brand" href="#">Alapanas</a>
        </div>
      </div>
    </nav>


      <div class="container-fluid bg-3 text-center">
        <h3 class="margin">Raga ${rag}</h3>
        <div class="card">
        <p></p>
          <p class="margin">Click play: </p>
              <iframe name="sndtrk" width="230" height="150" src= ${alap} frameborder="0"></iframe>
          <p></p>

          <form action='/next' method='POST'>
          <input type="submit" id="next" value="Next"/>
          </form>

          <form action='/return' method='POST'>
          <input type="submit" id="menu" value="Exit"/>
          </form>
        </div>
      </div>


    <!-- Footer -->
    <footer class="container-fluid bg-4 text-center">
      <p>Samapriya Dandibhotla</p>
    </footer>

    </body>
    </html>

""")
