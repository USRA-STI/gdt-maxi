.. _gsc-headers:

**************************************************************
MAXI/GSC FITS Headers (:mod:`gdt.missions.maxi.gsc.headers`)
**************************************************************
This module defines all of the FITS headers for the public data files. While
these classes are not usually directly called by the user, we may load one up
and see the contents and default values.  For example, here is the set of 
header definitions for the :ref:`event files<gsc-tte>`:

    >>> from gdt.missions.maxi.gsc.headers import EventsHeaders
    >>> hdrs = EventsHeaders()
    >>> hdrs
    <EventsHeaders: 3 headers>
    
Here is the ``PRIMARY`` header and default values (retrieved by index):

    >>> hdrs[0]
    TELESCOP= 'MAXI    '           / Mission name                                   
    INSTRUME= 'GSC     '           / Instrument name (GSC, SSC_H or SSC_Z)          
    GPCMOID = 'NA      '           / Gas Proportional Counter ID                    
    DATAMODE= '' / Data mode (32 or 64 BIT for GSC, STANDARD for S                  
    OBSERVER= 'MAXI Team'          / Principal Investigator                         
    NETWORKI= '' / Network interface (1553B/Ether)                                  
    FORMVER = '' / Event file format version                                        
    DATATYPE=                    0 / Data Type ID: Obs./Sim./Ground Cal.            
    DATAFORM=                    0 / Event Data Format ID                           
    DATE-OBS= '' / observation start date and time                                  
    TIME-OBS= '' / Start time                                                       
    DATE-END= '' / observation end date and time                                    
    TIME-END= '' / Stop time                                                        
    TSTART  =                  0.0 / time of first data                             
    TSTOP   =                  0.0 / time of last data                              
    TELAPSE =                  0.0 / TSTOP-TSTART                                   
    ONTIME  =                  0.0 / Actual time                                    
    RADECSYS= 'FK5     '           / World Coordinate System                        
    EQUINOX =               2000.0 / Equinox for coordinate system                  
    MJDREFI =                51544 / MJD reference day                              
    MJDREFF =  0.00074287037037037 / MJD reference (fraction of day)                
    TIMEREF = 'LOCAL   '           / reference time                                 
    TIMESYS = 'TT      '           / time measured from                             
    TIMEUNIT= 's       '           / unit for time keyword                          
    TIMEDEL =                  0.0 / Smallest time increment                        
    OBJECT  = '' / HEALPix tile number                                              
    RA_NOM  =                  0.0 / RA of the tile center [deg]                    
    DEC_NOM =                  0.0 / DEc of the tile center [deg]                   
    RADIUS_I=                  0.0 / inner radius for event extraction [degree]     
    RADIUS_O=                  0.0 / outer radius for event extraction [degree]     
    CREATOR = '' / Software                                                         
    USER    = '' / user name of the creator                                         
    ORIGIN  = 'ISAS/JAXA'          / Tape writing institution                       
    HPX_ORDR= 'RING    '           / HEALPIX order scheme (RING or NEST)            
    HPX_NSID=                    8 / HEALPIX nside                                  
    PROCVER = '' / Major.Minor.Tool.CALDB                                           
    SEQPNUM =                    1 / Number of the processing with this PROCVER     
    SOFTVER = '' / HEASOFT version                                                  
    CALDBVER= '' / CALDB version                                                    
    NEVENTS =                    0 / Number of events                               
    DETNAM  = '' / Detector                                                         
    EXPOSURE=                  0.0 / Exposure time                                  
    LIVETIME=                  0.0 / On-source time                                 
    MJD-OBS =                  0.0 / MJD of data start time                         
    TIMEZERO=                  0.0 / Time Zero                                      
    DATE    = '2024-02-22T21:55:28.225' / date of file creation (GMT)               

And here is the ``STDGTI`` header and default values:

    >>> hdrs['STDGTI']
    EXTNAME = 'STDGTI  '           / name of this binary table extension            
    HDUCLASS= 'OGIP    '           / Format conform to OGIP standard                
    HDUCLAS1= 'GTI     '           / File contains Good Time Intervals              
    HDUCLAS2= 'STANDARD'           / File contains Good Time Intervals              
    TELESCOP= 'MAXI    '           / Mission name                                   
    DATAMODE= '' / Data mode (32 or 64 BIT for GSC, STANDARD for S                  
    DETNAM  = '' / Detector                                                         
    INSTRUME= 'GSC     '           / Instrument name (GSC, SSC_H or SSC_Z)          
    OBJECT  = '' / HEALPix tile number                                              
    ONTIME  =                  0.0 / Actual time                                    
    EXPOSURE=                  0.0 / Exposure time                                  
    LIVETIME=                  0.0 / On-source time                                 
    DATE-OBS= '' / observation start date and time                                  
    TIME-OBS= '' / Start time                                                       
    DATE-END= '' / observation end date and time                                    
    TIME-END= '' / Stop time                                                        
    TSTART  =                  0.0 / time of first data                             
    TSTOP   =                  0.0 / time of last data                              
    TELAPSE =                  0.0 / TSTOP-TSTART                                   
    MJD-OBS =                  0.0 / MJD of data start time                         
    MJDREFI =                51544 / MJD reference day                              
    MJDREFF =  0.00074287037037037 / MJD reference (fraction of day)                
    TIMEREF = 'LOCAL   '           / reference time                                 
    TIMESYS = 'TT      '           / time measured from                             
    TIMEUNIT= 's       '           / unit for time keyword                          
    EQUINOX =               2000.0 / Equinox for coordinate system                  
    RADECSYS= 'FK5     '           / World Coordinate System                        
    USER    = '' / user name of the creator                                         
    FILIN001= '' / Input file name                                                  
    CREATOR = '' / Software                                                         
    ORIGIN  = 'ISAS/JAXA'          / Tape writing institution                       
    HDUNAME = 'STDGTI  '           / ASCDM block name                               
    MTYPE1  = 'TIME    '           / Data type                                      
    MFORM1  = 'START,STOP'         / names of the start and stop columns            
    METYP1  = 'R       '           / data descriptor type: Range, binned data       
    PROCVER = '' / Major.Minor.Tool.CALDB                                           
    CALDBVER= '' / CALDB version                                                    
    SOFTVER = '' / HEASOFT version                                                  
    SEQPNUM =                    1 / Number of the processing with this PROCVER     
    OBS_ID  = '' / Observation ID                                                   
    CLOCKAPP= 'T       '           / If clock correction are applied (F/T)          
    GPCMOID = 'NA      '           / Gas Proportional Counter ID                    
    OBSERVER= 'MAXI Team'          / Principal Investigator                         
    NETWORKI= '' / Network interface (1553B/Ether)                                  
    FORMVER = '' / Event file format version                                        
    DATATYPE=                    0 / Data Type ID: Obs./Sim./Ground Cal.            
    DATAFORM=                    0 / Event Data Format ID                           
    TIMEDEL =                  0.0 / Smallest time increment                        
    RA_NOM  =                  0.0 / RA of the tile center [deg]                    
    DEC_NOM =                  0.0 / DEc of the tile center [deg]                   
    RADIUS_I=                  0.0 / inner radius for event extraction [degree]     
    RADIUS_O=                  0.0 / outer radius for event extraction [degree]     
    HPX_ORDR= 'RING    '           / HEALPIX order scheme (RING or NEST)            
    HPX_NSID=                    8 / HEALPIX nside                                  
    DATE    = '2024-02-22T21:55:28.225' / date of file creation (GMT)               

See :external:ref:`Data File Headers<core-headers>` for more information about 
creating and using FITS headers.

Reference/API
=============

.. automodapi:: gdt.missions.maxi.gsc.headers
   :inherited-members:


