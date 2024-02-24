.. _maxi-finders:
.. |MaxiAuxilFinder| replace:: :class:`~gdt.missions.maxi.finders.MaxiAuxilFinder`

************************************************************
MAXI Data Finders (:mod:`gdt.missions.maxi.finders`)
************************************************************
MAXI Data is hosted publicly at the High Energy Astrophysics Science Archive 
Research Center (HEASARC) on a FTP server. But instead of having to navigate a
winding maze of FTP directories, we provide some classes built to retrieve the 
data you want.

.. _maxi-finders-aux:
Finding Auxiliary MAXI data
===========================
MAXI provides mission-level non-science data (auxiliary) that are broadly 
useful. There are attitude and orbit files that contain information about
the orientation of MAXI and its position in orbit, respectively.  There are 
also Good-Time-Interval (GTI) files available that mark the segments of time
that contain good data.

To retrieve auxiliary files for a given day, we use the |MaxiAuxilFinder| class
and initialize it with an Astropy Time object:

    >>> from gdt.missions.maxi.finders import MaxiAuxilFinder
    >>> from gdt.missions.maxi.time import Time
    >>> time = Time('2020-01-01 12:00:00', format='iso', scale='utc')
    >>> auxil_finder = MaxiAuxilFinder(time)
    >>> auxil_finder
    <MaxiAuxilFinder: 2020-01-01 12:00:00.000>
    >>> auxil_finder.num_files
    46

We can list the attitude and orbit files available:

    >>> auxil_finder.ls_attitude()
    ['mx_mjd58849.att.gz']
    >>> auxil_finder.ls_orbit()
    ['mx_mjd58849.orb.gz']

And we can list the GTI files available (there are GTI files for the low 
bitrate and medium bitrate data):

    >>> auxil_finder.ls_gti_low()
    ['mx_mjd58849_gsc0_low.gti.gz',
     'mx_mjd58849_gsc1_low.gti.gz',
     'mx_mjd58849_gsc2_low.gti.gz',
     'mx_mjd58849_gsc3_low.gti.gz',
     'mx_mjd58849_gsc4_low.gti.gz',
     'mx_mjd58849_gsc5_low.gti.gz',
     'mx_mjd58849_gsc6_low.gti.gz',
     'mx_mjd58849_gsc7_low.gti.gz',
     'mx_mjd58849_gsc8_low.gti.gz',
     'mx_mjd58849_gsc9_low.gti.gz',
     'mx_mjd58849_gsca_low.gti.gz',
     'mx_mjd58849_gscb_low.gti.gz']

This list includes a GTI file for each GSC detector.

We can also change to another directory by specifying a new time:

    >>> new_time =  Time('2022-10-09 12:00:00', format='iso', scale='utc')
    >>> auxil_finder.cd(new_time)
    >>> auxil_finder
    <MaxiAuxilFinder: 2022-10-09 12:00:00.000>

Now we can download the orbit file for this day:

    >>> auxil_finder.get_orbit('.', verbose=True)
    mx_mjd59861.orb.gz ━━━━━━━━━━━━━━━━━━━━ 100.0% • 8.1/8.1 MB • 4.2 MB/s • 0:00:00

We can also download the GTI files, but we can choose which detectors to download
based on the detector number:

    >>> # download GTI for gsc3 and gsc7
    >>> auxil_finder.get_gti_low('.', dets=[3, 7], verbose=True)
    mx_mjd59861_gsc3_low.gti.gz ━━━━━━━━━━━━━━━━━━ 100.0% • 3.2/3.2 kB • ? • 0:00:00
    mx_mjd59861_gsc7_low.gti.gz ━━━━━━━━━━━━━━━━━━ 100.0% • 3.2/3.2 kB • ? • 0:00:00


See :external:ref:`The FtpFinder Class<core-heasarc-finder>` for more details 
on using data finders, and continue on to 
:ref:`MAXI/GSC Data Finders<gsc-finders>` for details on how to find and 
download GSC science data.

Reference/API
=============

.. automodapi:: gdt.missions.maxi.finders
   :inherited-members:


