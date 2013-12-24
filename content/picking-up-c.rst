Picking up C#
#############
:date: 2013-07-03 16:14
:author: scovetta
:category: Uncategorized
:tags: c#
:slug: picking-up-c

It's been a while since I've done anything with C#, and I figured that
now's a good a time as any to brush things off and get up to speed with
the language. I'm a Mac guy now, so I'll be using Mono to write code.
This post will be a list of resources that I'm using to pick up things
as quickly as possible.

**Development Environments**

I came across `Xamarin Studio`_, which is working great so far. It's
free for basic use, and relatively affordable for commercial/business
use. It integrates with Xcode and other OSX tools, allowing you to write
iOS apps completely in C#. Pretty cool. I'm not sure what the
relationship is between this and the MonoDevelop IDE, but I'm getting
directed to download Xamarin Studio from the MonoDevelop website, so
there's something going on between the two of them.

You'll need to install Mono before that, and you can get that at
`MonoDevelop`_.

**Books & Tutorials**

I have a C# book upstairs in the attic somewhere. I don't feel much like
looking for it, so I'll try some online resources first.

The first free online ebook that I'm reading through is `C# School`_,
available at Programmer's Heaven. It's a bit outdated, covering up to C#
2.0 (C# 5.0 was released in late 2012), but covers the basics.

I am also supplementing things by watching the Lynda.com `C# Essential
Training`_ course. Lynda costs $25/month, but the quality of the videos
more than makes up for it.

 

**C# 3.0 - New Features**

**Automatic Properties:**

Instead of doing:

.. code-block:: c#

    private string name;
    public string Name {
        get {
            return name;
        }
        set {
            name = value;
        }
    }

We can just do:

.. code-block:: c#

    public string Name { get; set; }

**Object Initializers**

Instead of doing:

.. code-block:: c#

    Customer c = new Customer();
    c.CustomerID = "ABC123";
    c.CustomerName = "Mike";

We can just do:

.. code-block:: c#

    Customer c= new Customer() { CustomerID = "ABC123", CustomerName = "Mike" };

**Collection Intiailizers**

.. code-block:: c#

    List<Customer> clist = new List<Customer>() {
        new Customer { CustomerID = "ABC123", ... },
        new Customer { CustomerID = "DEF456", ... },
        ...
    }

**Type Inference**

Instead of doing:

.. code-block:: c#

    List<Customer> clist = new List<Customer>();

We can just do:

.. code-block:: c#

    var clist = new List<Customer>();


**Up to Speed on C# Versions**

-  `What's New in C# 3.0`_ (MSDN)

**Topic-Specific Videos**

-  `C# 5.0 Async and Await Demo`_

.. _Xamarin Studio: http://xamarin.com/
.. _MonoDevelop: http://monodevelop.com/Download
.. _C# School: http://www.programmersheaven.com/ebooks/csharp_ebook.pdf
.. _C# Essential Training: http://www.lynda.com/Visual-Studio-2010-tutorials/C-Essential-Training/83789-2.html
.. _What's New in C# 3.0: http://channel9.msdn.com/Blogs/DavidAiken/VS2008-Training-Kit-Whats-new-in-C-30
.. _C# 5.0 Async and Await Demo: http://www.youtube.com/watch?v=cxOC2NMJJq8
