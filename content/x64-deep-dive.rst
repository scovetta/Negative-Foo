x64 Deep Dive
#############
:date: 2011-11-17 01:47
:author: scovetta
:category: Uncategorized
:tags: x86
:slug: x64-deep-dive

This tutorial discusses some of the key aspects of code execution on the
X64 CPU like compiler optimizations, exception handling, parameter
passing and parameter retrieval and shows how these topics are closely
related to each other. It covers the important debugger commands related
to the above topics and provides the necessary background required to
interpret and understand the output of these commands. It also
highlights how the X64 CPU does things differently from the X86 CPU and
how it affects debugging on X64. And finally it ties everything together
and illustrates how this knowledge can be applied to retrieve register
based parameters from X64 call stacks, something that always poses a
challenge when debugging X64 code.

This tutorial takes a step by steps approach to present the content and
makes use of diagrams, disassembly listings and debugger output
extensive to drive home the key points. Readers are expected to have a
good understand of how things work on the X86 CPU in terms of register
usage, stack usage and function layout to make most of this tutorial.

`Read Tutorial`_

.. _Read Tutorial: http://www.codemachine.com/article_x64deepdive.html
