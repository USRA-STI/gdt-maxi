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

from gdt.missions.maxi.gsc.detectors import *


class TestGscFov(unittest.TestCase):
    
    def test_H(self):
        det = GscFov.H
        assert det.full_name == 'GSC-H'
        assert det.number == 0
        assert det.azimuth.value == 0.0
        assert det.zenith.value == 90.0
        
        assert det.fov[0] == (280.0, 91.5)
        assert det.fov[1] == (80.0, 91.5)
        assert det.fov[2] == (80.0, 88.5)
        assert det.fov[3] == (280.0, 88.5)
        assert det.fov[4] == (280.0, 91.5)

    def test_Z(self):
        det = GscFov.Z
        assert det.full_name == 'GSC-Z'
        assert det.number == 1
        assert det.azimuth.value == 0.0
        assert det.zenith.value == 180.0
        
        assert det.fov[0] == (268.5, 100.0)
        assert det.fov[1] == (91.5, 100.0)
        assert det.fov[2] == (88.5, 100.0)
        assert det.fov[3] == (271.5, 100.0)
        assert det.fov[4] == (268.5, 100.0)


class TestGscDetectors(unittest.TestCase):
    
    def test_HA0(self):
        det = GscDetectors.HA0
        assert det.full_name == 'GSC_0'
        assert det.number == 0

    def test_HA1(self):
        det = GscDetectors.HA1
        assert det.full_name == 'GSC_1'
        assert det.number == 1

    def test_HA2(self):
        det = GscDetectors.HA2
        assert det.full_name == 'GSC_2'
        assert det.number == 2

    def test_HB0(self):
        det = GscDetectors.HB0
        assert det.full_name == 'GSC_6'
        assert det.number == 6

    def test_HB1(self):
        det = GscDetectors.HB1
        assert det.full_name == 'GSC_7'
        assert det.number == 7

    def test_HB2(self):
        det = GscDetectors.HB2
        assert det.full_name == 'GSC_8'
        assert det.number == 8
    
    def test_ZA0(self):
        det = GscDetectors.ZA0
        assert det.full_name == 'GSC_3'
        assert det.number == 3

    def test_ZA1(self):
        det = GscDetectors.ZA1
        assert det.full_name == 'GSC_4'
        assert det.number == 4

    def test_ZA2(self):
        det = GscDetectors.ZA2
        assert det.full_name == 'GSC_5'
        assert det.number == 5

    def test_ZB0(self):
        det = GscDetectors.ZB0
        assert det.full_name == 'GSC_9'
        assert det.number == 9

    def test_ZB1(self):
        det = GscDetectors.ZB1
        assert det.full_name == 'GSC_A'
        assert det.number == 10

    def test_ZB2(self):
        det = GscDetectors.ZB2
        assert det.full_name == 'GSC_B'
        assert det.number == 11

    def test_h_detectors(self):
        hs = [det.name for det in GscDetectors.h_detectors()]
        self.assertListEqual(hs, ['HA0', 'HA1', 'HA2', 'HB0', 'HB1', 'HB2'])

    def test_z_detectors(self):
        zs = [det.name for det in GscDetectors.z_detectors()]
        self.assertListEqual(zs, ['ZA0', 'ZA1', 'ZA2', 'ZB0', 'ZB1', 'ZB2'])
      
    def test_is_h_detector(self):
        assert GscDetectors.HA0.is_h_detector() == True
        assert GscDetectors.ZA0.is_h_detector() == False

    def test_is_z_detector(self):
        assert GscDetectors.HA0.is_z_detector() == False
        assert GscDetectors.ZA0.is_z_detector() == True
    
