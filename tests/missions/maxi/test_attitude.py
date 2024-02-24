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
from gdt.core.coords import Quaternion
from gdt.missions.maxi.attitude import MaxiAttitude
from gdt.missions.maxi.headers import AttitudeHeaders

att_file = data_path / 'maxi-gsc/mx_mjd58849.att.gz'

# the first sample
time_att1 = 631152082.011275
quat1 = [0.76156184, -0.55583739,  0.14661502, -0.29928647]

# the last sample
time_att2 = 631238482.1558492
quat2 = [-0.13035963, -0.31312412,  0.70131989,  0.6269849]

@unittest.skipIf(not att_file.exists(), 
                 "test files aren't downloaded. run gdt-data download.")
class TestMaxiAttitude(unittest.TestCase):
    
    def setUp(self):
        self.att = MaxiAttitude.open(att_file)
        
    def test_get_spacecraft_frame(self):
        frame = self.att.get_spacecraft_frame()
        assert frame.obstime.size == 86401
        
        assert frame[0].obstime.value == time_att1
        assert round(frame[0].quaternion.x, 6) == round(quat1[0], 6)
        assert round(frame[0].quaternion.y, 6) == round(quat1[1], 6)
        assert round(frame[0].quaternion.z, 6) == round(quat1[2], 6)
        assert round(frame[0].quaternion.w, 6) == round(quat1[3], 6)

        assert frame[-1].obstime.value == time_att2
        assert round(frame[-1].quaternion.x, 6) == round(quat2[0], 6)
        assert round(frame[-1].quaternion.y, 6) == round(quat2[1], 6)
        assert round(frame[-1].quaternion.z, 6) == round(quat2[2], 6)
        assert round(frame[-1].quaternion.w, 6) == round(quat2[3], 6)
    
    def test_headers(self):
        assert isinstance(self.att.headers, AttitudeHeaders)
