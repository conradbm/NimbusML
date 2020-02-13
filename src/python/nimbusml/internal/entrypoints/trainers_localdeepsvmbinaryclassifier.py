# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Trainers.LocalDeepSvmBinaryClassifier
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def trainers_localdeepsvmbinaryclassifier(
        training_data,
        predictor_model=None,
        feature_column_name='Features',
        label_column_name='Label',
        example_weight_column_name=None,
        normalize_features='Auto',
        caching='Auto',
        tree_depth=3,
        lambda_w=0.1,
        lambda_theta=0.01,
        lambda_thetaprime=0.01,
        sigma=1.0,
        number_of_iterations=15000,
        use_bias=True,
        calibrator=None,
        max_calibration_examples=1000000,
        cache=True,
        **params):
    """
    **Description**
        LD-SVM learns a binary, non-linear SVM classifier with a kernel that
        is specifically designed to reduce prediction time. LD-SVM
        learns decision boundaries that are locally linear.

    :param training_data: The data to be used for training (inputs).
    :param feature_column_name: Column to use for features (inputs).
    :param label_column_name: Column to use for labels (inputs).
    :param example_weight_column_name: Column to use for example
        weight (inputs).
    :param normalize_features: Normalize option for the feature
        column (inputs).
    :param caching: Whether trainer should cache input training data
        (inputs).
    :param tree_depth: Depth of Local Deep SVM tree (inputs).
    :param lambda_w: Regularizer for classifier parameter W (inputs).
    :param lambda_theta: Regularizer for kernel parameter Theta
        (inputs).
    :param lambda_thetaprime: Regularizer for kernel parameter
        Thetaprime (inputs).
    :param sigma: Parameter for sigmoid sharpness (inputs).
    :param number_of_iterations: Number of iterations (inputs).
    :param use_bias: No bias (inputs).
    :param calibrator: The calibrator kind to apply to the predictor.
        Specify null for no calibration (inputs).
    :param max_calibration_examples: The maximum number of examples
        to use when training the calibrator (inputs).
    :param cache: Whether to cache the data before the first
        iteration (inputs).
    :param predictor_model: The trained model (outputs).
    """

    entrypoint_name = 'Trainers.LocalDeepSvmBinaryClassifier'
    inputs = {}
    outputs = {}

    if training_data is not None:
        inputs['TrainingData'] = try_set(
            obj=training_data,
            none_acceptable=False,
            is_of_type=str)
    if feature_column_name is not None:
        inputs['FeatureColumnName'] = try_set(
            obj=feature_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if label_column_name is not None:
        inputs['LabelColumnName'] = try_set(
            obj=label_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if example_weight_column_name is not None:
        inputs['ExampleWeightColumnName'] = try_set(
            obj=example_weight_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if normalize_features is not None:
        inputs['NormalizeFeatures'] = try_set(
            obj=normalize_features,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'No',
                'Warn',
                'Auto',
                'Yes'])
    if caching is not None:
        inputs['Caching'] = try_set(
            obj=caching,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Auto',
                'Memory',
                'None'])
    if tree_depth is not None:
        inputs['TreeDepth'] = try_set(
            obj=tree_depth,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if lambda_w is not None:
        inputs['LambdaW'] = try_set(
            obj=lambda_w,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if lambda_theta is not None:
        inputs['LambdaTheta'] = try_set(
            obj=lambda_theta,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if lambda_thetaprime is not None:
        inputs['LambdaThetaprime'] = try_set(
            obj=lambda_thetaprime,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if sigma is not None:
        inputs['Sigma'] = try_set(
            obj=sigma,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if number_of_iterations is not None:
        inputs['NumberOfIterations'] = try_set(
            obj=number_of_iterations,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if use_bias is not None:
        inputs['UseBias'] = try_set(
            obj=use_bias,
            none_acceptable=True,
            is_of_type=bool)
    if calibrator is not None:
        inputs['Calibrator'] = try_set(
            obj=calibrator,
            none_acceptable=True,
            is_of_type=dict)
    if max_calibration_examples is not None:
        inputs['MaxCalibrationExamples'] = try_set(
            obj=max_calibration_examples,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if cache is not None:
        inputs['Cache'] = try_set(
            obj=cache,
            none_acceptable=True,
            is_of_type=bool)
    if predictor_model is not None:
        outputs['PredictorModel'] = try_set(
            obj=predictor_model, none_acceptable=False, is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint
