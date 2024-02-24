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

import os
import numpy as np
import unittest

from gdt.missions.maxi.time import *
from gdt.missions.maxi.gsc.finders import GscEventsFinder

download_dir  = os.path.dirname(os.path.abspath(__file__))

                
class TestGscEventsFinder(unittest.TestCase):
    
    finder = GscEventsFinder(Time('2020-01-01 12:00:00', format='iso'), 'low')
    
    def test_cd(self):
        self.assertEqual(self.finder.num_files, 750)
       
        time = Time('2020-01-02 12:00:00', format='iso')
        self.finder.cd(time, 'low')
        self.assertEqual(self.finder.num_files, 753)
       
        time = Time('2020-01-01 12:00:00', format='iso')
        self.finder.cd(time, 'med')
        self.assertEqual(self.finder.num_files, 752)
        
        self.finder.cd(time, 'low')
    
    def test_ls_event(self):
        files = self.finder.ls_event()
        assert len(files) > 0
        for file in files:
            assert 'evt' in file
    
    def test_get_event(self):
        fnames = self.finder.get_event(download_dir, pixels=(0,1,2))
        assert len(fnames) == 3
        for fname in fnames:
            os.remove(os.path.join(download_dir, fname))

