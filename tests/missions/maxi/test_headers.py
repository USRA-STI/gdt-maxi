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
from gdt.missions.maxi.headers import *


class TestAttitudeHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = AttitudeHeaders()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'ISAS/JAXA'
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
        assert 'DATE' in hdr.keys()
        assert 'CREATOR' in hdr.keys()

    def test_attitude(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'ATTITUDE'
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'ISAS/JAXA'
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
        assert 'DATE' in hdr.keys()
        assert 'CREATOR' in hdr.keys()
        assert 'TSTART' in hdr.keys()
        assert 'TSTOP' in hdr.keys()
        assert 'DATE-OBS' in hdr.keys()
        assert 'DATE-END' in hdr.keys()
        assert 'PROCVER' in hdr.keys()
    

class TestOrbitHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = OrbitHeaders()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'ISAS/JAXA'
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
        assert 'DATE' in hdr.keys()
        assert 'CREATOR' in hdr.keys()

    def test_orbit(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'ORBIT'
        assert 'VERSION' in hdr.keys()
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'MAXI'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'ISAS/JAXA'
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
        assert 'DATE' in hdr.keys()
        assert 'CREATOR' in hdr.keys()
        assert 'TSTART' in hdr.keys()
        assert 'TSTOP' in hdr.keys()
        assert 'DATE-OBS' in hdr.keys()
        assert 'DATE-END' in hdr.keys()
        assert 'PROCVER' in hdr.keys()
    


