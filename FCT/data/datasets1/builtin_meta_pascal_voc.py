# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
"""
Created on Wednesday, September 28, 2022

@author: Guangxing Han
"""

# PASCAL VOC categories
PASCAL_VOC_ALL_CATEGORIES = {
    1: ['brownblight','powdery mildew','bacterial blight','anthrancose'], 
    2: ['brownblight','powdery mildew','bacterial blight','anthrancose'], 
    3: ['brownblight','powdery mildew','bacterial blight','anthrancose'], 
}

PASCAL_VOC_NOVEL_CATEGORIES = {
    1: ['brownblight','anthrancose'],
    2: ['brownblight','anthrancose'],
    3: ['brownblight','anthrancose'],
}

PASCAL_VOC_BASE_CATEGORIES = {
    1: ['powdery mildew','bacterial blight'],
    2: ['powdery mildew','bacterial blight'],
    3: ['powdery mildew','bacterial blight'],
}

def _get_pascal_voc_fewshot_instances_meta():
    ret = {
        "thing_classes": PASCAL_VOC_ALL_CATEGORIES,
        "novel_classes": PASCAL_VOC_NOVEL_CATEGORIES,
        "base_classes": PASCAL_VOC_BASE_CATEGORIES,
    }
    return ret


def _get_builtin_metadata_pascal_voc(dataset_name):
    if dataset_name == "pascal_voc_fewshot":
        return _get_pascal_voc_fewshot_instances_meta()
    raise KeyError("No built-in metadata for dataset {}".format(dataset_name))
