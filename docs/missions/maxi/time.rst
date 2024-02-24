.. _maxi-time:

***************************************************
MAXI Mission Epoch  (:mod:`gdt.missions.maxi.time`)
***************************************************

The MAXI Mission time is typically expressed as the number of seconds elapsed
since January 1, 2000 00:00:00 UTC in the Terrestrial Time scale. We have 
defined a specialized epoch to work with Astropy ``Time`` objects so that the 
MAXI mission time can be easily converted to/from other formats and time scales.

To use this, we simply import and create an astropy Time object with a `'maxi'`
format:

    >>> from gdt.missions.maxi.time import Time
    >>> maxi_met = Time(556288865.0, format='maxi')
    >>> maxi_met
    <Time object: scale='tt' format='maxi' value=556288865.0>
    
Now, say we want to retrieve the GPS timestamp:

    >>> maxi_met.gps
    1187008878.0

The Astropy ``Time`` object readily converts it for us. We can also do the 
reverse conversion:

    >>> gps_time = Time(maxi_met.gps, format='gps')
    >>> gps_time
    <Time object: scale='tai' format='gps' value=1187008878.0>
    
    >>> gps_time.maxi
    556288865.0

And we should, of course, get back the MAXI mission time we started with.  
This enables you do do any time conversions already provided by Astropy, as 
well as time conversions between other missions within the GDT.

In addition to time conversions, all time formatting available in Astropy is 
also available here.  For example, we can format the MAXI mission time in ISO 
format:

    >>> maxi_met.iso
    '2017-08-17 12:42:09.184'

    
Reference/API
=============

.. automodapi:: gdt.missions.maxi.time
   :inherited-members:


