How to Flush DNS Cache
######################
:date: 2011-11-17 19:13
:author: scovetta
:category: How To
:tags: dns
:slug: how-to-flush-dns-cache

Instructions for flushing your DNS cache in various operating systems.

Microsoft Windows
~~~~~~~~~~~~~~~~~

To flush your DNS cache within Windows, open a command prompt and run
the following command:

``ipconfig /flushdns``

Linux
~~~~~

To flush DNS cache within Linux, you can restart the ncsd daemon, which
could be done in any of the following ways. (It depends on your specific
Linux distribution.)

``sudo /etc/init.d/nscd reload sudo /etc/rc.d/init.d/nscd reload sudo service nscd reload``

If you don't have nscd installed, you can install it by doing one of the
following:

``apt-get install nscd yum install nscd``

If you're using Bind, you can flush the daemon's cache by doing:

``sudo rndc flush``

Mac OSX
~~~~~~~

You can flush your DNS cache by using either the lookupd or the
dscacheutil command, depending on your version of OSX:

``lookupd -flushcache     ; Leopard dscacheutil -flushcache    ; Snow Lepoard and Lion``
