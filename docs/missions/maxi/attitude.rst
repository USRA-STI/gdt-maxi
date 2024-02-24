.. _maxi-attitude:
.. |MaxiAttitude| replace:: :class:`~gdt.missions.maxi.attitude.MaxiAttitude`
.. |MaxiFrame| replace:: :class:`~gdt.missions.maxi.frame.MaxiFrame`

*******************************************************
MAXI Attitude Files (:mod:`gdt.missions.maxi.attitude`)
*******************************************************

The MAXI mission provides attitude files that specify the orientation of MAXI
relative to the J2000 frame that is sampled at an approximate 1-s cadence over
a day. We can open these files using the |MaxiAttitude| class and extract the
frame information from them.

For example we can read the example attitude file that is in the testing/example
data:

    >>> from gdt.core import data_path
    >>> from gdt.missions.maxi.attitude import MaxiAttitude
    >>> att_file = data_path / 'maxi-gsc/mx_mjd58849.att.gz'
    >>> att = MaxiAttitude.open(att_file)
    >>> att
    <MaxiAttitude(filename="mx_mjd58849.att.gz") at 0x103afafa0>

To extract the MAXI frame, we do the following:

    >>> frame = att.get_spacecraft_frame()
    >>> frame
    <MaxiFrame: 86401 frames;
     obstime=[631152082.011275, ...]
     quaternion=[(x, y, z, w) [ 0.76156184, -0.55583739,  0.14661502, -0.29928647], ...]>

Notice that this |MaxiFrame| object contains 86401 different frames, each 
defined at a particular ``obstime`` and with a quaternion defining the rotation 
between the MAXI frame and the J2000 frame. We can use this frame to do all of
the things described in :ref:`MAXI Reference Frame<maxi-frame>`.  For example,
if we create an Astropy SkyCoord of an object on the sky, we can rotate it into
each of the MAXI frames.

    >>> from astropy.coordinates import SkyCoord
    >>> coord = SkyCoord(100.0, -30.0, unit='deg')
    >>> maxi_coords = coord.transform_to(frame)
    >>> (maxi_coords.az, maxi_coords.el)
    <Longitude [162.47630661, 162.46212383, 162.44592815, ...,  28.67196423,
                  28.68926214,  28.70586066] deg>,
     <Latitude [ 33.71676537,  33.77730426,  33.83788703, ..., -32.13139582,
                -32.18918228, -32.2475741 ] deg>)

Or we can go in the other direction, and convert a MAXI coordinate into the 
celestial frame:

    >>> maxi_coord = SkyCoord(50.0, 25.0, frame=frame, unit='deg')
    >>> # convert to the Galactic frame
    >>> maxi_coord.galactic
    <SkyCoord (Galactic): (l, b) in deg
        [(335.29677607, -10.47592442), (335.26120761, -10.50898651),
         (335.22413471, -10.54205297), ..., (240.98969174,  45.17289394),
         (240.99658923,  45.22071526), (241.00427102,  45.26932204)]>

We can also extract a single frame or slice multiple frames:

    >>> frame[100]
    <MaxiFrame: 1 frames;
     obstime=[631152182.0114429]
     obsgeoloc=[(0., 0., 0.) m]
     obsgeovel=[(0., 0., 0.) m / s]
     quaternion=[(x, y, z, w) [ 0.7679603 , -0.53712165,  0.10544197, -0.33259481]]>

    >>> frame[100:110]
    <MaxiFrame: 10 frames;
     obstime=[631152182.0114429, ...]
     quaternion=[(x, y, z, w) [ 0.7679603 , -0.53712165,  0.10544197, -0.33259481], ...]>

Note that the attitude file contains *only* the attitude information, and there
is no positional information, which is contained within the orbit file and is 
discussed further in :ref:`MAXI Orbit Files<maxi-orbit>`. 
See :ref:`MAXI Reference Frame<maxi-frame-combine>` for information about how 
to combine the attitude and orbit information into a single |MaxiFrame| object.

For more details about working with spacecraft frames, see 
:external:ref:`Spacecraft Attitude, Position, and Coordinates<core-coords>`.

Reference/API
=============

.. automodapi:: gdt.missions.maxi.attitude
   :inherited-members:


