"Security Questions" Considered Harmful
#######################################
:date: 2009-10-08 03:59
:author: scovetta
:category: Uncategorized
:tags: security
:slug: security-questions-considered-harmful

Many web-sites today have implemented "secret questions" that are used
when you forget your password or as second factor of authentication.
Questions like \ *What is your mother's maiden name?* or *What is the
name of your primary school? *\ are among a small list of very common
questions.

The basic reasons why these questions should be avoided include:

-  There isn't enough entropy in the answers
-  The answers are often publicly discoverable
-  The answers are common across different web-sites

**Reason #1 - Not Enough Entropy**

When you answer a question like, \ *What was the make & model of your
first car?*, there are only a limited number of answers. Out of 100
random individuals in the US, how many of them do you think would
answer, "Toyota Corolla", "Honda Civic", or "Nissan Sentra"? (I have no
idea if these are actually the most popular answers, but you get the
point.)

A particularly awful question that further illustrates the point
is \ *Are you male or female? *\ The attacker gets a 50% chance of
guessing correctly.

We can easily estimate the strength of a secret question through the
following method:

#. Let X be the total number of unique possible answers to the question.
#. Calculate log(x) in base 2. This determines the number of bits
   required to encode all possible answers.
#. Divide that answer by 6.2 (approximate number of bits in a standard
   password character).

That's it. Let's try it with the question, \ *What was the make & model
of your first car?*

`Edmunds`_ provides a list of the 50 most popular make-model
combinations. I have no idea how it calculated that, but let's assume
it's correct for the demographics of our victim base. We take 50, and
calculate log(50) in base 2. We can do that easily by searching Google
for \ `log(50)/log(2)`_ and get an answer of 5.64. We divide that number
of 6.2 to get 0.90.

**That means that asking, \ *What was the make & model of your first
car? *\ is as strong as asking the user for a one-character password.**

**Reason #2 - Answers are Publicly Discoverable**

In September 2008, Sarah Palin's Yahoo account was compromised by a
"hacker" that was able to reset the account password after providing
Sarah Palin's birthdate, which was publicly available on \ `her
Wikipedia page`_.

This demonstrates that answers to security questions are often public
knowledge. For example:

-  **Birthdate:** Facebook, MySpace, Wikipedia, birthdatabase.com, and
   other sites
-  **Car Make & Model:** DMV records, which are public records, can be
   obtained by anyone
-  **Mother's Maiden Name: ~**\ 25% chance that an uncle or cousin will
   have the same last name, Facebook, MySpace, Classmates.com
-  **Name of Primary School: **\ Most people live near where they grew
   up.

**Reason #3 - Answers are Common Across Web-Sites**

When multiple web-sites ask the same security question, it reduces the
security of all of the sites, because a security compromise against any
one of those sites could result in attackers logging in as affected
users into the other sites. If PayPal asks me about my mother's maiden
name, and so does foobar.com, and an attacker gets into the database at
foobar.com, then they'll have my mother's maiden name, and can reset my
password at PayPal.

**What Can We Do?**

It's usually far easier to point out a problem than to fix it, and
that's certainly true in this area. I have a few suggestions on how to
make the process a bit safer.

**For Web Developers:**

#. **Store Answers in Hashed Form.** Never store security answers in
   clear text, or even encrypted. Instead, the answer provided should be
   hashed with a public and private salt, just like a password. In order
   to make things a little easier on the user (e.g. "Saint Agnes" vs.
   "St. Agnes"), you can remove spaces, convert to a single case, and
   substitute common abbreviations, so that both answers would be
   converted to SAINTAGNES before being hashed and stored. The result is
   that if an attacker were to ever compromise your database, the hashed
   answers would not be useful in attacking any other web-sites.
#. **Ask the User for the Question. **\ Instead of forcing the user to
   choose a question from a list, ask them to write their own question.
   If the user attempts to use a common question, force them to use a
   different one. Store the question encrypted (not hashed, since you'll
   need to ask them at some point). This doesn't guarantee that the user
   will choose a strong question, but neither does it restrict them to
   choose a weak one.
#. **Never Limit Password Length. **\ It seems absurd to me how many
   major web-sites limit password length to 8 characters or less. Never
   limit the password length that your users give you. (You can be
   reasonable, and use something like 256 characters if you're worried
   about a denial of service attack.) I'm including this best practice
   in this list because the answer to a secret question is a de-facto
   password and should be treated in the same way.

**For Users:**

#. **Use Password Hasher. **\ Password Hasher is a add-on for Firefox,
   but a similar add-on could be created for any web-browser. The
   purpose of Password Hasher is to pre-hash passwords (using a secret
   key) before they are submitted in a form. The user types "St. Agnes"
   into the secret answer field, but the web-browser submits
   "d8b82e7d4b825ee2451f9c5743ab8e41ad0359dba1b4f18f68eeb232b499878a"
   instead.
#. **Don't Answer Questions Truthfully. **\ When a web-site asks you for
   the name of your primary school, \ *you don't actually have the
   answer truthfully*. Type anything you want - just be sure that if the
   site asks you that question when you need to reset your password, you
   type that same thing in. Giving out information such as your mother's
   maiden name, social security number (even the last four digits) or
   birthdate should be avoided whenever possible.
#. **Remove Your Birthdate from Social Networking Sites. **\ Yes,
   everyone loves getting a bunch of "Happy Birthday" tweets or posts on
   their Facebook wall, but your birthdate is pretty sensitive and
   shouldn't be given out to the world.

**More Information:**

-  Bruce Schneier's Blog: \ `Secret Questions`_, May 2009
-  Technology Review: \ `Are Your "Secret Questions" Too Easily
   Answered?`_, May 2009

.. _Edmunds: http://www.edmunds.com/reviews/list/mostpopular/
.. _log(50)/log(2): http://www.google.com/search?q=log%2850%29/log%282%29
.. _her Wikipedia page: http://en.wikipedia.org/wiki/Sarah_Palin
.. _Secret Questions: http://www.schneier.com/blog/archives/2009/05/secret_question.html
.. _Are Your "Secret Questions" Too Easily Answered?: http://www.technologyreview.com/web/22662/?a=f
