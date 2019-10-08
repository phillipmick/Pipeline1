<!DOCTYPE html>
<html lang="en">
<head>
<title>Lighthouse Island Bistro</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {font-family:Verdana, Arial, sans-serif;
      background-color: #00005D;
}
#wrapper { background-color: #b3c7e6;
           color: #000066;
           width: 80%;
		   margin: auto;
}
header { background-color: #869dc7;
        color: #00005D;
		padding: 10px;
}
header h1 { padding-left: 20px;
 }
header h2 { margin-top: 0;
            padding-right: 20px;
            font-size: .80em;
		    font-style: italic;
            text-align: right;
			color: #00005D; }

nav { float: left;
	   width: 150px;
	   letter-spacing:0.1em;
	   font-weight: bold;
}
nav ul { list-style-type: none;
         margin: 0;
         padding: 0;
}
nav li { padding: 15px;
}
nav a { text-decoration: none;
}
nav a:link { color: #ffffff; }
nav a:visited { color: #eaeaea; }
nav a:hover {  color: #869dc7;}
#content { background-color: #ffffff;
           color: #000000;
		   padding: 10px 20px;
		   margin-left: 150px;
	       overflow: auto;
}

h2 { color: #869dc7;
     font-family: arial, sans-serif;
	 margin: 5px;
}

figure {   float: right;
		   margin: 10px;
		   padding-left: 20px;
 }
figcaption { text-align: center;
		   font-size: .8em;
		   font-style: italic;
}

footer {font-size:70%;
         text-align: center;
         padding: 10px;
         background-color: #869dc7;
		 clear: both;
}
header, hgroup, nav, footer, figure, figcaption { display: block; }
@media only screen and (max-width: 768px) 
{
        nav  { float:none; width:auto; padding: 0.5em;  } 
		nav li {display: inline;}
		nav ul {text-align: center;}
	 #content { margin-left: 0 ;  }
	 #wrapper { width: auto;}
	 body { margin: 0; }
	 
         }

</style>
<!--[if lt IE 9]>
   <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"> </script>
<![endif]-->
</head>
<body>
<div id="wrapper">
  <header>
    <hgroup>
      <h1>Lighthouse Island Bistro</h1>
      <h2>the best coffee on the coast</h2>
    </hgroup>
  </header>
  <nav>
    <ul>
	 <li><a href="index.html">Home</a></li>
     <li><a href="menu.html">Menu</a></li>
     <li><a href="directions.html">Directions</a></li>
     <li><a href="contact.html">Contact</a></li>
	</ul>
   </nav>
<div id="content">
    <figure>
     <img src="lighthouseisland.jpg" width="250" height="355" alt="Lighthouse Island">
	 <figcaption>Island Lighthouse, Built in 1870</figcaption>
	 </figure>
   	<h2>Locally Roasted Free-Trade Coffee</h2>
    <p>Indulge in the aroma of freshly ground roast coffee. Specialty drinks are available hot or cold.</p>
    <h2>Specialty Pastries</h2>
    <p>Enjoy a selection of our fresh-baked, organic pastries, including
  fresh-fruit muffins, scones, croissants, and cinammon rolls.</p>
  	<h2>Lunchtime is Anytime</h2>
    <p>Savor delicious wraps and sandwiches on hearty, whole-grain breads with locally-grown salad, fruit, and vegetables. </p>
    <h2>Panoramic View</h2>
	<p>Take in some scenery!</p>
	<p>The top of our lighthouse offers a panoramic view of the countryside. Challenge your friends to climb our 100-stair tower.</p>
   </div>
   <footer>Copyright &copy; 2014
   </footer>
  </div>
</body>
</html>

