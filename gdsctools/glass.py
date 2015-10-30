# coding=utf-8
# -*- coding utf-8 -*-
#
#  This file is part of GDSCTools software
#
#  Copyright (c) 2015 - Wellcome Trust Sanger Institute
#  All rights reserved
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the BSD 3-Clause License.
#  See accompanying file LICENSE.txt distributed with this software
#
#  website: http://github.com/CancerRxGene/gdsctools
#
##############################################################################
"""Glass effect size"""
import numpy as np


def glass(x, y):
    r"""Return Effect size through Glass :math:`\Delta` estimator

    :param x: first sample
    :param y: second sample
    :return: 2 values (one or each sample)

    The Glass effect size is computed as 

    .. math::  


        \Delta = \frac{\bar{x}_1-\bar{x}_2}{\sigma_i}

    .. note:: the standard deviation is the unbiased one (divided by N-1)

    where :math:`\sigma` is the standard deviation of either group

    """
    x = np.array(x)
    y = np.array(y)

    # mean difference: 
    md = np.abs(x.mean() - y.mean())

    # here, we want same as in R that is unbiased variance
    # so we use ddof = 1
    g1 = md / x.std(ddof=1)
    g2 = md / y.std(ddof=1)

    return g1, g2
