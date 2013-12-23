Viewing All G-Mail Messages Hack
################################
:date: 2011-11-23 23:03
:author: scovetta
:category: How To
:tags: google, hack
:slug: viewing-all-g-mail-messages-hack

I don't really consider this worthy of being called a "hack", but I
noticed that if you load the **all** anchor within G-Mail, you see all
received messages, regardless of whether they're in your Inbox, your
archive, or in a folder. It could be useful if you know you received a
message at a certain time, but not sure where it went.

To do this, open your G-Mail Inbox and change #inbox to #all in the URL.
It should look something like this:

https://mail.google.com/mail/u/0/#all

In fact, after examining some of the JavaScript that comes down with the
G-Mail page:

``function Ol(b){nl.call(this,"all",b)}function Pl(b){nl.call(this,"archive",b)}function Ql(b){nl.call(this,"chats",b)}function Rl(b){nl.call(this,"delivered",b)}function Sl(b){nl.call(this,"drafts",b)}function Tl(b){nl.call(this,"inbox",b)}function Ul(b){nl.call(this,"muted",b)}function Vl(b){nl.call(this,"outbox",b)}function Wl(b){nl.call(this,"sent",b)}function Xl(b){nl.call(this,"spam",b)}function Yl(b){nl.call(this,"starred",b)}function Zl(b){nl.call(this,"trash",b)}``

It seems that you can use any of these to bookmark a specific view into
G-Mail:

-  **all: View all messages**
-  archive: View archived messages
-  chats: View chats
-  delivered: Not sure
-  drafts: View drafts
-  inbox: Default, view your inbox
-  muted: **Not sure**
-  outbox:\ **Outbox, but doesn't seem to work**
-  sent: View sent items
-  spam: View your spam folder
-  starred: View starred messages only
-  trash: View trashed messages

