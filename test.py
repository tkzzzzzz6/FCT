import torch
# import detectron2
import torchvision

def check_pytorch():
    print("Testing PyTorch...")
    print("PyTorch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("CUDA version:", torch.version.cuda)
    else:
        print("CUDA is not available.")

def check_cudnn():
    print("Testing cuDNN...")
    print("cuDNN version:", torch.backends.cudnn.version())

def check_detectron2():
    print("Testing Detectron2...")
    print("Detectron2 version:", detectron2.__version__)

if __name__ == "__main__":
    check_pytorch()
    check_cudnn()
    # check_detectron2()
