# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
OnnxRunner
"""

__all__ = ["OnnxRunner"]


from ...entrypoints.models_onnxtransformer import models_onnxtransformer
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignature


class OnnxRunner(BasePipelineItem, DefaultSignature):
    """
    **Description**
        Applies an ONNX model to a dataset.

    :param model_file: Path to the onnx model file.

    :param input_columns: Name of the input column.

    :param output_columns: Name of the output column.

    :param gpu_device_id: GPU device id to run on (e.g. 0,1,..). Null for CPU.
        Requires CUDA 9.1.

    :param fallback_to_cpu: If true, resumes execution on CPU upon GPU error.
        If false, will raise the GPU execption.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            model_file,
            input_columns=None,
            output_columns=None,
            gpu_device_id=None,
            fallback_to_cpu=False,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.model_file = model_file
        self.input_columns = input_columns
        self.output_columns = output_columns
        self.gpu_device_id = gpu_device_id
        self.fallback_to_cpu = fallback_to_cpu

    @property
    def _entrypoint(self):
        return models_onnxtransformer

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            model_file=self.model_file,
            input_columns=self.input_columns,
            output_columns=self.output_columns,
            gpu_device_id=self.gpu_device_id,
            fallback_to_cpu=self.fallback_to_cpu)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
