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
import unittest
from gdt.core import data_path
from gdt.core.binning.binned import combine_by_factor
from gdt.core.binning.unbinned import bin_by_time
from gdt.missions.maxi.gsc.detectors import GscDetectors
from gdt.missions.maxi.gsc.headers import EventsHeaders
from gdt.missions.maxi.gsc.response import GscRmf
from gdt.missions.maxi.gsc.tte import *

tte_file = data_path / 'maxi-gsc/mx_mjd55616_gsc_med_000.evt.gz'
rmf803_file = data_path / 'maxi-gsc/mx_gsc0_hv803_detx0000_0000.rmf'


@unittest.skipIf(not tte_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestGscTte(unittest.TestCase):
    
    def setUp(self):
        self.tte = GscTte.open(tte_file)
        self.rmf = GscRmf.open(rmf803_file)
    
    def test_detector(self):
        assert self.tte.detector == 'ALL'
    
    def test_event_deadtime(self):
        self.assertEqual(self.tte.event_deadtime, 3e-5)

    def test_filename(self):
        assert self.tte.filename == 'mx_mjd55616_gsc_med_000.evt.gz'
    
    def test_headers(self):
        assert isinstance(self.tte.headers, EventsHeaders)
    
    def test_num_chans(self):
        assert self.tte.num_chans == 1187
    
    def test_overflow_deadtime(self):
        assert self.tte.overflow_deadtime == 3e-5
    
    def test_time_range(self):
        t0, t1 = self.tte.time_range
        self.assertAlmostEqual(t0, 351823349.07326806)
        self.assertAlmostEqual(t1, 351905899.23335385)
            
    def test_trigtime(self):
        assert self.tte.trigtime is None
    
    def test_rebin_energy(self):
        self.tte.set_ebounds(self.rmf.ebounds)
        tte2 = self.tte.rebin_energy(combine_by_factor, 2)
        assert tte2.num_chans == self.tte.num_chans // 2
    
    def test_to_phaii(self):
        phaii = self.tte.to_phaii(bin_by_time, 8.192)
        assert phaii.data.num_times == 10077
        
        self.tte.set_ebounds(self.rmf.ebounds)
        phaii = self.tte.to_phaii(bin_by_time, 8.192)
        assert phaii.data.num_times == 10077
        
    def test_set_ebounds(self):
        self.tte.set_ebounds(self.rmf.ebounds)
        assert self.tte.ebounds.num_intervals == self.rmf.ebounds.num_intervals
    
    def test_slice_energy(self):
        tte2 = self.tte.slice_energy((50, 300))
        chan_min, chan_max = tte2.data.channel_range
        assert chan_min == 50
        assert chan_max == 300
        assert tte2.detector == self.tte.detector
        
    def test_slice_time(self):
        tte2 = self.tte.slice_time((351823449., 351823549.))
        t0, t1 = tte2.time_range
        self.assertAlmostEqual(t0, 351823449., places=0)
        self.assertAlmostEqual(t1, 351823539., places=0)
        assert tte2.detector == self.tte.detector
        
    def test_to_pha(self):
        with self.assertRaises(RuntimeError):
            pha = self.tte.to_pha()

        self.tte.set_ebounds(self.rmf.ebounds)
        pha = self.tte.to_pha()
        assert pha.num_chans == self.tte.num_chans

    def test_to_spectrum(self):
        spec = self.tte.to_spectrum()
        assert spec.size == 1200

        self.tte.set_ebounds(self.rmf.ebounds)
        spec = self.tte.to_spectrum()
        assert spec.size == 1200

