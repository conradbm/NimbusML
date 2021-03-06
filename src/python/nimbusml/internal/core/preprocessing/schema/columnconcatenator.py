# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
ColumnConcatenator
"""

__all__ = ["ColumnConcatenator"]


from ....entrypoints.transforms_columnconcatenator import \
    transforms_columnconcatenator
from ....utils.utils import trace
from ...base_pipeline_item import BasePipelineItem, MultiOutputsSignature


class ColumnConcatenator(BasePipelineItem, MultiOutputsSignature):
    """

    Combines several columns into a single vector-valued column.

    .. remarks::
        ``ColumnConcatenator`` creates a single vector-valued column from
        multiple
        columns. It can be performed on data before training a model. The
        concatenation
        can significantly speed up the processing of data when the number of
        columns
        is as large as hundreds to thousands.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`ColumnDropper
        <nimbusml.preprocessing.schema.ColumnDropper>`,
        :py:class:`ColumnSelector
        <nimbusml.preprocessing.schema.ColumnSelector>`.

    .. index:: transform, schema

    Example:
       .. literalinclude:: /../nimbusml/examples/ColumnConcatenator.py
              :language: python
    """

    @trace
    def __init__(
            self,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

    @property
    def _entrypoint(self):
        return transforms_columnconcatenator

    @trace
    def _get_node(self, **all_args):

        input_columns = self.input
        if input_columns is None and 'input' in all_args:
            input_columns = all_args['input']
        if 'input' in all_args:
            all_args.pop('input')

        output_columns = self.output
        if output_columns is None and 'output' in all_args:
            output_columns = all_args['output']
        if 'output' in all_args:
            all_args.pop('output')

        # validate input
        if input_columns is None:
            raise ValueError(
                "'None' input passed when it cannot be none.")

        if not isinstance(input_columns, list):
            raise ValueError(
                "input has to be a list of list of strings, instead got %s" %
                type(input_columns))

        for i in input_columns:
            if not isinstance(i, list):
                raise ValueError(
                    "input has to be a list of list strings, instead got input element of type %s" %
                    type(i))

        # validate output
        if output_columns is None:
            raise ValueError(
                "'None' output passed when it cannot be none.")

        if not isinstance(output_columns, list):
            raise ValueError(
                "output has to be a list of strings, instead got %s" %
                type(output_columns))

        if (len(input_columns) != len(output_columns)):
            raise ValueError(
                "input and output have to be of same length, instead input %s and output %s" %
                (len(input_columns), len(output_columns)))

        column = []
        for i in range(len(input_columns)):
            source = []
            for ii in input_columns[i]:
                source.append(ii)
            column.append(
                dict([('Source', source), ('Name', output_columns[i])]))

        algo_args = dict(
            column=column
        )

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
