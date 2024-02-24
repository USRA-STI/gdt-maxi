.. _maxi-frame:
.. |MaxiFrame| replace:: :class:`~gdt.missions.maxi.frame.MaxiFrame`
.. |MaxiFrame.combine_orbit_attitude()| replace:: :meth:`MaxiFrame.combine_orbit_attitude()<gdt.missions.maxi.frame.MaxiFrame.combine_orbit_attitude>`
.. |MaxiAttitude| replace:: :class:`~gdt.missions.maxi.attitude.MaxiAttitude`
.. |MaxiOrbit| replace:: :class:`~gdt.missions.maxi.orbit.MaxiOrbit`
.. |Quaternion| replace:: :class:`~gdt.core.coords.Quaternion`

******************************************************
MAXI Reference Frame (:mod:`gdt.missions.maxi.frame`)
******************************************************

The MAXI reference frame, |MaxiFrame|, is the frame that is aligned
with the MAXI coordinate frame, and is represented by a quaternion that defines 
the rotation from MAXI coordinates to the ICRS coordinate frame.  This frame 
takes advantage of the Astropy coordinate frame design, so we can use the 
MaxiFrame to convert Astropy SkyCoord objects between the MAXI frame and any 
celestial frame.

Manually Initializing a Frame
=============================
While the |MaxiFrame| is typically initialized when reading from the attitude 
and orbit files (see |MaxiAttitude| and |MaxiOrbit|) instead of manually by a 
user, we can manually define the frame with a |Quaternion|:

    >>> from gdt.core.coords import Quaternion
    >>> from gdt.missions.maxi.frame import MaxiFrame
    >>> quat = Quaternion([-0.218,  0.009,  0.652, -0.726])
    >>> maxi_frame = MaxiFrame(quaternion=quat)
    >>> maxi_frame
    <MaxiFrame: 1 frames;
     obstime=[J2000.000]
     obsgeoloc=[(0., 0., 0.) m]
     obsgeovel=[(0., 0., 0.) m / s]
     quaternion=[(x, y, z, w) [-0.218,  0.009,  0.652, -0.726]]>

Notice that we can also define the frame with an ``obstime``, which is useful
for transforming between the MaxiFrame and a non-inertial time-dependent frame; 
an ``obsgeoloc``, which can define the spacecraft location in orbit; and
``obsgeovel``, which defines the spacecraft orbital velocity.

Now let us define a SkyCoord in RA and Dec:

    >>> from astropy.coordinates import SkyCoord
    >>> coord = SkyCoord(100.0, -30.0, unit='deg')
    
And we can simply rotate this into the MAXI frame with the following:
    
    >>> maxi_coord = coord.transform_to(maxi_frame)
    >>> (maxi_coord.az, maxi_coord.el)
    (<Longitude [200.39733555] deg>, <Latitude [-41.88750942] deg>)

We can also transform from the MAXI frame to other frames.  For example, we
define a coordinate in the MAXI frame this way:

    >>> maxi_coord = SkyCoord(50.0, 25.0, frame=maxi_frame, unit='deg')
    
Now we can tranform to ICRS coordinates:

    >>> maxi_coord.icrs
    <SkyCoord (ICRS): (ra, dec) in deg
        [(313.69000519, 26.89158349)]>

or Galactic coordinates:

    >>> maxi_coord.galactic
    <SkyCoord (Galactic): (l, b) in deg
        [(71.5141302, -11.56931006)]>
        
or any other coordinate frames provided by Astropy.

.. _maxi-frame-combine:
Combining Orbit and Attitude Frames
===================================
We typically won't manually create a |MaxiFrame| object, but rather these 
objects are a result of reading attitude and orbit files and extracting the
information from within those files.  More information about how to read those
ffiles can be found in :ref:`Maxi Attitude Files<maxi-attitude>` and 
:ref:`Maxi Orbit Files<maxi-orbit>`.  Because the frames from the attitude files
only contain attitude information and the frames from the orbit files only 
contain orbital information, it is often useful to combine that information into
a single frame (or set of frames), and this can be done with the 
|MaxiFrame.combine_orbit_attitude()| method.

Assuming we have two frames, ``att_frame`` and ``orb_frame`` that we have 
extracted from attitude and orbit files, respectively, we combine them into a
single frame in the following way:

    >>> # the MAXI attitude frame
    >>> att_frame
    <MaxiFrame: 86401 frames;
     obstime=[631152082.011275, ...]
     quaternion=[(x, y, z, w) [ 0.76156184, -0.55583739,  0.14661502, -0.29928647], ...]>

    >>> # the MAXI orbit frame
    >>> orb_frame
    <MaxiFrame: 86362 frames;
     obstime=[631152006.0929999, ...]
     obsgeoloc=[(-3988969.7208, -1428272.8356, 5300477.4864) m, ...]
     obsgeovel=[(-7318.41587813, -498.94788896, -600.77996162) m / s, ...]
    >

    >>> from gdt.missions.maxi.frame import MaxiFrame
    >>> combined_frame = MaxiFrame.combine_orbit_attitude(orb_frame, att_frame)
    >>> combined_frame
    <MaxiFrame: 86325 frames;
     obstime=[631152082.011275, ...]
     obsgeoloc=[(-3834147.96033173, -1985374.36954955, 5235177.78434637) m, ...]
     obsgeovel=[(-7229.7200539, -818.54642748, -1110.50065591) m / s, ...]
     quaternion=[(x, y, z, w) [ 0.76156184, -0.55583739,  0.14661502, -0.29928647], ...]>

One thing to notice is that the attitude and orbit |MaxiFrame| objects have a 
different number of sample frames and a different range of ``obstime`` even 
though they represent the MAXI attitude and orbital position for the same day.
This is because the attitude and orbit parameters are natively sampled at 
slightly different rates and phases. Therefore, when the 
|MaxiFrame.combine_orbit_attitude()| combines the two frames together, it
interpolates the attitude and orbit frames onto a common array of times that 
must span the *intersection* of the two time ranges.  By default, the sampling
period for the combined frame is 1 second, but this can be set with the
``sample_period`` keyword argument. 

Reference/API
=============

.. automodapi:: gdt.missions.maxi.frame
   :inherited-members:


