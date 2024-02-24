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
from gdt.missions.maxi.time import *

# tstart from mx_mjd55046.att.gz
met1 = 3.025889814082700E+08
utc_str1 = '2009-08-03T04:29:39.408'

# tstart from mx_mjd55616_gsc_low_000.evt.gz
# Not using because the file itself contains incorrect times.
# The conversion between MET and UTC ISOT is off by 1.754 s for TSTART and
# is off by 9.676 s for TSTOP.  The fact that the time conversion is 
# inconsistent in the same file, along with the fact that the conversion works
# for the attitude/orbit files, indicates the science files have incorrect 
# TSTART/TSTOP or DATE-OBS/DATE-END.
met2 = 351820802.754062
utc_str2 = '2011-02-23T23:59:59'

# tstart from mx_mjd58849.att.gz
met3 = 6.311520820112751E+08
utc_str3 = '2020-01-01T00:01:17.011'


class TestTime():
    
    def test_to_utc(self):
        assert Time(met1, format='maxi').utc.isot == utc_str1
        #assert Time(met2, format='maxi').isot == utc_str2
        assert Time(met3, format='maxi').utc.isot == utc_str3
    
    def test_to_maxi(self):
        assert Time(utc_str1, format='isot', scale='utc').maxi == round(met1, 3)
        #assert Time(utc_str2, format='isot', scale='utc').maxi == round(met2, 3)
        assert Time(utc_str3, format='isot', scale='utc').maxi == round(met3, 3)


