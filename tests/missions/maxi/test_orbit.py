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

from gdt.core import data_path
from gdt.missions.maxi.orbit import MaxiOrbit
from gdt.missions.maxi.headers import OrbitHeaders

orb_file = data_path / 'maxi-gsc/mx_mjd58849.orb.gz'

# the first sample
time_orb1 = 631152006.0929999
xyz1 = [-3988.9697208000002, -1428.2728356, 5300.4774864]
vel1 = [-7.318415878125001, -0.4989478889648438, -0.6007799616210938]

# the last sample
time_orb2 = 631238406.0810001
xyz2 = [4069.944108, 1306.5383064, -5293.958424]
vel2 = [7.293625875000001, -0.11359239667968751, 0.8026731638671876]

@unittest.skipIf(not orb_file.exists(), 
                 "test files aren't downloaded. run gdt-data download.")
class TestMaxiOrbit(unittest.TestCase):
    
    def setUp(self):
        self.orb = MaxiOrbit.open(orb_file)
    
    def test_get_spacecraft_frame(self):
        frame = self.orb.get_spacecraft_frame()
        assert frame.obstime.size == 86362
        
        assert frame[0].obstime.value == time_orb1
        assert round(frame[0].obsgeoloc.x.value, 6) == round(xyz1[0] * 1000.0, 6)
        assert round(frame[0].obsgeoloc.y.value, 6) == round(xyz1[1]* 1000.0, 6)
        assert round(frame[0].obsgeoloc.z.value, 6) == round(xyz1[2]* 1000.0, 6)
        assert round(frame[0].obsgeovel.x.value, 6) == round(vel1[0] * 1000.0, 6)
        assert round(frame[0].obsgeovel.y.value, 6) == round(vel1[1]* 1000.0, 6)
        assert round(frame[0].obsgeovel.z.value, 6) == round(vel1[2]* 1000.0, 6)

        assert frame[-1].obstime.value == time_orb2
        assert round(frame[-1].obsgeoloc.x.value, 6) == round(xyz2[0] * 1000.0, 6)
        assert round(frame[-1].obsgeoloc.y.value, 6) == round(xyz2[1]* 1000.0, 6)
        assert round(frame[-1].obsgeoloc.z.value, 6) == round(xyz2[2]* 1000.0, 6)
        assert round(frame[-1].obsgeovel.x.value, 6) == round(vel2[0] * 1000.0, 6)
        assert round(frame[-1].obsgeovel.y.value, 6) == round(vel2[1]* 1000.0, 6)
        assert round(frame[-1].obsgeovel.z.value, 6) == round(vel2[2]* 1000.0, 6)
    
    def test_headers(self):
        assert isinstance(self.orb.headers, OrbitHeaders)
