# -*- coding: utf-8 -*-

"""Tests constants."""
import os

TEST_FOLDER = os.path.dirname(os.path.realpath(__file__))
RESOURCES_FOLDER = os.path.join(TEST_FOLDER, 'resources')

GML_FILE_EXAMPLE = os.path.join(RESOURCES_FOLDER, '_graph.gml')
COMMUTE_TIME_KERNEL = os.path.join(RESOURCES_FOLDER, 'commuteTimeKernel.csv')
DIFFUSION_KERNEL = os.path.join(RESOURCES_FOLDER, 'diffusionKernel.csv')
INVERSE_COSINE_KERNEL = os.path.join(RESOURCES_FOLDER, 'inverseCosineKernel.csv')
P_STEP_KERNEL = os.path.join(RESOURCES_FOLDER, 'pStepKernel.csv')
REGULARISED_LAPLACIAN_KERNEL = os.path.join(RESOURCES_FOLDER, 'regularisedLaplacianKernel.csv')


INPUT_SCORES = os.path.join(RESOURCES_FOLDER, 'input_scores.csv')
INPUT_UNLABELED_SCORES = os.path.join(RESOURCES_FOLDER, 'input_unlabeled_scores.csv')

OUTPUT_RAW_SCORES = os.path.join(RESOURCES_FOLDER, 'output_raw_scores.csv')
OUTPUT_Z_SCORES = os.path.join(RESOURCES_FOLDER, 'output_z_scores.csv')
OUTPUT_ML_SCORES = os.path.join(RESOURCES_FOLDER, 'output_ml_scores.csv')
OUTPUT_GM_SCORES = os.path.join(RESOURCES_FOLDER, 'output_gm_scores.csv')
