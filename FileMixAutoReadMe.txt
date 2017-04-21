FILEMIXAUTO - Sugar Activity/Linux version - Notes
Art Hunkins
abhunkin@uncg.edu
www.arthunkins.com


Working with User Soundfiles/Objects

FILEMIXAUTO is a self-playing, automatic version of the FileMix
activity. FileMixAuto can handle 1-4 mono or stereo soundfiles. The
files can be of any sample rate and a variety of uncompressed
formats including WAV and AIFF; also Ogg/Vorbis, but not MP3. The
Ogg/Vorbis format is only possible when the Sugar version is later
than 0.84; this excludes the original XO-1 and SoaS
(Sugar-on-a-Stick) Strawberry.

*However*, the ogg vorbis format (which is written by later versions
of the Record activity) *can* be used by SoaS (Strawberry) 0.84 if
libsndfile is updated. This can be done while connected to the
internet by issuing the following commands in the Terminal:
  su <Enter>
  yum update libsndfile <Enter>
Neither the XO-1.5, nor XO-1 upgraded to Sugar 0.84 require this mod.

Students are encouraged to create their own soundfiles, especially
to make their own nature soundscapes. (This is the primary intent
behind FileMixAuto. The four short "nature" files included here
are abbreviated versions of those from the author's DUSK AT ST.
FRANCIS SPRINGS [www.arthunkins.com].) Soundscapes can to set to play
from 30 seconds up to 24 hours, and can be shut off whenever desired.
They can be used as background for movement, pantomime, dramatic
productions, meditation/relaxation, or just to create a mood.

The natural vehicle for soundfile creation is the Record activity.
This activity is fairly simple and straightforward; the only problem
is that many versions of it do not work with various incarnations of
Sugar. The following pairings of Record with Sugar seem to work
reliably: v64 with Sugar-on-a-Stick Strawberry (0.84 - works rather
poorly); and v86 with XO-1.5, and XO-1 upgraded to Sugar 0.84. Sugar
0.86 (Blueberry) and above (as of 5/2011) are compatible with Record
v90/91, including XO's upgraded to at least Sugar 0.90 (Mango lassi -
Fedora 14). Please note that Record prior to v74 (except for v61-64)
produce ogg *speex* files; these files are incompatible with FileMix.

Soundfiles must be moved into the folder where this file resides,
and be renamed soundin.1 through soundin.4. Alternatively, and more
practically, however, user sound-files may be loaded from the Journal
(Sugar 0.84 and later). In this case, only wav and ogg/vorbis formats
are allowed.

Unfortunately, no other Sugar activity (including TimeLapse,
ShowNTell, and most importantly, Etoys) produces soundfiles useable
by FileMixAuto. Either they write files other than Ogg Vorbis or wav,
are restricted to Sugar 0.82, or their output is inaccessible to the
Journal and other activities (the case with Etoys).

More advanced users may wish to record their soundfiles on some other
system, and import their wav or ogg vorbis files into the Journal via
a USB drive. (Display drive contents in Journal view, and drag your
file onto the Journal icon.)

Otherwise, adventurous users may run the fine Audacity application to
record and edit. (Happily, none of the limitations of the Record
activity apply here.) In the Terminal, connected to the web, enter:
  su <Enter>
  yum import audacity <Enter>
  ...
  audacity <Enter>
(you are now running Audacity from the Terminal).

When you are finished recording and editing (including auditioning the
file in loop mode), "Export" the file in wav or ogg vorbis format,
saving it to a USB drive with appropriate filename. Exit audacity. In
the Journal, display the contents of your USB drive, and drag your
newly-recorded file onto the Journal icon. It is now ready for
FileMixAuto.
 

The (Random) Controls

A number of controls, all of which are set prior to performance, allow
for independent random variation of the (up to) 4 soundfiles. Files of
slightly varied duration (the default soundfiles are excellent
examples), that begin at different random points within the file,
create an ever-changing texture. If the loops are carefully and
continuously made, and striking events avoided, the resultant
soundscapes should be both seamless and modestly interesting.

1) Number of files: self-explanatory (soundin.1 is file #1). If you
don't need all 4, reduce the number, as it is less work for the
computer. This is not crucial, however, as the volumes of unwanted
files can be reduced to zero. If you do not select one of your own
files, the corresponding default file will play.

2) Maximum Volume, files 1-4: here is where you set basic mix levels.
The files never get relatively louder than this.

3) Random Rate: the common random speed at which random changes occur.
A rate of zero is no change in speed at all. The fastest rate is two
changes per second. All changes are gradual and "rounded"; as a result,
the periodic "points" of change are not noticeable. What is heard is a
kind of "average random rate" of change.

4) Random Volume Change: changes of volume for the four soundfiles are
independent. Particularly important: the AMOUNT of change (up to 100%)
is DOWNWARD from (or below) maximum volume for each file.

5) Random Pitch Change: random pitch variation up to 10% above AND
BELOW the original pitch.

6) Random Filter Peak (Resonance): variation in the center frequency
strength of the filter. A higher peak concentrates the sound around the
central filter frequency. Zero represents minimum filtering and a sound
closest to the original.

7) Random Filter Frequency: variation AROUND the center point of the
filter (both up and down). Works in conjunction with #8.

8) Filter (center point) Shift: this is NOT a random variation. The
center point of the filter is moved up or down by a fixed amount. Works
in conjunction with #7.

9) Fade In/Out Duration: duration of initial fadein and final fadeout.
These durations are included in Total Duration (below). Positive
numbers are SECONDS, negative numbers are MINUTES. Range: 0 seconds to
10 minutes.

10) Total Duration: self-explanatory. All files begin and end at the
same time (though they start at different locations within; see below).
Positive numbers indicate MINUTES, negative numbers are HOURS. 0 = 30
seconds. Range: 30 seconds to 24 hours. Though the performance will
conclude at the time specified, it can always be halted sooner by
hitting STOP (in which case, of course, there is no final fade). When a
performance concludes naturally, the START button immediately
reappears.

Note: Every file begins from a different random position each time a
performance is started.

Additional observation: Although the controllers display only integer
values, the buttons may be clicked and decimal - or other alternate
numbers - inserted. (This may be particularly appropriate for Total
Duration.) Upon hitting START, the display returns to the closest
integer, but the chosen value will remain until changed.


No Sound - Sample Rate Issues

On a few systems, e.g. the Intel Classmate PC, the specified sr
(sample rate) of 44100 may not produce audio. Substitute a rate of
48000 (or, if necessary, 32000) toward the beginning of the
FileMixAuto.csd file, using a text editor.


Audio Glitching/Breakup

If you get audio glitching, open Sugar's Control Panel, and turn off
Extreme power management (under Power) or Wireless radio (under
Network). Stereo headphones (an inexpensive set will work fine) or
external amplifier/speaker system are highly recommended.


Resizing the Font

The font display of this activity can be resized in csndsugui.py,
using any text editor. Further instructions are found toward the
beginning of csndsugui.py. (Simply change the value of the "resize"
variable (= 0), plus or minus.)


