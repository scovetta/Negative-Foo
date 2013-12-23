Danger Will Robinson!! New TLDs and the Universal Search Bar
############################################################
:date: 2013-07-25 08:43
:author: scovetta
:category: Published Articles
:tags: dns
:slug: danger-will-robinson-new-tlds-and-the-universal-search-bar

If you haven't noticed recently, your web-browser's URL bar doubles as a
web-search bar. Type in google.com and you'll go there. Type in 'giant
fish statue', and you'll get you expect. How does the browser know which
action to perform?

One might think that the browser first tries to resolve what you typed
into an IP address, and it fails, perform a search. That might make
sense, but isn't correct, because:

-  Some ISPs will hijack unknown domains to point to their very
   unhelpful advertising page (I'm looking at you, `Optimum Online`_!)
-  Some browsers will fail out with a error page:

|Chrome Invalid Domain Image|

*Ok, so what?*

Let's say you're looking for a very popular document, say,
royalbaby.pdf. You type that text into your URL bar, and you expect to
get a page of search results, but some time prior, somebody went along
and registered the domain *royalbaby.pdf*. Now you think you're looking
at search results, but you're actually the that guy's page, looking at
whatever he wants to show you.

This is similar to typo-squatting, but relying on the dual-use nature of
URL bars.

So what can we do?

-  First, we could ask users to look at the URL bar, but if there's
   anything we've learned over the past 15 years, its that that type of
   training is useless at scale.
-  We could disable URL bars for searching, but that seems like a pretty
   silly "fix".
-  Web-browsers could keep (and update) a list of valid TLDs and somehow
   use that, but suppose I'm looking to do research on the DOS-era
   COMMAND.COM shell?
-  Web-browsers could ask the user whether they meant to go to
   COMMAND.COM or do a search for COMMAND.COM.
-  Web-browsers could default to searching unless the http:// prefix was
   used.

None of these answers are very satisfying. Fortunately, when I took a
look at the `current`_ and `proposed`_ TLD list, only of a few popular
file extensions appeared on the list, so until someone registers .PDF or
.DOCX, this will likely be a minimal problem at best. I did see .APP on
the proposed list, which would certainly conflict with searches for,
say, Mail.App or Calendar.App, which I'm sure would be among the first
domains to be registered.

 

.. _Optimum Online: https://www.optimum.net/pages/DNS.html
.. _current: http://data.iana.org/TLD/tlds-alpha-by-domain.txt
.. _proposed: http://money.cnn.com/infographic/technology/new-gtld-list/

.. |Chrome Invalid Domain Image| image:: http://negativefoo.org/wp-content/uploads/2013/07/Screen-Shot-2013-07-25-at-8.25.47-AM-300x148.png
   :target: http://negativefoo.org/wp-content/uploads/2013/07/Screen-Shot-2013-07-25-at-8.25.47-AM.png
