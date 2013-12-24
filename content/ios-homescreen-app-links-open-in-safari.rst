iOS Homescreen App Links Open in Safari
#######################################
:date: 2013-01-08 21:05
:author: scovetta
:category: How To
:tags: html5, iOS
:slug: ios-homescreen-app-links-open-in-safari

On iOS, you can configure web-sites that have been added to the user's
home screen to open without the chrome around Safari by setting the meta
tag:

.. code-block:: html

	<meta name="apple-mobile-web-app-capable" content="yes">


However, you'll soon notice that when a user clicks on any links within
the page, they'll open up in a new Safari window (certainly not what
you'd expect). The solution comes from `Stack Overflow`_. If you're
using jQuery or Zepto:

.. code-block:: javascript

    $("body").on("click", "a", function(event) {
       event.target.target != "_blank" && (window.location = event.target.href);
    });

Otherwise, you can use the following:

.. code-block:: javascript

    document.body.addEventListener(function(event) {
        if (event.target.href && event.target.target != "_blank") {
            event.preventDefault();
            window.location = this.href;                
        }
    });

.. _Stack Overflow: http://stackoverflow.com/questions/2898740/iphone-safari-web-app-opens-links-in-new-window
