## 环境

我电脑上的配置是：
detectron2                0.6
pytorch                   1.10.0          py3.8_cuda11.3_cudnn8.2.0_0    

你电脑如果跑不起，可以试试autodl，要用autodl的话你跟我说一声，我把镜像分享给你

## 数据集

FCT和Meta faster rcnn都要进行数据划分，而且格式是一样的

如果没记错的话都是先进行base class训练，再用base+novel进行微调

微调的时候才有1 shot 2shot...之分

## 训练&评价指标

我需要 per-class mAP50,overall bbox AP,Mean precision@50,Mean recall@50

你需要改evaluation文件，我是直接在pascal_voc_evaluation里改的，等会发你

如果配置文件里面没有EVAL_PERIOD你要自己补上：


ft阶段的训练参数：MAX_ITER要一样，如果涉及WARMUP就把WARMIUP_ITERS设计成一样
![1739539818893278bfe2369b133637c3fd5b0252df4cf.png](https://fastly.jsdelivr.net/gh/tkzzzzzz6/imagehost@main/blog/1739539818893278bfe2369b133637c3fd5b0252df4cf.png)

## 其他

每个网络都先跑5shot，跑完之后给我看看ft训练的log文件