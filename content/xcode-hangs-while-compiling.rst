Xcode Hangs While Compiling
###########################
:date: 2013-03-03 14:08
:author: scovetta
:category: How To
:tags: Xcode
:slug: xcode-hangs-while-compiling

I've run into a recent issue where Xcode pins the CPU (technically it's
kernel\_task) during a compile. Nothing major changed, so I tried clean
builds, restarting Xcode, restarting OSX, but nothing changed. After a
little bit of investigation, I found the culprit: I had a bad alias
(pointed to itself or a nonexistent file), and it seemed like the
compiler got stuck in a loop trying to resolve it. Once I fixed this and
added that actual file back to the project, everything compiled fine.
