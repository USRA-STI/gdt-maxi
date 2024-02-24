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
from gdt.missions.maxi.gsc.detectors import GscDetectors
from gdt.missions.maxi.gsc.headers import ArfHeaders, RmfHeaders
from gdt.missions.maxi.gsc.response import *
from gdt.core.spectra.functions import PowerLaw

arf_file = data_path / 'maxi-gsc/mx_gsc0_arfcorr_20151126.fits'
rmf803_file = data_path / 'maxi-gsc/mx_gsc0_hv803_detx0000_0000.rmf'
rmf854_file = data_path / 'maxi-gsc/mx_gsc0_hv854_detxm002_m002.rmf'

@unittest.skipIf(not arf_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestMaxiArf(unittest.TestCase):
    
    def setUp(self):
        self.arf = GscArf.open(arf_file)
    
    def test_detector(self):
        assert self.arf.detector == 'HA0'
    
    def test_headers(self):
        assert isinstance(self.arf.headers, ArfHeaders)
    
    def test_get_arf(self):
        arf = self.arf.get_arf(803)
        assert round(float(arf.counts[0]), 6) == round(0.5928503, 6)
        assert round(float(arf.lo_edges[0]), 3) == round(0.475, 3)
        assert round(float(arf.hi_edges[0]), 3) == round(0.525, 3)
        assert round(float(arf.counts[-1]), 6) == round(1.0, 6)
        assert round(float(arf.lo_edges[-1]), 3) == round(60.425, 3)
        assert round(float(arf.hi_edges[-1]), 3) == round(60.475, 3)

        arf = self.arf.get_arf(854)
        assert round(float(arf.counts[0]), 7) == round(1.0013245, 7)
        assert round(float(arf.lo_edges[0]), 3) == round(0.475, 3)
        assert round(float(arf.hi_edges[0]), 3) == round(0.525, 3)
        assert round(float(arf.counts[-1]), 6) == round(1.0, 6)
        assert round(float(arf.lo_edges[-1]), 3) == round(60.425, 3)
        assert round(float(arf.hi_edges[-1]), 3) == round(60.475, 3)
    
        with self.assertRaises(ValueError):
            self.arf.get_arf(888)


@unittest.skipIf((not rmf803_file.exists()) or (not rmf854_file.exists()), 
                "test files aren't downloaded. run gdt-data download.")
class TestMaxiRmf(unittest.TestCase):
    
    def setUp(self):
        self.rmf803 = GscRmf.open(rmf803_file)
        self.rmf854 = GscRmf.open(rmf854_file)
    
    def test_detector(self):
        assert self.rmf803.detector == 'HA0'
        assert self.rmf854.detector == 'HA0'
    
    def test_headers(self):
        assert isinstance(self.rmf803.headers, RmfHeaders)
        assert isinstance(self.rmf854.headers, RmfHeaders)
    
    def test_apply_arf(self):
        arf = GscArf.open(arf_file)
        rsp803 = self.rmf803.apply_arf(arf)
        assert isinstance(rsp803, GscRsp)
        rsp854 = self.rmf854.apply_arf(arf)
        assert isinstance(rsp854, GscRsp)


@unittest.skipIf((not rmf803_file.exists()) or (not arf_file.exists()), 
                "test files aren't downloaded. run gdt-data download.")
class TestGscRsp(unittest.TestCase):
    
    def setUp(self):
        arf = GscArf.open(arf_file)
        rmf = GscRmf.open(rmf803_file)
        self.rsp = rmf.apply_arf(arf)
            
    def test_detector(self):
        assert self.rsp.detector == 'HA0'

    def test_filename(self):
        assert self.rsp.filename == 'mx_gsc0_hv803_detx0000_0000.rsp'
    
    def test_num_chans(self):
        assert self.rsp.num_chans == 1200

    def test_num_ebins(self):
        assert self.rsp.num_ebins == 1201

    def test_tcent(self):
        assert self.rsp.tcent == 0.0

    def test_trigtime(self):
        assert self.rsp.trigtime is None

    def test_tstart(self):
        assert self.rsp.tstart == 0.0

    def test_tstop(self):
        assert self.rsp.tstop == 0.0

    def test_fold_spectrum(self):
        ebins = self.rsp.fold_spectrum(PowerLaw().fit_eval, (0.01, -2.2), exposure=2.0)
        assert ebins.size == self.rsp.num_chans
        assert ebins.exposure[0] == 2.0

    def test_rebin(self):
        rsp = self.rsp.rebin(factor=2)
        assert rsp.num_chans == self.rsp.num_chans // 2
        assert rsp.num_ebins == self.rsp.num_ebins

    def test_resample(self):
        rsp = self.rsp.resample(num_photon_bins=600)
        assert rsp.num_chans == rsp.num_chans
        assert rsp.num_ebins == 600

