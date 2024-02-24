.. _gsc-catalogs:
.. |MaxiGsc37MonthCatalog| replace:: :class:`~gdt.missions.maxi.gsc.catalogs.MaxiGsc37MonthCatalog`
.. |MaxiGsc7YearCatalog| replace:: :class:`~gdt.missions.maxi.gsc.catalogs.MaxiGsc7YearCatalog`

***********************************************************
MAXI/GSC Catalogs (:mod:`gdt.missions.maxi.gsc.catalogs`)
***********************************************************

The HEASARC hosts a couple of MAXI/GSC catalogs: a high Galactic Latitude 
catalog of sources from the first 37 months of observations, and a more 
complete catalog of the first 7 years of sources. HEASARC provides a way to 
search these catalogs online through their Browse interface, but we offer a way 
to do it in Python through the Data Tools.

Let's look at accessing the 7-year catalog (|MaxiGsc7YearCatalog|):

    >>> from gdt.missions.maxi.gsc.catalogs import MaxiGsc7YearCatalog
    >>> cat = MaxiGsc7YearCatalog()
    Sending request and awaiting response from HEASARC...
    Downloading maxigsc7yr from HEASARC via w3query.pl...
    Finished in 2 s
    >>> cat
    <MaxiGsc7YearCatalog: 38 columns, 907 rows>
    
Depending on your connection, initialization may take a few seconds. We can 
see what columns are available in the catalog:

    >>> print(cat.columns)
    ('NAME',
     'RA',
     'DEC',
     'ERROR_RADIUS',
     'FLUX_4_10',
     'FLUX_4_10_ERROR',
     'FLUX_3_4_LIMIT',
     'FLUX_3_4',
     'FLUX_3_4_ERROR',
     'EXCESS_VARIANCE',
     'EXCESS_VARIANCE_ERROR',
     'CTRPART_NAME',
     'OBJECT_TYPE',
     'BII',
     'CATALOG',
     'CATALOG_SOURCE_NUMBER',
     'CTRPART_DEC',
     'CTRPART_FLAGS',
     'CTRPART_OFFSET',
     'CTRPART_RA',
     'DETSIG_10_20',
     'DETSIG_3_4',
     'DETSIG_4_10',
     'FLUX_10_20',
     'FLUX_10_20_ERROR',
     'FLUX_10_20_LIMIT',
     'FLUX_3_10',
     'FLUX_3_10_ERROR',
     'HARDNESS_RATIO_1',
     'HARDNESS_RATIO_1_ERROR',
     'HARDNESS_RATIO_2',
     'HARDNESS_RATIO_2_ERROR',
     'HARDNESS_RATIO_3',
     'HARDNESS_RATIO_3_ERROR',
     'LII',
     'NOTE_FLAG',
     'REDSHIFT',
     'TIMEVAR')

We can also return the range of values for a given column:

    >>> cat.column_range('FLUX_4_10')
    (4.33e-12, 1.8192e-07)

If we only care about specific columns in the table, we can return a numpy 
record array with only those columns. Let's return a table with the RA, Dec, 
and error radius for every source:

    >>> cat.get_table(columns=('RA', 'DEC', 'ERROR_RADIUS'))
    rec.array([(3.47146e+02, -8.9383e+01,  709.2),
               (2.87090e+01, -8.3889e+01,  504. ),
               (2.96915e+02, -8.3585e+01, 1184.4), ...
               (3.19187e+02,  8.2221e+01,  406.8),
               (2.39155e+02,  8.4996e+01,  720. ),
               (2.59998e+02,  8.6165e+01,  536.4)],
              dtype=[('RA', '<f8'), ('DEC', '<f8'), ('ERROR_RADIUS', '<f8')])

Importantly, we can make slices of the catalog based on conditionals. Let's 
only select triggers with positive declinations:

    >>> sliced_cat = cat.slice('DEC', lo=0.0, hi=90.0)
    >>> sliced_cat
    <MaxiGsc7YearCatalog: 38 columns, 361 rows>
          
We can also slice on multiple conditionals, simultaneously. Select everything 
that has a positive declination *and* has an error radius less than 0.1 degree:

    >>> sliced_cat2 = cat.slices([('DEC', 0.0, 90.0), ('ERROR_RADIUS', 0.0, 0.1)])
    >>> sliced_cat2
    <MaxiGsc7YearCatalog: 38 columns, 63 rows>

    >>> sliced_trigcat2.get_table(columns=('trigger_name', 'trigger_time', 'error_radius'))
    rec.array([(287.824,  0.577, 0.), (285.442,  1.475, 0.),
               (284.579,  3.335, 0.), (287.989,  4.939, 0.),
               (279.994,  5.029, 0.), (287.675,  7.684, 0.), ...
               (343.29 , 62.617, 0.), (338.912, 63.401, 0.),
               ( 19.566, 63.711, 0.), (  6.308, 64.132, 0.),
               ( 19.492, 65.268, 0.)],
              dtype=[('RA', '<f8'), ('DEC', '<f8'), ('ERROR_RADIUS', '<f8')])

For more information on working with catalogs, see 
:external:ref:`The BrowseCatalog Class<core-heasarc-browse>`.

Reference/API
=============

.. automodapi:: gdt.missions.maxi.gsc.catalogs
   :inherited-members:


