# CUDA_VISIBLE_DEVICES=0 python3 fsod_train_net.py --num-gpus 1 --dist-url auto \
#         --config-file configs/fsod/two_branch_1shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.yaml SOLVER.IMS_PER_BATCH 8 2>&1 | tee log/two_branch_1shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.txt
# CUDA_VISIBLE_DEVICES=0 python3 fsod_train_net.py --num-gpus 1 --dist-url auto \
#         --config-file configs/fsod/two_branch_2shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.yaml SOLVER.IMS_PER_BATCH 8 2>&1 | tee log/two_branch_2shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.txt
# CUDA_VISIBLE_DEVICES=0 python3 fsod_train_net.py --num-gpus 1 --dist-url auto \
#         --config-file configs/fsod/two_branch_3shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.yaml SOLVER.IMS_PER_BATCH 8 2>&1 | tee log/two_branch_3shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.txt
CUDA_VISIBLE_DEVICES=0 python3 fsod_train_net.py --num-gpus 1 --dist-url auto \
        --config-file configs/fsod/two_branch_5shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.yaml SOLVER.IMS_PER_BATCH 8 2>&1 | tee log/two_branch_5shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.txt
# CUDA_VISIBLE_DEVICES=0 python3 fsod_train_net.py --num-gpus 1 --dist-url auto \
#         --config-file configs/fsod/two_branch_10shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.yaml SOLVER.IMS_PER_BATCH 8 2>&1 | tee log/two_branch_10shot_finetuning_pascalvoc_split1_pvt_v2_b2_li.txt
