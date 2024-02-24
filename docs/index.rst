.. _gdt-cgro:

**********************************************************
Welcome to the MAXI Gamma-ray Data Tools Documentation!
**********************************************************

The MAXI Gamma-ray Data Tools is a toolkit for MAXI data, primarily from the 
Gas Slit Camera (GSC) instrument, built on the 
:external:ref:`GDT Core Package<gdt-core>`.

.. image:: images/MAXI_new_logo_ver2_03_kibo.png
   :scale: 25%
   :align: center

The Monitor of All Sky X-ray Image (MAXI) mission contains two X-ray instruments 
on-board the ISS, the Gas Slit Camera (GSC) and the Solid-state Slit Camera 
(SSC). The GSC, which is the primary focus of GDT-MAXI, is sensitive to X-rays 
between 2 and 30 keV, and has detected numerous transients including many GRBs 
since 2009. The GDT-MAXI currently supports data access of the the GSC event 
files and responses as well as the MAXI auxiliary files used to determine the
pointing of the MAXI instruments and the location of the ISS in orbit.

.. figure:: https://heasarc.gsfc.nasa.gov/docs/maxi/gallery/images/mihara1_fig3.jpg

.. rubric:: Citing

If you use the MAXI Gamma-ray Data Tools in your research and publications, 
we would definitely appreciate an appropriate acknowledgment and citation! We 
suggest including the following BibTex entries:

::

 @misc{GDT-MAXI,
       author = {Adam Goldstein},
       title = {MAXI Gamma-ray Data Tools: v1.0.0},
       year = 2024,
       url = {https://github.com/USRA-STI/gdt-maxi}
 }

 @misc{GDT-CORE,
       author = {Adam Goldstein and William H. Cleveland and Daniel Kocevski},
       title = {Gamma-ray Data Tools Core: v2.0.1},
       year = 2024,
       url = {https://github.com/USRA-STI/gdt-core}
 }
 

.. rubric:: Acknowledgments

The creation of the MAXI Gamma-ray Data Tools were funded by the NASA's
Astrophysics Data Analysis Program (ADAP) via grant number 80NSSC21K0651.


***************
Getting Started
***************
.. toctree::
   :maxdepth: 1

   install

******************
User Documentation
******************

MAXI Definitions
=================
.. toctree::
   :maxdepth: 1

Mission Definitions
-------------------
.. toctree::
   :maxdepth: 1

   missions/maxi/time
   missions/maxi/frame
   missions/maxi/plot
   missions/maxi/finders
   missions/maxi/headers

Data Types
----------
.. toctree::
   :maxdepth: 1

   missions/maxi/attitude
   missions/maxi/orbit
   

MAXI/GSC
========

Instrument Definitions
----------------------

.. toctree::
   :maxdepth: 1

   missions/maxi/gsc/detectors
   missions/maxi/gsc/headers

Data Types
----------

.. toctree::
   :maxdepth: 1

   missions/maxi/gsc/tte
   missions/maxi/gsc/response

Data Finders and Catalogs
-------------------------

.. toctree::
   :maxdepth: 1

   missions/maxi/gsc/finders
   missions/maxi/gsc/catalogs

----

*******
License
*******
.. toctree::
   :maxdepth: 1
   
   license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
