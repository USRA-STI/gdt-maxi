.. _maxi-orbit:
.. |MaxiOrbit| replace:: :class:`~gdt.missions.maxi.orbit.MaxiOrbit`
.. |MaxiFrame| replace:: :class:`~gdt.missions.maxi.frame.MaxiFrame`

**************************************************************
MAXI Orbit Files (:mod:`gdt.missions.maxi.orbit`)
**************************************************************

The MAXI mission provides orbit files that specify the position and velocity of 
the ISS (and hence MAXI) in orbit at an approximate 1-s cadence over a day. We 
can open these files using the |MaxiOrbit| class and extract the orbit 
information from them.

For example we can read the example orbit file that is in the testing/example
data:

    >>> from gdt.core import data_path
    >>> from gdt.missions.maxi.orbit import MaxiOrbit
    >>> orb_file = data_path / 'maxi-gsc/mx_mjd58849.orb.gz'
    >>> orb = MaxiOrbit.open(orb_file)
    >>> orb
    <MaxiOrbit(filename="mx_mjd58849.orb.gz") at 0x102e1fd30>

To extract the orbit information into a MAXI frame, we do the following:

    >>> frame = orb.get_spacecraft_frame()
    >>> frame
    <MaxiFrame: 86362 frames;
     obstime=[631152006.0929999, ...]
     obsgeoloc=[(-3988969.7208, -1428272.8356, 5300477.4864) m, ...]
     obsgeovel=[(-7318.41587813, -498.94788896, -600.77996162) m / s, ...]
    >

Notice that this |MaxiFrame| object contains 86362 different frames, each 
defined at a particular ``obstime`` and with a ``obsgeoloc`` defining the 
position of MAXI in orbit and a ``obsgeovel`` defining the orbital velocity.

Using these frames, we can retrieve the location of MAXI in orbit relative to 
the geocenter:

    >>> # latitude
    >>> frame.earth_location.lat
    <Latitude [ 51.43604804,  51.42789274,  51.41964168, ..., -51.17471138,
               -51.16413275, -51.15346404] deg>
    >>> # longitude
    >>> frame.earth_location.lon
    <Longitude [ 99.7838931 ,  99.88232441,  99.98072336, ..., -83.292815  ,
                -83.19609091, -83.09941138] deg>
    >>> # altitude
    >>> frame.earth_location.height
    <Quantity [420683.68471216, 420683.01131551, 420681.40903219, ...,
               439028.5961116 , 439024.11948029, 439019.11857587] m>

We can also extract a single frame or slice multiple frames:

    >>> frame[100]
    <MaxiFrame: 1 frames;
     obstime=[631152106.0929999]
     obsgeoloc=[(-3779109.7392, -2159243.586, 5206397.3088) m]
     obsgeovel=[(-7191.26129531, -919.02691758, -1270.66417031) m / s]
     quaternion=[None]>

    >>> frame[100:110]
    <MaxiFrame: 10 frames;
     obstime=[631152106.0929999, ...]
     obsgeoloc=[(-3779109.7392, -2159243.586, 5206397.3088) m, ...]
     obsgeovel=[(-7191.26129531, -919.02691758, -1270.66417031) m / s, ...]
    >

Note that the orbit file contains *only* the orbit information, and there
is no attitude information, which is contained within the attitude file and is 
discussed further in :ref:`MAXI Attitude Files<maxi-attitude>`. 
See :ref:`MAXI Reference Frame<maxi-frame-combine>` for information about how 
to combine the attitude and orbit information into a single |MaxiFrame| object.

For more details about working with spacecraft frames, see 
:external:ref:`Spacecraft Attitude, Position, and Coordinates<core-coords>`.

Reference/API
=============

.. automodapi:: gdt.missions.maxi.orbit
   :inherited-members:


