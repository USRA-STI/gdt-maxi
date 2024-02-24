# CONTAINS TECHNICAL DATA/COMPUTER SOFTWARE DELIVERED TO THE U.S. GOVERNMENT 
# WITH UNLIMITED RIGHTS
#
# Grant No.: 80NSSC21K0651
# Grantee Name: Universities Space Research Association
# Grantee Address: 425 3rd Street SW, Suite 950, Washington DC 20024
#
# Copyright 2024 by Universities Space Research Association (USRA). All rights 
# reserved.
#
# Developed by: Adam Goldstein
#               Universities Space Research Association
#               Science and Technology Institute
#               https://sti.usra.edu
#
# This work is a derivative of the Gamma-ray Data Tools (GDT), including the 
# Core and Fermi packages, originally developed by the following:
#
#     William Cleveland and Adam Goldstein
#     Universities Space Research Association
#     Science and Technology Institute
#     https://sti.usra.edu
#     
#     Daniel Kocevski
#     National Aeronautics and Space Administration (NASA)
#     Marshall Space Flight Center
#     Astrophysics Branch (ST-12)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not 
# use this file except in compliance with the License. You may obtain a copy of 
# the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the 
# License for the specific language governing permissions and limitations under 
# the License.

import unittest
from gdt.missions.maxi.gsc.headers import *


class TestArfHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = ArfHeaders()

    def test_primary(self):
        # nothing in this header
        hdr = self.headers[0]

    def test_HVB803(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'HVB803'
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'INSTRUME' in hdr.keys()
        assert 'HDUCLASS' in hdr.keys()
        assert hdr['HDUCLASS'] == 'OGIP'
        assert 'HDUCLAS1' in hdr.keys()
        assert hdr['HDUCLAS1'] == 'RESPONSE'
        assert 'HDUCLAS2' in hdr.keys()
        assert hdr['HDUCLAS2'] == 'SPECRESP'
        assert 'HDUVERS' in hdr.keys()
        assert 'VERSION' in hdr.keys()
        assert 'CCLS0001' in hdr.keys()
        assert hdr['CCLS0001'] == 'CPF'
        assert 'CCNM0001' in hdr.keys()
        assert hdr['CCNM0001'] == 'ARFCORR'
        assert 'CDTP0001' in hdr.keys()
        assert hdr['CDTP0001'] == 'DATA'
        assert 'CVSD0001' in hdr.keys()
        assert 'CDES0001' in hdr.keys()
        assert 'CBD10001' in hdr.keys()

    def test_HVB854(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'HVB854'
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'INSTRUME' in hdr.keys()
        assert 'HDUCLASS' in hdr.keys()
        assert hdr['HDUCLASS'] == 'OGIP'
        assert 'HDUCLAS1' in hdr.keys()
        assert hdr['HDUCLAS1'] == 'RESPONSE'
        assert 'HDUCLAS2' in hdr.keys()
        assert hdr['HDUCLAS2'] == 'SPECRESP'
        assert 'HDUVERS' in hdr.keys()
        assert 'VERSION' in hdr.keys()
        assert 'CCLS0001' in hdr.keys()
        assert hdr['CCLS0001'] == 'CPF'
        assert 'CCNM0001' in hdr.keys()
        assert hdr['CCNM0001'] == 'ARFCORR'
        assert 'CDTP0001' in hdr.keys()
        assert hdr['CDTP0001'] == 'DATA'
        assert 'CVSD0001' in hdr.keys()
        assert 'CDES0001' in hdr.keys()
        assert 'CBD10001' in hdr.keys()


class TestEventsHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = EventsHeaders()

    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'INSTRUME' in hdr.keys()
        assert 'GPCMOID' in hdr.keys()
        assert 'DATAMODE' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert 'NETWORKI' in hdr.keys()
        assert 'FORMVER' in hdr.keys()
        assert 'DATATYPE' in hdr.keys()
        assert 'DATAFORM' in hdr.keys()
        assert 'DATE-OBS' in hdr.keys()
        assert 'TIME-OBS' in hdr.keys()
        assert 'DATE-END' in hdr.keys()
        assert 'TIME-END' in hdr.keys()
        assert 'TSTART' in hdr.keys()
        assert 'TSTOP' in hdr.keys()
        assert 'TELAPSE' in hdr.keys()
        assert 'ONTIME' in hdr.keys()
        assert 'RADECSYS' in hdr.keys()
        assert hdr['RADECSYS'] == 'FK5'
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'MJDREFI' in hdr.keys()
        assert hdr['MJDREFI'] == 51544
        assert 'MJDREFF' in hdr.keys()
        assert hdr['MJDREFF'] == 0.00074287037037037
        assert 'TIMEREF' in hdr.keys()
        assert hdr['TIMEREF'] == 'LOCAL'
        assert 'TIMESYS' in hdr.keys()
        assert hdr['TIMESYS'] == 'TT'
        assert 'TIMEUNIT' in hdr.keys()
        assert hdr['TIMEUNIT'] == 's'
        assert 'TIMEDEL' in hdr.keys()
        assert 'OBJECT' in hdr.keys()
        assert 'RA_NOM' in hdr.keys()
        assert 'DEC_NOM' in hdr.keys()
        assert 'RADIUS_I' in hdr.keys()
        assert 'RADIUS_O' in hdr.keys()
        assert 'CREATOR' in hdr.keys()
        assert 'USER' in hdr.keys()
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'ISAS/JAXA'
        assert 'HPX_ORDR' in hdr.keys()
        assert 'HPX_NSID' in hdr.keys()
        assert 'PROCVER' in hdr.keys()
        assert 'SEQPNUM' in hdr.keys()
        assert 'SOFTVER' in hdr.keys()
        assert 'CALDBVER' in hdr.keys()
        assert 'NEVENTS' in hdr.keys()
        assert 'DETNAM' in hdr.keys()
        assert 'EXPOSURE' in hdr.keys()
        assert 'LIVETIME' in hdr.keys()
        assert 'MJD-OBS' in hdr.keys()
        assert 'TIMEZERO' in hdr.keys()
        assert 'DATE' in hdr.keys()

    def test_events(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'EVENTS'
        assert 'HDUCLASS' in hdr.keys()
        assert hdr['HDUCLASS'] == 'OGIP'
        assert 'HDUCLAS1' in hdr.keys()
        assert hdr['HDUCLAS1'] == 'EVENTS'
        assert 'CLOCKAPP' in hdr.keys()
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'INSTRUME' in hdr.keys()
        assert 'GPCMOID' in hdr.keys()
        assert 'DATAMODE' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert 'NETWORKI' in hdr.keys()
        assert 'FORMVER' in hdr.keys()
        assert 'DATATYPE' in hdr.keys()
        assert 'DATAFORM' in hdr.keys()
        assert 'DATE-OBS' in hdr.keys()
        assert 'TIME-OBS' in hdr.keys()
        assert 'DATE-END' in hdr.keys()
        assert 'TIME-END' in hdr.keys()
        assert 'TSTART' in hdr.keys()
        assert 'TSTOP' in hdr.keys()
        assert 'TELAPSE' in hdr.keys()
        assert 'ONTIME' in hdr.keys()
        assert 'RADECSYS' in hdr.keys()
        assert hdr['RADECSYS'] == 'FK5'
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'MJDREFI' in hdr.keys()
        assert hdr['MJDREFI'] == 51544
        assert 'MJDREFF' in hdr.keys()
        assert hdr['MJDREFF'] == 0.00074287037037037
        assert 'TIMEREF' in hdr.keys()
        assert hdr['TIMEREF'] == 'LOCAL'
        assert 'TIMESYS' in hdr.keys()
        assert hdr['TIMESYS'] == 'TT'
        assert 'TIMEUNIT' in hdr.keys()
        assert hdr['TIMEUNIT'] == 's'
        assert 'TIMEDEL' in hdr.keys()
        assert 'OBJECT' in hdr.keys()
        assert 'RA_NOM' in hdr.keys()
        assert 'DEC_NOM' in hdr.keys()
        assert 'RADIUS_I' in hdr.keys()
        assert 'RADIUS_O' in hdr.keys()
        assert 'CREATOR' in hdr.keys()
        assert 'USER' in hdr.keys()
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'ISAS/JAXA'
        assert 'HPX_ORDR' in hdr.keys()
        assert 'HPX_NSID' in hdr.keys()
        assert 'PROCVER' in hdr.keys()
        assert 'SEQPNUM' in hdr.keys()
        assert 'SOFTVER' in hdr.keys()
        assert 'CALDBVER' in hdr.keys()
        assert 'TIMEZERO' in hdr.keys()
        assert 'DETNAM' in hdr.keys()
        assert 'EXPOSURE' in hdr.keys()
        assert 'LIVETIME' in hdr.keys()
        assert 'MJD-OBS' in hdr.keys()
        assert 'FILIN001' in hdr.keys()
        assert 'NPIXSOU' in hdr.keys()
        assert 'OBS_ID' in hdr.keys()
        assert 'DATE' in hdr.keys()

    def test_stdgti(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'STDGTI'
        assert 'HDUCLASS' in hdr.keys()
        assert hdr['HDUCLASS'] == 'OGIP'
        assert 'HDUCLAS1' in hdr.keys()
        assert hdr['HDUCLAS1'] == 'GTI'
        assert 'HDUCLAS2' in hdr.keys()
        assert hdr['HDUCLAS2'] == 'STANDARD'
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'DATAMODE' in hdr.keys()
        assert 'DETNAM' in hdr.keys()
        assert 'INSTRUME' in hdr.keys()
        assert 'OBJECT' in hdr.keys()
        assert 'ONTIME' in hdr.keys()
        assert 'EXPOSURE' in hdr.keys()
        assert 'LIVETIME' in hdr.keys()
        assert 'DATE-OBS' in hdr.keys()
        assert 'TIME-OBS' in hdr.keys()
        assert 'DATE-END' in hdr.keys()
        assert 'TIME-END' in hdr.keys()
        assert 'TSTART' in hdr.keys()
        assert 'TSTOP' in hdr.keys()
        assert 'TELAPSE' in hdr.keys()
        assert 'MJD-OBS' in hdr.keys()
        assert 'MJDREFI' in hdr.keys()
        assert hdr['MJDREFI'] == 51544
        assert 'MJDREFF' in hdr.keys()
        assert hdr['MJDREFF'] == 0.00074287037037037
        assert 'TIMEREF' in hdr.keys()
        assert hdr['TIMEREF'] == 'LOCAL'
        assert 'TIMESYS' in hdr.keys()
        assert hdr['TIMESYS'] == 'TT'
        assert 'TIMEUNIT' in hdr.keys()
        assert hdr['TIMEUNIT'] == 's'
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'RADECSYS' in hdr.keys()
        assert hdr['RADECSYS'] == 'FK5'
        assert 'USER' in hdr.keys()
        assert 'FILIN001' in hdr.keys()        
        assert 'CREATOR' in hdr.keys()
        assert 'ORIGIN' in hdr.keys()
        assert 'HDUNAME' in hdr.keys()
        assert hdr['HDUNAME'] == 'STDGTI'
        assert 'MTYPE1' in hdr.keys()
        assert hdr['MTYPE1'] == 'TIME'
        assert 'MFORM1' in hdr.keys()
        assert hdr['MFORM1'] == 'START,STOP'
        assert 'METYP1' in hdr.keys()
        assert hdr['METYP1'] == 'R'
        assert 'PROCVER' in hdr.keys()
        assert 'CALDBVER' in hdr.keys()
        assert 'SOFTVER' in hdr.keys()
        assert 'SEQPNUM' in hdr.keys()
        assert 'OBS_ID' in hdr.keys()
        assert 'CLOCKAPP' in hdr.keys()
        assert 'GPCMOID' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert 'NETWORKI' in hdr.keys()
        assert 'FORMVER' in hdr.keys()
        assert 'DATATYPE' in hdr.keys()
        assert 'DATAFORM' in hdr.keys()
        assert 'TIMEDEL' in hdr.keys()
        assert 'RA_NOM' in hdr.keys()
        assert 'DEC_NOM' in hdr.keys()
        assert 'RADIUS_I' in hdr.keys()
        assert 'RADIUS_O' in hdr.keys()
        assert 'HPX_ORDR' in hdr.keys()
        assert 'HPX_NSID' in hdr.keys()
        assert 'DATE' in hdr.keys()


class TestRmfHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = RmfHeaders()

    def test_primary(self):
        hdr = self.headers[0]
        assert 'RMFTYPE' in hdr.keys()
        assert 'COL_THA' in hdr.keys()
        assert 'COL_PHI' in hdr.keys()
        assert 'DET_THA' in hdr.keys()
        assert 'DET_PHI' in hdr.keys()
        assert 'NUMDETX' in hdr.keys()
        assert 'DETXCNTR' in hdr.keys()
        assert 'DETXMIN' in hdr.keys()
        assert 'DETXMAX' in hdr.keys()
        assert 'NUMDETY' in hdr.keys()
        assert 'DETYCNTR' in hdr.keys()
        assert 'DETYMIN' in hdr.keys()
        assert 'DETYMAX' in hdr.keys()
        assert 'CONTENT' in hdr.keys()
        assert hdr['CONTENT'] == 'RESPONSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'ISAS/JAXA'
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'INSTRUME' in hdr.keys()
        assert 'DETNAM' in hdr.keys()
        assert 'DATE' in hdr.keys()

    def test_matrix(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'MATRIX'
        assert 'RMFTYPE' in hdr.keys()
        assert 'COL_THA' in hdr.keys()
        assert 'COL_PHI' in hdr.keys()
        assert 'DET_THA' in hdr.keys()
        assert 'DET_PHI' in hdr.keys()
        assert 'NUMDETX' in hdr.keys()
        assert 'DETXCNTR' in hdr.keys()
        assert 'DETXMIN' in hdr.keys()
        assert 'DETXMAX' in hdr.keys()
        assert 'NUMDETY' in hdr.keys()
        assert 'DETYCNTR' in hdr.keys()
        assert 'DETYMIN' in hdr.keys()
        assert 'DETYMAX' in hdr.keys()
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'INSTRUME' in hdr.keys()
        assert 'DETNAM' in hdr.keys()
        assert 'CHANTYPE' in hdr.keys()
        assert 'DETCHANS' in hdr.keys()
        assert 'HDUCLASS' in hdr.keys()
        assert hdr['HDUCLASS'] == 'OGIP'
        assert 'HDUCLAS1' in hdr.keys()
        assert hdr['HDUCLAS1'] == 'RESPONSE'
        assert 'HDUCLAS2' in hdr.keys()
        assert hdr['HDUCLAS2'] == 'RSP_MATRIX'
        assert 'HDUVERS' in hdr.keys()
        assert 'HDUCLAS3' in hdr.keys()
        assert hdr['HDUCLAS3'] == 'DETECTOR'
        assert 'HDUVERS1' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'VERSION' in hdr.keys()
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'ISAS/JAXA'        
        assert 'CCLS0001' in hdr.keys()
        assert hdr['CCLS0001'] == 'CPF'
        assert 'CCNM0001' in hdr.keys()
        assert hdr['CCNM0001'] == 'SPECRESP MATRIX'
        assert 'CDTP0001' in hdr.keys()
        assert hdr['CDTP0001'] == 'DATA'
        assert 'CVSD0001' in hdr.keys()
        assert 'CVST0001' in hdr.keys()
        assert 'CDES0001' in hdr.keys()
        assert 'CBD10001' in hdr.keys()
        assert 'CBD20001' in hdr.keys()
        assert 'CBD30001' in hdr.keys()
        
    def test_ebounds(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'EBOUNDS'
        assert 'RMFTYPE' in hdr.keys()
        assert 'COL_THA' in hdr.keys()
        assert 'COL_PHI' in hdr.keys()
        assert 'DET_THA' in hdr.keys()
        assert 'DET_PHI' in hdr.keys()
        assert 'NUMDETX' in hdr.keys()
        assert 'DETXCNTR' in hdr.keys()
        assert 'DETXMIN' in hdr.keys()
        assert 'DETXMAX' in hdr.keys()
        assert 'NUMDETY' in hdr.keys()
        assert 'DETYCNTR' in hdr.keys()
        assert 'DETYMIN' in hdr.keys()
        assert 'DETYMAX' in hdr.keys()
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'INSTRUME' in hdr.keys()
        assert 'DETNAM' in hdr.keys()
        assert 'CHANTYPE' in hdr.keys()
        assert 'DETCHANS' in hdr.keys()
        assert 'HDUCLASS' in hdr.keys()
        assert hdr['HDUCLASS'] == 'OGIP'
        assert 'HDUCLAS1' in hdr.keys()
        assert hdr['HDUCLAS1'] == 'RESPONSE'
        assert 'HDUCLAS2' in hdr.keys()
        assert hdr['HDUCLAS2'] == 'EBOUNDS'
        assert 'HDUVERS' in hdr.keys()
        assert 'HDUCLAS3' in hdr.keys()
        assert hdr['HDUCLAS3'] == 'DETECTOR'
        assert 'HDUVERS1' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'VERSION' in hdr.keys()
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'ISAS/JAXA'        
        assert 'CCLS0001' in hdr.keys()
        assert hdr['CCLS0001'] == 'CPF'
        assert 'CCNM0001' in hdr.keys()
        assert hdr['CCNM0001'] == 'EBOUNDS'
        assert 'CDTP0001' in hdr.keys()
        assert hdr['CDTP0001'] == 'DATA'
        assert 'CVSD0001' in hdr.keys()
        assert 'CVST0001' in hdr.keys()
        assert 'CDES0001' in hdr.keys()
        assert 'CBD10001' in hdr.keys()
        assert 'CBD20001' in hdr.keys()
        assert 'CBD30001' in hdr.keys()
        
        
    
            

