XIB Changes Not Appearing in iOS Simulator
##########################################
:date: 2013-03-01 08:45
:author: scovetta
:category: How To
:tags: iOS
:slug: xib-changes-not-appearing-in-ios-simulator

I came across an interesting issue this morning and I thought I would
share. I was editing a ViewController and associated XIB file, adding an
IBAction to do some (irrelevant) things, but nothing was working. The
IBAction wasn't being called at all (though the viewDidLoad function
was). I checked and double-checked that the outlet was referenced from
the XIB file, to no avail. I tried clean builds, restarted Xcode, and
everything else I could think of.

Finally, I tried resetting the iOS Simulator.

**Bingo!** The application crashed with a "can't find XIB file" error.

The problem was that after a git merge, the XIB file was removed from
the target, and so wasn't being included in the distribution. However,
apparently since the old XIB file (without the IBAction) already
existed, it was being used, despite a clean build occurring. I re-added
the XIB file manually by choosing the Target, Build Phases, Copy Bundle
Resources, and added the XIB file to that section. (I also had to add
the associated implementation (.m) file to the Compile Sources section
for a similar reason.)

I thought that when Xcode deployed to a simulator, it was transferring
the entire application bundle, but it seems like it's doing a (slightly
broken) sync instead.

**So lesson learned:** If you're troubleshooting iOS development and you
ever don't see your changes, you probably want to add **Reset iOS
Simulator Settings** to your checklist.
