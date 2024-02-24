.. _gsc-finders:
.. |GscEventsFinder| replace:: :class:`~gdt.missions.maxi.gsc.finders.GscEventsFinder`

************************************************************
MAXI/GSC Data Finders (:mod:`gdt.missions.maxi.gsc.finders`)
************************************************************
MAXI Data is hosted publicly at the High Energy Astrophysics Science Archive 
Research Center (HEASARC) on a FTP server. But instead of having to navigate a
winding maze of FTP directories, we provide some classes built to retrieve the 
data you want.

Finding GSC Event Data
===========================
MAXI/GSC provides science data event lists for all observations and are 
organized as daily files and divided into 768 files (at most) representing the
photons originating from a HEALPixel with resolution NSIDE=8.  The events are
also provided at low and medium bitrates.

To retrieve GSC event files for a given day, we use the |GscEventsFinder| class
and initialize it with an Astropy Time object and either "low" or "med" for 
which bitrate we are interested in:

    >>> from gdt.missions.maxi.gsc.finders import GscEventsFinder
    >>> from gdt.missions.maxi.time import Time
    >>> time = Time('2020-01-01 12:00:00', format='iso', scale='utc')
    >>> gsc_finder = GscEventsFinder(time, 'low')
    >>> gsc_finder
    <GscEventsFinder: 2020-01-01 12:00:00.000, low>
    >>> gsc_finder.num_files
    750

Notice that even though the file indexing is by HEALPix index, not all 768 
indices are used.  This can happen if GSC did not observed the part of the 
sky covered by a HEALPixel during that day.

We can list the event files available:

    >>> gsc_finder.ls_event()
    ['mx_mjd58849_gsc_low_000.evt.gz',
     'mx_mjd58849_gsc_low_001.evt.gz',
     'mx_mjd58849_gsc_low_002.evt.gz',
     'mx_mjd58849_gsc_low_003.evt.gz',
     'mx_mjd58849_gsc_low_004.evt.gz',
     ...
     'mx_mjd58849_gsc_low_763.evt.gz',
     'mx_mjd58849_gsc_low_764.evt.gz',
     'mx_mjd58849_gsc_low_765.evt.gz',
     'mx_mjd58849_gsc_low_766.evt.gz',
     'mx_mjd58849_gsc_low_767.evt.gz']


We can also change to another directory by specifying a new time (and bitrate):

    >>> new_time =  Time('2022-10-09 12:00:00', format='iso', scale='utc')
    >>> gsc_finder.cd(new_time, 'med')
    >>> gsc_finder
    <GscEventsFinder: 2022-10-09 12:00:00.000, med>

Now we can download some event files.  We can download all event files, or we
can choose to download certain event files based on their HEALPix index:

    >>> # download events for pixels 33 and 34
    >>> gsc_finder.get_event('.', pixels=[33, 34], verbose=True)
    mx_mjd59861_gsc_med_033.evt.gz ━━━━━━━━━ 100.0% • 461.5/46… • 1.4 MB/s • 0:00:00
                                                      kB                            
    mx_mjd59861_gsc_med_034.evt.gz ━━━━━━━━━ 100.0% • 536.3/5… • 552.1     • 0:00:00
                                                      kB         kB/s               


See :external:ref:`The FtpFinder Class<core-heasarc-finder>` for more details 
on using data finders, and see 
:ref:`Finding Auxiliary MAXI datas<maxi-finders-aux>` for details on how to 
find and download MAXI orbit, attitude, and GTI files.

Reference/API
=============

.. automodapi:: gdt.missions.maxi.gsc.finders
   :inherited-members:


