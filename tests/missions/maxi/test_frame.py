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

import numpy as np
import unittest
from astropy.constants import R_earth
from astropy.coordinates import SkyCoord
import astropy.coordinates.representation as r

from gdt.core import data_path
from gdt.core.coords import Quaternion
from gdt.missions.maxi.attitude import MaxiAttitude
from gdt.missions.maxi.frame import *
from gdt.missions.maxi.orbit import MaxiOrbit
from gdt.missions.maxi.time import Time
from gdt.missions.maxi.gsc.detectors import GscFov

att_file = data_path / 'maxi-gsc/mx_mjd58849.att.gz'
orb_file = data_path / 'maxi-gsc/mx_mjd58849.orb.gz'

# taken from the first attitude sample in mx_mjd58849.att.gz
time_att = 631152082.011275
quat = Quaternion([0.76156184, -0.55583739,  0.14661502, -0.29928647])

# taken from the first orbit sample in mx_mjd58849.orb.gz
time_orb = 631152006.0929999
geoloc = r.CartesianRepresentation(x=-3988.9697208000002, y=-1428.2728356, 
                                   z=5300.4774864, unit='km')
latitude = 51.260266939984156
longitude = 99.78280706834872
altitude = 6785.787020220252 # from geocenter

class TestMaxiFrameAttitude(unittest.TestCase):
    
    def setUp(self):
        self.frame = MaxiFrame(obstime=Time(time_att, format='maxi'),
                               quaternion=quat, detectors=GscFov)
    
    def test_to_cgro_frame(self):
        
        coord1 = SkyCoord(0.0, 0.0, unit='deg').transform_to(self.frame)
        assert round(coord1.az[0].value, 2) == 294.08
        assert round(coord1.el[0].value, 2) == 33.78

        coord2 = SkyCoord(90.0, 0.0, unit='deg').transform_to(self.frame)
        assert round(coord2.az[0].value, 2) == 192.25
        assert round(coord2.el[0].value, 2) == 17.03

        coord3 = SkyCoord(0.0, 90.0, unit='deg').transform_to(self.frame)
        assert round(coord3.az[0].value, 2) == 259.97
        assert round(coord3.el[0].value, 2) == -51.07
                
    def test_to_icrs_frame(self):
        coord1 = SkyCoord(294.08, 33.78, unit='deg', frame=self.frame).icrs
        assert round(coord1.ra[0].value, 2) == 360.0
        assert round(coord1.dec[0].value, 2) == 0.0

        coord2 = SkyCoord(192.25, 17.03, unit='deg', frame=self.frame).icrs
        assert round(coord2.ra[0].value, 2) == 90.0
        assert round(coord2.dec[0].value, 2) == 0.0

        coord3 = SkyCoord(259.97, -51.07, unit='deg', frame=self.frame).icrs
        assert round(coord3.dec[0].value, 1) == 90.0

    def test_detectors(self):
        self.assertTrue(isinstance(self.frame.detectors.H, GscFov))
        self.assertTrue(isinstance(self.frame.detectors.Z, GscFov))
            

class TestMaxiFrameOrbi(unittest.TestCase):
    
    def setUp(self):
        self.frame = MaxiFrame(obstime=Time(time_orb, format='maxi'),
                               obsgeoloc=geoloc, detectors=GscFov)
    
    def test_latitude(self):
        lat = self.frame.earth_location.lat
        assert round(lat.value, 0) == round(latitude, 0)

    def test_longitude(self):
        lon = self.frame.earth_location.lon
        assert round(lon.value, 2) == round(longitude, 2)
    
    def test_altitude(self):
        # since we have to add the mean Earth radius, this will introduce some
        # uncertainty.  Testing to < 0.5% deviation.
        height = self.frame.earth_location.height.to('km')
        alt = R_earth.to('km') + height
        assert np.abs(alt.value - altitude) / altitude < 0.005

@unittest.skipIf(not att_file.exists() or not orb_file.exists(), 
                 "test files aren't downloaded. run gdt-data download.")
class TestCombineOrbitAttitude(unittest.TestCase):
    
    def setUp(self):
        att = MaxiAttitude.open(att_file)
        self.att_frame = att.get_spacecraft_frame()
        orb = MaxiOrbit.open(orb_file)
        self.orb_frame = orb.get_spacecraft_frame()
        self.frame = MaxiFrame.combine_orbit_attitude(self.orb_frame,
                                                      self.att_frame)
    
    def test_attitude(self):
        els = [1000, 43200, -1000]
        for i in els:
            frame = self.frame.at(self.att_frame.obstime[i])
            assert round(frame.quaternion.x, 5) == \
                   round(self.att_frame[i].quaternion.x, 5)
            assert round(frame.quaternion.y, 5) == \
                   round(self.att_frame[i].quaternion.y, 5)
            assert round(frame.quaternion.z, 5) == \
                   round(self.att_frame[i].quaternion.z, 5)
            assert round(frame.quaternion.w, 5) == \
                   round(self.att_frame[i].quaternion.w, 5)
               

    def test_orbit(self):
        els = [1000, 43200, -2000]
        for i in els:
            frame = self.frame.at(self.orb_frame.obstime[i])
            assert round(frame.obsgeoloc.x.value, 0) == \
                   round(self.orb_frame[i].obsgeoloc.x.value, 0)
            assert round(frame.obsgeoloc.y.value, 0) == \
                   round(self.orb_frame[i].obsgeoloc.y.value, 0)
            assert round(frame.obsgeoloc.z.value, 0) == \
                   round(self.orb_frame[i].obsgeoloc.z.value, 0)
            assert round(frame.obsgeovel.x.value, 0) == \
                   round(self.orb_frame[i].obsgeovel.x.value, 0)
            assert round(frame.obsgeovel.y.value, 0) == \
                   round(self.orb_frame[i].obsgeovel.y.value, 0)
            assert round(frame.obsgeovel.z.value, 0) == \
                   round(self.orb_frame[i].obsgeovel.z.value, 0)

    def test_errors(self):
        with self.assertRaises(ValueError):
            MaxiFrame.combine_orbit_attitude(self.orb_frame, self.att_frame,
                                             sample_period=-1.0)

        with self.assertRaises(TypeError):
            MaxiFrame.combine_orbit_attitude(self.att_frame, self.att_frame)

        with self.assertRaises(TypeError):
            MaxiFrame.combine_orbit_attitude(self.orb_frame, self.orb_frame)

