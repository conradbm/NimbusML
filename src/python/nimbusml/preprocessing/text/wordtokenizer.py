# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
WordTokenizer
"""

__all__ = ["WordTokenizer"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.preprocessing.text.wordtokenizer import \
    WordTokenizer as core
from ...internal.utils.utils import trace


class WordTokenizer(core, BaseTransform, TransformerMixin):
    """
    **Description**
        The input to this transform is text, and the output is a vector of text containing the words (tokens) in the original text. The separator is space, but can be specified as any other character (or multiple characters) if needed.

    :param columns: see `Columns </nimbusml/concepts/columns>`_.

    :param char_array_term_separators: Array of single character term
        separator(s). By default uses space character separator.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            char_array_term_separators=None,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            char_array_term_separators=char_array_term_separators,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)