# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
#
# MDAnalysis --- https://www.mdanalysis.org
# Copyright (c) 2006-2017 The MDAnalysis Development Team and contributors
# (see the file AUTHORS for the full list of names)
#
# Released under the Lesser GNU Public Licence, v2.1 or any higher version
#
# Please cite your use of MDAnalysis in published work:
#
# R. J. Gowers, M. Linke, J. Barnoud, T. J. E. Reddy, M. N. Melo, S. L. Seyler,
# D. L. Dotson, J. Domanski, S. Buchoux, I. M. Kenney, and O. Beckstein.
# MDAnalysis: A Python package for the rapid analysis of molecular dynamics
# simulations. In S. Benthall and S. Rostrup editors, Proceedings of the 15th
# Python in Science Conference, pages 102-109, Austin, TX, 2016. SciPy.
# doi: 10.25080/majora-629e541a-00e
#
# N. Michaud-Agrawal, E. J. Denning, T. B. Woolf, and O. Beckstein.
# MDAnalysis: A Toolkit for the Analysis of Molecular Dynamics Simulations.
# J. Comput. Chem. 32 (2011), 2319--2327, doi:10.1002/jcc.21787

import pytest
import warnings


def test_coordinate_converterbase_warning():
    from MDAnalysis.coordinates.base import ConverterBase
    import MDAnalysis.converters.base

    wmsg = ("ConverterBase moved from coordinates.base."
            "ConverterBase to converters.base.ConverterBase "
            "and will be removed from coordinates.base "
            "in MDAnalysis release 3.0.0")

    with pytest.warns(DeprecationWarning, match=wmsg):
        class DerivedConverter(ConverterBase):
            pass

    assert issubclass(DerivedConverter, ConverterBase)
    assert not issubclass(DerivedConverter,
                          MDAnalysis.converters.base.ConverterBase)


def test_converters_converterbase_no_warning():
    from MDAnalysis.converters.base import ConverterBase

    # check that no warning is issued at all
    # when subclassing converters.base.ConverterBase
    with warnings.catch_warnings():
        warnings.simplefilter("error")

        class DerivedConverter(ConverterBase):
            pass

    assert issubclass(DerivedConverter, ConverterBase)
