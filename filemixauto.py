# FILEMIXAUTO - Audio File Looper/Mixer/Processor for Children (2011)
# Art Hunkins (www.arthunkins.com)
#   
#    FileMixAuto is licensed under the Creative Commons Attribution-Share
#    Alike 3.0 Unported License. To view a copy of this license, visit
#    http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to
#    Creative Commons, 171 Second Street, Suite 300, San Francisco,
#    California, 94105, USA.
#
#    It is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# version 5  Changes:
#    GUI tweaks


import csndsugui
import gobject
from sugar.activity import activity
from sugar.graphics.objectchooser import ObjectChooser
from sugar import mime
import gtk
import os

class FileMixAuto(activity.Activity):

 def __init__(self, handle):
  
   activity.Activity.__init__(self, handle)

   red = (0xDDDD, 0, 0)
   brown = (0x6600, 0, 0)
   green = (0, 0x5500, 0)
   self.paths = ["0"]*5
   self.jobjects = [None]*5
   self.buts = [None]*5

   win = csndsugui.CsoundGUI(self)
   width = gtk.gdk.screen_width()
   height = gtk.gdk.screen_height()
   if os.path.exists("/etc/olpc-release") or os.path.exists("/sys/power/olpc-pm"):
     adjust = 78
   else:
     adjust = 57
   screen = win.box()
   screen.set_size_request(width, height - adjust)
   scrolled = gtk.ScrolledWindow()
   scrolled.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
   screen.pack_start(scrolled)
   all = gtk.VBox()
   all.show()
   scrolled.add_with_viewport(all)
   scrolled.show()

   win.text("<big><b><big><u>FILEMIXAUTO</u> - Audio File Looper/Mixer/Processor \
for Children (2011)</big></b>\n\
\t\t\t\t    Art Hunkins (www.arthunkins.com)</big>", all)

   win.text("Loop and process 1 to 4 mono/stereo files; \
wav and ogg vorbis formats only (no ogg vorbis on Sugar 0.84).\n\
  User sound files must be placed in Journal (Record activity \
does this). <b>No user files on Sugar 0.82</b> (original XO-1).\n\
  The default files are abbreviated versions of those from the author's \
<b>DUSK AT ST. FRANCIS SPRINGS</b>.\n\
You are urged to create your own sound files suitable for looping, for example, \
with the Record activity - \n  especially nature soundscapes - to set a mood \
or accompany movement, drama, pantomime, etc.", all, brown)

   self.b2box = win.box(False, all)
   bbox = win.box(False, all)
   self.bb = bbox
   self.w = win
   self.r = red
   self.g = green
   self.br = brown
   self.p = False

   try:
     from jarabe import config
     version = [int(i) for i in config.version.split('.')][:2]
   except ImportError:
     version = [0, 82]
   if version >= [0, 84]:
     boxa = win.box(False, self.b2box)
     boxb = win.box(False, self.b2box)
     boxc = win.box(True, boxb)
     self.boxd = win.box(False, boxc)
     boxe = win.box(True, boxc)
     win.text("\t\tOptionally, select your own <b>audio</b> file(s) from the Journal.\n\
\t\tDeselect a file by choosing another, or by closing Journal.\n\
\t\tCreate your files with Record or Audacity (see ReadMe.txt).\t   ", boxa, green)
     win.text("Select File(s):", self.boxd, brown)
     for i in range(1, 5):
       self.buts[i] = win.cbbutton(self.boxd, self.choose, " %d " %i)
       self.buts[i].modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0x6600, 0, 0))
     but = win.cbbutton(boxe, self.auto, " CLICK when selections made ")
     but.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0x7700, 0))
     but.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0, 0x7700, 0))
   else:
     self.auto(self)

 def choose(self, widget):
   chooser = ObjectChooser(parent=self, what_filter=mime.GENERIC_TYPE_AUDIO)
   result = chooser.run()
   index = self.boxd.child_get_property(widget, "position")
   if result == gtk.RESPONSE_ACCEPT:
     self.jobjects[index] = chooser.get_selected_object()
     self.paths[index] = str(self.jobjects[index].get_file_path())
     self.buts[index].modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0x8800, 0))
     self.buts[index].modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0, 0x8800, 0))
   else:
     self.paths[index] = "0"
     self.jobjects[index] = None
     self.buts[index].modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0x6600, 0, 0))
     self.buts[index].modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0x6600, 0, 0))

 def send_data(self):
   for i in range(1, 5):
     self.w.set_filechannel("file%d" % i, self.paths[i])

 def playcsd(self, widget):
   def start(self):
     self.p = True
     self.w.play()
     gobject.timeout_add(500, checkstat)
     self.but.child.set_label("STOP !")
     self.but.child.set_use_markup(True)
     self.but.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0xFFFF, 0, 0))
     self.but.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0xFFFF, 0, 0))
   def stop(self):
     self.p = False
     self.w.recompile()
     self.w.channels_reinit()
     self.send_data()
     self.but.child.set_label("START !")
     self.but.child.set_use_markup(True)
     self.but.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0x7700, 0))
     self.but.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0, 0x7700, 0))
   def checkstat():
     if self.w.perf.GetStatus() == 2:
       stop(self)
     return True
   if self.p == False:
     start(self)
   else:
     stop(self)
 
 def auto(self, widget):
   self.b2box.destroy()
   self.box1 = self.w.box(True, self.bb)
   self.w.text("       ", self.box1)
   self.box2 = self.w.box(True, self.bb)
   self.f = self.w.framebox(" <b>FileMixAuto</b> - <i>Select Options First</i> ",\
False, self.box2, self.r)
   self.b1 = self.w.box(True, self.f)
   self.b2 = self.w.box(True, self.f)
   self.b3 = self.w.box(True, self.f)
   self.b4 = self.w.box(True, self.f)
   self.b5 = self.w.box(True, self.f)
   self.b6 = self.w.box(True, self.f)
   self.b7 = self.w.box(True, self.f)
   self.w.csd("FileMixAuto.csd")
   self.w.spin(4, 1, 4, 1, 1, self.b1, 0, "Files", "# of Files")
   self.w.spin(0, 0, 50, 1, 5, self.b1, 0, "RandRate", "Random Rate\n\
[0=no change]")
   self.w.spin(10, 0, 10, 1, 1, self.b2, 0, "MaxVol1", "Max Vol/File1 ")
   self.w.spin(10, 0, 10, 1, 1, self.b2, 0, "MaxVol2", "Max Vol/File2 \n\
   Random Vol") 
   self.w.spin(10, 0, 10, 1, 1, self.b3, 0, "MaxVol3", "Max Vol/File3 ")
   self.w.spin(10, 0, 10, 1, 1, self.b3, 0, "MaxVol4", " Max Vol/File4 \n\
is < Max Vol")
   self.w.spin(0, 0, 10, 1, 1, self.b4, 0, "RandVol", "Random Volume")
   self.w.spin(0, 0, 10, 1, 1, self.b4, 0, "RandPtch", "Random Pitch\n\
[+/- 10% max]")
   self.w.spin(0, 0, 10, 1, 1, self.b5, 0, "RandPeak", "Random Peak")
   self.w.spin(0, 0, 10, 1, 1, self.b5, 0, "RandFilt", "Random Filter")
   self.w.spin(0, -10, 10, 1, 1, self.b6, 0, "FiltShft", "Filter Center +/-")
   self.w.spin(5, -10, 60, 1, 10, self.b6, 0, "FadeDur", "   Fade Duration\n\
[+ = secs;- = mins]")
   self.dur = self.w.spin(1, -24, 60, 1, 10, self.b7, 0, "TotalDur",\
"  Total Duration\n[+ = mins;- = hrs;\n    0 = 30 secs]")
   self.send_data() 
   self.but = self.w.cbbutton(self.b7, self.playcsd, "START !")
   self.but.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0x7700, 0))
   self.but.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0, 0x7700, 0))

