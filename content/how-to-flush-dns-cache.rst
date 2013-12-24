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

::

	C:\> ipconfig /flushdns

Linux
~~~~~

To flush DNS cache within Linux, you can restart the ncsd daemon, which
could be done in any of the following ways. It depends on your specific
Linux distribution. 

Reference: http://www.cyberciti.biz/faq/rhel-debian-ubuntu-flush-clear-dns-cache/

::

	$ sudo /etc/init.d/nscd reload 
	$ sudo /etc/rc.d/init.d/nscd reload
	$ sudo service nscd reload

If you're using dnsmasq, you can restart that process as well:

::

	$ sudo /etc/init.d/dnsmasq restart
	# service dnsmasq restart

If you're using Bind, you can flush the daemon's cache by doing:

::
	
	# /etc/init.d/named restart
	# rndc restart
	# rndc exec
	$ sudo rndc flush

Mac OSX
~~~~~~~

You can flush your DNS cache by using either the dscacheutil command
or by restarting the mDNSResponder process, depending on your version
of OS X. 

Reference: http://randomerrata.com/post/45487345023/clear-dns-cache

::

	sudo dscacheutil -flushcache       ; Leopard & Snow Lepoard
	sudo killall -HUP mDNSResponder    ; Lion & Mountain Lion
