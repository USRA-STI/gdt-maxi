.. _gsc-detectors:
.. |GscDetectors| replace:: :class:`~gdt.missions.maxi.gsc.detectors.GscDetectors`
.. |GscFov| replace:: :class:`~gdt.missions.maxi.gsc.detectors.GscFov`
.. |Detectors| replace:: :class:`~gdt.core.detector.Detectors`

************************************************************************
MAXI/GSC Detector Definitions (:mod:`gdt.missions.maxi.gsc.detectors`)
************************************************************************

GSC Fields of View
==================

The |GscFov| class contains the naming and orientation of the two fields-of-view
(FOVs) of the the Gas-Slit Camera on-board MAXI.  In general, the two FOVs are 
oriented 90 degrees from one another and can be described as an approximated
rectangular box with a width of ~3 degrees and a length of ~160 degrees.  One
FOV is pointed in the direction of the ISS motion in orbit (the Horizontal, or 
GSC-H) and the other FOV is pointed at the zenith (GSC-Z). The naming, 
pointing, and bounding box of the FOV is contained within the |GscFov| class.

We can easily retrieve a FOV definition by using standard "dot" notation:

    >>> from gdt.missions.maxi.gsc.detectors import GscFov
    >>> GscFov.H
    <GscFov: H>

We can retrive the string name of the FOV:

    >>> GscFov.H
    'H'

As well as the full name of the FOV:

    >>> GscFov.H.full_name
    'GSC-H'

Since the |GscFov| class inherits from the |Detectors| base class, we 
can also retrieve the pointing information of the FOV in the MAXI frame:

    >>> # FOV azimuth, zenith
    >>> GscFov.from_str('Z').pointing()
    (<Quantity 0. deg>, <Quantity 180. deg>)
    
    >>> # detector elevation
    >>> GscFov.from_full_name('GSC-Z').elevation
    <Quantity -90. deg>


We can also retrieve the bounding box of the FOV:

    >>> GscFov.Z.fov
    [(268.5, 100.0), (91.5, 100.0), (88.5, 100.0), (271.5, 100.0), (268.5, 100.0)]


GSC PSPC Detectors
==================
Each GSC FOV is covered by 6 Position Sensitive Gas Proportional Counters 
(PSPCs), each of which are given names and produce data.  The |GscDetectors|
class tracks the information of these detectors in the same was as |GscFov| 
does for FOVs.  

To get a list of the GSC detectors, we can iterate over the |GscDetectors| 
class:

    >>> from gdt.missions.maxi.gsc.detectors import GscDetectors
    >>> print([detector.name for detector in GscDetectors])
    ['HA0', 'HA1', 'HA2', 'HB0', 'HB1', 'HB2', 'ZA0', 'ZA1', 'ZA2', 'ZB0', 'ZB1', 'ZB2']
    
And we can get the list of detectors that only belong the Horizontal FOV:

    >>> GscDetectors.h_detectors()
    [<GscDetectors: HA0>,
     <GscDetectors: HA1>,
     <GscDetectors: HA2>,
     <GscDetectors: HB0>,
     <GscDetectors: HB1>,
     <GscDetectors: HB2>]

And we can test if a particular detector is in the zenithal FOV:

    >>> print([det.is_z_detector() for det in GscDetectors])
    [False, False, False, False, False, False, True, True, True, True, True, True]


Reference/API
=============

.. automodapi:: gdt.missions.maxi.gsc.detectors
   :inherited-members:

