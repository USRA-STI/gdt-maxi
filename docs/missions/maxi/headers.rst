.. _maxi-headers:

****************************************************
MAXI FITS Headers (:mod:`gdt.missions.maxi.headers`)
****************************************************
This module defines all of the FITS headers for the public data files. While
these classes are not usually directly called by the user, we may load one up
and see the contents and default values.  For example, here is the set of 
header definitions for the :ref:`attitude files<maxi-attitude>`:

    >>> from gdt.missions.maxi.headers import AttitudeHeaders
    >>> hdrs = AttitudeHeaders()
    >>> hdrs
    <AttitudeHeaders: 2 headers>
    
Here is the ``PRIMARY`` header and default values (retrieved by index):

    >>> hdrs[0]
    TELESCOP= 'MAXI    '           / Mission name                                   
    ORIGIN  = 'ISAS/JAXA'          / Tape writing institution                       
    RADECSYS= 'FK5     '           / World Coordinate System                        
    EQUINOX =               2000.0 / Equinox for coordinate system                  
    MJDREFI =                51544 / MJD reference day                              
    MJDREFF =  0.00074287037037037 / MJD reference (fraction of day)                
    TIMEREF = 'LOCAL   '           / reference time                                 
    TIMESYS = 'TT      '           / time measured from                             
    TIMEUNIT= 's       '           / unit for time keyword                          
    DATE    = '2024-02-22T21:49:53.537' / date of file creation (GMT)               
    CREATOR = '' / Software                                                         

And here is the ``ATTITUDE`` header and default values:

    >>> hdrs['ATTITUDE']
    EXTNAME = 'ATTITUDE'           / name of this binary table extension            
    TELESCOP= 'MAXI    '           / Mission name                                   
    ORIGIN  = 'ISAS/JAXA'          / Tape writing institution                       
    RADECSYS= 'FK5     '           / World Coordinate System                        
    EQUINOX =               2000.0 / Equinox for coordinate system                  
    MJDREFI =                51544 / MJD reference day                              
    MJDREFF =  0.00074287037037037 / MJD reference (fraction of day)                
    TIMEREF = 'LOCAL   '           / reference time                                 
    TIMESYS = 'TT      '           / time measured from                             
    TIMEUNIT= 's       '           / unit for time keyword                          
    DATE    = '2024-02-22T21:49:53.537' / date of file creation (GMT)               
    CREATOR = '' / Software                                                         
    TSTART  =                  0.0 / time of first data                             
    TSTOP   =                  0.0 / time of last data                              
    DATE-OBS= '' / observation start date and time                                  
    DATE-END= '' / observation end date and time                                    
    PROCVER = '' / Major.Minor.Tool.CALDB                                           

See :external:ref:`Data File Headers<core-headers>` for more information about 
creating and using FITS headers.
    
Reference/API
=============

.. automodapi:: gdt.missions.maxi.headers
   :inherited-members:


