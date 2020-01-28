# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
DateTimeSplitter
"""

__all__ = ["DateTimeSplitter"]


from ...entrypoints.transforms_datetimesplitter import \
    transforms_datetimesplitter
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignature


class DateTimeSplitter(BasePipelineItem, DefaultSignature):
    """
    **Description**
        Splits a date time value into each individual component

    :param prefix: Output column prefix.

    :param country: Country to get holidays for. Defaults to none if not
        passed.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            prefix,
            country='None',
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.prefix = prefix
        self.country = country

    @property
    def _entrypoint(self):
        return transforms_datetimesplitter

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            source=self.source,
            prefix=self.prefix,
            country=self.country)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)