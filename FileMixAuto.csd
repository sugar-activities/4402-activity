; FileMixAuto (2011) for realtime Csound5 - by Arthur B. Hunkins
;  1-4 (user) soundfiles suitable for looping. Files may be mono or stereo;
;   can have different sample rates, may be a variety of different types
;   including WAV and AIFF; also Ogg/Vorbis (with Sugar 0.86/Blueberry or
;   later, or Sugar 0.84/Strawberry with updated libsndfile) but not MP3.
;  They must be named soundin.1 (through soundin.4), and in the same folder as this file,
;   or they may be loaded through the Journal (with Sugar 0.84/Strawberry or later).
;  Default soundfiles are the same as those in FileMix.

<CsoundSynthesizer>
<CsOptions>

-odac -+rtaudio=alsa -m0d --expression-opt -b128 -B2048

</CsOptions>
<CsInstruments>

sr      = 44100
; change sample rate to 48000 (or 32000 if necessary) when 44100 gives no audio.
; (Necessary for Intel Classmate PC and some other systems.)
ksmps   = 100
nchnls  = 2

        seed    0
ga1     init    0
ga2     init    0
gktrig  init    0
        
gitemp  ftgen   2, 0, 512, -5, 200, 512, sr / 13.2

gifiles    chnexport "Files", 1
gimaxvol1  chnexport "MaxVol1", 1
gimaxvol2  chnexport "MaxVol2", 1
gimaxvol3  chnexport "MaxVol3", 1
gimaxvol4  chnexport "MaxVol4", 1
girandrate chnexport "RandRate", 1
girandvol  chnexport "RandVol", 1
girandptch chnexport "RandPtch", 1
girandpeak chnexport "RandPeak", 1
girandfilt chnexport "RandFilt", 1
gifiltshft chnexport "FiltShft", 1
gifadedur  chnexport "FadeDur", 1
gitotaldur chnexport "TotalDur", 1

        instr 1
        
gimvol1 =       gimaxvol1 * .1
gimvol2 =       gimaxvol2 * .1
gimvol3 =       gimaxvol3 * .1
gimvol4 =       gimaxvol4 * .1
girrate =       girandrate * .01
girvol  =       girandvol * .1
girptch =       girandptch * .01
girpeak =       girandpeak * .1
girfilt =       girandfilt * .1
gifshft =       gifiltshft * .1
gifade  =       gifadedur
        if gifade > 0 igoto skip
gifade  =       abs(gifade) * 60      
gifade  =       (gifade == 0? .01: gifade)
skip:
gitotal =       gitotaldur * 60
        if gitotal > 0 igoto skip2
gitotal =       abs(gitotal) * 60      
gitotal =       (gitotal == 0? 30: gitotal)
skip2:
        event_i "i", 2, 0, gitotal
        tabw_i  gimvol1, 0, 3
        event_i "i", 6, 0, gitotal
        if gifiles == 1 igoto fin
        event_i "i", 3, 0, gitotal
        tabw_i  gimvol2, 1, 3
        if gifiles == 2 igoto fin
        event_i "i", 4, 0, gitotal
        tabw_i  gimvol3, 2, 3
        if gifiles == 3 igoto fin
        event_i "i", 5, 0, gitotal
        tabw_i  gimvol4, 3, 3
fin:
        endin        

        instr 2, 3, 4, 5

        if p1 != 2 goto cont
Sname	chnget	"file1"
i1      strcmp  Sname, "0"
        if i1 != 0 goto cont2
Sname   =       "soundin.1"
        goto cont2
cont:
        if p1 != 3 goto cont3
Sname	chnget	"file2"
i1      strcmp  Sname, "0"
        if i1 != 0 goto cont2
Sname   =       "soundin.2"
        goto cont2
cont3:
        if p1 != 4 goto cont4
Sname	chnget	"file3"
i1      strcmp  Sname, "0"
        if i1 != 0 goto cont2
Sname   =       "soundin.3"
        goto cont2
cont4:                
Sname	chnget	"file4"
i1      strcmp  Sname, "0"
        if i1 != 0 goto cont2
Sname   =       "soundin.4"
cont2:                
iamp    tab_i   p1 - 2, 3
        if girrate > 0 goto skip
kamp2   =       iamp
        goto skip2
skip:
kamp    rspline iamp - (iamp * girvol), iamp, girrate, girrate
kamp2   table   kamp * 512, 1
kamp2   port    kamp2, .01
skip2:
ichans  filenchnls Sname
ilen    filelen Sname
ipeak   filepeak Sname
imult   =       32760 / gifiles / ipeak
kamp2   =       kamp2 * imult
irand   unirand ilen * .75
        if girrate > 0 goto skip3
kbase   =       1
        goto skip4
skip3:
kbase   rspline girptch, -girptch, girrate, girrate
kbase   port    1 + kbase, .01
skip4:
        if ichans == 2 goto skip5
a1      diskin2 Sname, kbase, irand, 1
        goto skip6
skip5:        
a1, a2  diskin2 Sname, kbase, irand, 1
skip6:
        if girrate > 0 goto skip7
kfreq   =       0
        goto skip8
skip7:
kfreq   rspline (-256 * girfilt) + (gifshft * 255), (255 * girfilt) + (gifshft * 254), girrate, girrate   
        if kfreq < 255 goto skip9
kfreq   =       255
        goto skip8
skip9:
        if kfreq > -256 goto skip8
kfreq   =       -256
skip8:
kfreq   table   256 + kfreq, 2
kfreq   port    kfreq, .01
        if girrate > 0 goto skip10
kres    =       .25
        goto skip11
skip10:
kres    rspline 0, .45 * girpeak, girrate, girrate
kres    port    .25 + kres, .01
skip11:
a3,a4,a5 svfilter a1, kfreq, kres, 1
        if ichans == 1 goto skip12
a6,a7,a8 svfilter a2, kfreq, kres, 1
skip12:
kamp2   =       kamp2 + (kamp2 * 3 * (kres - .25))
ga1     =       ga1 + (a5 * kamp2)   
ga2     =       ga2 + ((ichans == 1? a5: a8) * kamp2)  

        endin
   
        instr 6

        if (gifade * 2) <= p3 goto skip
gifade  =       p3 * .5
skip:
kamp    linseg  0, gifade, 1, p3 - (gifade * 2) , 1, gifade, 0   
kamp2   table   kamp * 512, 1
kamp2   port    kamp2, .01
        outs    ga1 * kamp2, ga2 * kamp2
ga1     =       0
ga2     =       0

        endin

</CsInstruments>

<CsScore>

f 1 0 512 16 0 512 .8 1
f 3 0 4 -2 1 1 1 1
i 1 0 .01

e

</CsScore>
</CsoundSynthesizer>

