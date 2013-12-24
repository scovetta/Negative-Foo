SSL Certificate Madness!
########################
:date: 2011-03-29 05:19
:author: scovetta
:category: How To
:tags: ssl
:slug: ssl-certificate-madness

If you've ever wasted too many hours of your life trying to get a server
SSL certificate installed on Apache Tomcat or J-Boss, this post might
help you out a bit.

First, you can ignore keytool. (Hooray!) Tomcat and J-Boss both support
using certificates in the PKCS12 format, but we're going to assume that
you're starting out with just a PEM-encoded key and certificate file.

**Step 1: Create a key file**

.. code-block:: bash

	openssl genrsa -aes256 -passout “pass:foobar" -out server.key 2048

This creates a 2048-bit key, encrypted with AES-256 using the password
“foobar". If you don't want to use a password at all, you can leave
those out, and just have:

.. code-block:: bash

	openssl genrsa -out server.key 2048

You really want to use a 2048-bit key instead of the older 1024-bit
keys. Besides being much stronger, most certificate authorities will no
longer create certificates based off of 1024-bit keys.

**Step 2: Create a Certificate Signing Request (CSR)**

.. code-block:: bash

	openssl req -new -key server.key -out server.csr

This command creates a new CSR based off an existing key. You'll be
prompted for the key password you created in Step #1 and for details of
the certificate. The common name needs to match what the web-browser
will be accessing, so if you're planning to put this certificate on a
server called “centurian24.yourcompany.com", but end-users will go to
“support.yourcompany.com", then you should put “support.yourcompany.com"
as the common name.

**Step #3: Get the certificate signed.**

Send the certificate to VeriSign, GoDaddy, or your favorite SSL
certificate authority. If you're asked for the server type, say Apache
(not Tomcat— just Apache).

You'll get back a certificate and possibly a set of intermediate
certificates. These intermediate certificates are the “glue" between the
server certificate (which you now have) and the root certificate
authority certificate (which comes pre-installed in web-browsers).
Sometimes you can get away with not installing the intermediate
certificate, but we're trying to do things the right way.

If the certificate provider doesn't give you an intermediate
certificate, you may need to find it yourself on their website. Some
links that might help:

-  `GoDaddy Certificate Chain`_ (Use gd\_bundle.crt)
-  `VeriSign Certificate Chain`_ (Choose one of the bundles)

**Step #4: Create a PKCS12 archive.**

.. code-block:: bash
	
	openssl pkcs12 -export -chain -CAfile intermediate.crt -in server.crt -inkey server.key -out server.p12

This command takes the three files you now have and combines them into a
single file, which can be imported into IIS, Apache Tomcat, or
J-Boss. You'll be prompted for a password for the PKCS12 file, which you
will use in the next step. You'll also be prompted for the password you
used to create the key in Step #1.

**Step #5a: Configure J-Boss**

You can configure J-Boss by editing the
server/default/deploy/jboss-web.deployer/server.xml and

.. code-block:: xml

	<Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true" maxThreads="150" 
			   scheme="https" secure="true" clientAuth="false" sslProtocol="TLS" 
			   keystoreFile="${jboss.server.home.dir}/conf/server.p12" 
			   keystorePass="keystorePassword" keystoreType="pkcs12"/>

The keystoreType="pkcs12" line is very important, and you may need to
un-comment this section from the configuration file.

**Step #5b: Configuring Apache Tomcat**

Apache Tomcat is similar to J-Boss, and the configuration is almost
identical. In the $CATALINA\_BASE/conf/server.xml file:

.. code-block:: xml

	<Connector port="8443" maxThreads="150" scheme="https" secure="true"
			   SSLEnabled="true" sslProtocol="TLS" keystoreFile="conf/server.p12" 
			   keystorePass="keystorePassword" keystoreType="pkcs12"/>``

Please note that you don't have to use a PKCS12 file with Apache
Tomcat. \ `Apache Tomcat 7`_ supports JKS (legacy), PKCS11 (Apache) and
PKCS12 (what we did above) formats. If you want to use PKCS11, you can
just use:

.. code-block:: xml

	<Connector port="8443" maxThreads="150" scheme="https" secure="true"
			   SSLEnabled="true" sslProtocol="TLS" SSLCertificateFile="conf/server.crt"
			   SSLCertificateKeyFile="conf/server.key" SSLPassword="<your-key-password>" />``

**Step #5c: Configuring IIS**

TBD

**Step #6: Start the Web Server**

Your web-server should start and will be responding on the SSL port
(either 443 or 8443, unless you've configured it to be something else.

.. _GoDaddy Certificate Chain: https://certs.godaddy.com/anonymous/repository.seam
.. _VeriSign Certificate Chain: https://knowledge.verisign.com/support/ssl-certificates-support/index?page=content&id=AR657
.. _Apache Tomcat 7: http://tomcat.apache.org/tomcat-7.0-doc/ssl-howto.html
