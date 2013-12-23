How to Say You've Been Hacked... in a Good Way
##############################################
:date: 2012-02-11 10:04
:author: scovetta
:category: Security
:tags: data breach, sony, TEDxBigApple, zappos
:slug: how-to-say-youve-been-hacked-in-a-good-way

|image0|\ I received an e-mail from TEDxBigApple this morning that
started with the line:

**We've been hacked!**
^^^^^^^^^^^^^^^^^^^^^^

Now, since TED is all about innovation, I assumed this was a (not so)
clever marketing attempt at using the "other" definition of hacker, so I
read on.

No, no. They were hacked.

    As you know, Feb 4th was centered around Disruptive Ideas, and as
    poetic justice would have it, our success means we have been
    unfortunately pranked by a Disruptive force. Someone or someones
    surreptitiously gained access to our registered database and has
    sent out an invitation to join a site called biapplepulse.com.

Wait, what?

[youtube\_sc url="AcvDgZI91SU" title="YouTube%20Video%20Player"
modestbranding="1" hd="1"]

Ok, so it's not incompetence anymore, but **poetic justice; hacking** is
now\ **being pranked**, and\ **criminals**\ are just a\ **Disruptive
force**?

As much as I hate the corporate "come to Jesus"-style notifications,
they usually have quite a bit less BS than this. When a company is
hacked, and data lost, I expect a number of things:

#. **I want to know what was lost, specifically.** Was it just my name
   and e-mail address? A hashed password? If so, how was it hashed?
   Where was the salt stored? How many records were lost?
#. **What was the root cause?** Was a system not patched? Did an
   administrator use a password of **password1**? Did the founder just
   give the list to their buddy?
#. **Who was responsible?** Was this an organized campaign by a foreign
   nation? Some jerk running metasploit and selling the information to
   others?
#. **What is being done to make sure this never happens again?** Saying
   things like "we're strengthening our security measures... (blah blah
   blah)" is not sufficient. If you had taken security seriously before,
   you would have had those strengthened security measures set up in the
   first place. Oh, so NOW you realize that security is important. As a
   customer, I want to know specifically what is being done. No
   generalities anymore.

As an organization that customers put their trust in with their personal
information, the data breach exposes the fact that you are in fact **not
trustworthy**, and the onus on you to earn back that trust. The points
above are a good start, but in general, you need to be honest and
transparent when you alert your customers as soon as possible. If your
lawyers are telling you to delay notification or hide facts from the
public, it's time to get new lawyers.

After the Zappos breach in January 2012, I sent a letter to the company
asking for clarification on their existing security practices and the
nature of the data lost:

    First, the Zappos website states that "[you] also encrypt payment
    information traveling within our company as well. All payment
    information is encrypted while in storage within a network that is
    firewalled off from the rest of the company and the internet.". I
    don't understand how the last four digits of my credit card number
    (clearly, "payment information") could have been disclosed if they
    were encrypted, unless the cryptographic keys were also disclosed.

    Second, the notification e-mail mentions that my password is
    "cryptographically scrambled". As I'm sure you know, there is a
    world of difference between weak and strong methods of cryptographic
    hashing. Which method of hashing was used, and was a per-user and/or
    static salt used to further protect the passwords? This is important
    because many users re-use passwords between sites, and users need to
    know whether they need to change their passwords on all sites or
    not.

    Third, your website also mentions in a few areas that you use the
    Trustwave Trusted Commerce Seal as an "assurance that [you] use
    industry standard measures to secure [my] personal information". The
    image is from 2007 and I cannot find any active links showing
    current Trustwave certification. Did Zappos have current
    certification from Trustwave at the time of the breach?

    Finally, and probably the most important. Has Zappos undergone
    regular, external penetration tests on your critical systems? Were
    the systems breached included in these security assessments? Was the
    root cause of the breach a zero-day / APT-style attack, out of date
    patches, insider attack, lack of policy, or something else? Your
    customers need to understand if Zappos is trustworthy enough to
    continue doing business with, and prompt disclosure if a good first
    step, the devil is in the details, and the world is watching. I
    would be happy to discuss these matters under NDA, though for the
    benefit of your users, I would hope that you would consider public
    disclosure in the best interests of the company.

I received the following, totally unhelpful response.

    Thank you for contacting the Zappos.com Customer Loyalty Team.

    We are currently cooperating with the FBI in an ongoing
    investigation, including undergoing digital forensics. We sincerely
    apologize that we have been unable to answer your questions.

    The email communication that was sent to you by our CEO was also
    sent to our employees. Here at Zappos, our customers come first, as
    soon as we are able to provide more information we will let you
    know.

    As always, please remember that Zappos.com will never ask you for
    personal or account information in an e-mail.

    | To stay up-to-date on all current information regarding this
    situation, please see:
    |  www.zappos.com/passwordchange

    | Sincerely,
    |  The Zappos.com Customer Loyalty Team

Not surprisingly, nothing new has been posted to the link above since
January 20th.

Unfortunately, I see only two ways of disclosure moving in this
direction:

-  **Regulation.** The only reason that companies tell their customers
   anything is that they're required to by law. They don't have your
   best interests in mind, and they don't **really** feel sorry for the
   breach. Stronger regulations that require more detailed disclosure
   would go a long way toward informing customers of the actual risk
   they face. In addition, if **monetary damages** were included,
   perhaps companies in general would more appropriately fund security
   programs. If Sony knew they would have had to pay $250 to each
   customer lost, for each of the 75 million records lost, don't you
   think they would have invested a bit more in their security program?
-  **Loss of Customers.** Hardly a day goes by when some company needs
   to alert customers of a data breach. Familiarity breeds apathy in
   this regard, and the outrage that followed the CardSystems and TJ
   MAXX breaches has become only a dull groan of displeasure. If
   customers immediately ceased to do business with any company that
   loses their records, it would also increase (quite significantly) the
   cost of a data breach to the company.

I've included the full text of the e-mail received from TEDxBigApple.

    **Apologies from TEDxBigApple...**

    | 
    |  **We've been hacked!**

    | 
    |  As you know, Feb 4th was centered around Disruptive Ideas, and as
    poetic justice would have it, our success means we have been
    unfortunately pranked by a Disruptive force. Someone or someones
    surreptitiously gained access to our registered database and has
    sent out an invitation to join a site called biapplepulse.com. We
    would like to be clear that this site is in no way affiliated with
    TED, TEDx, or TEDxBigApple. If you received this email we sincerely
    apologize. As a precautionary step you may want to block all emails
    coming from an address ending with @bigapplepulse.com, but that is
    entirely up to you.

     

    All information pertaining to TEDxBigApple will come from
    info@tedxbigapple.com and noone else. If you receive any messages
    from third parties please feel free to inform us and we will
    investigate the source of the problem.

     

    We hope that you have been enjoying seeing some photos of the event,
    and we are working hard to bring you all the videos by the end of
    next week!

     

    In the meantime if you would like to be removed from our email list
    we will be sad, but of course respect your wishes. Your information
    and involvement with TEDxBigApple means a lot to us and we hope that
    you will continue to be a part of our events moving forward.

    Let's strengthen the innovation community together.

    | Warmly,
    |  -TEDxBigApple Team

.. |image0| image:: http://negativefoo.org/wp-content/uploads/2012/02/tedxbigapple291.png
   :target: http://negativefoo.org/2012/02/how-to-say-youve-been-hacked-in-a-good-way/tedxbigapple291-2/
