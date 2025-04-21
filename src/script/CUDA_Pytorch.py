import torch
import matplotlib.pyplot as plt


def pythorchVersion():
    print("PyTorch 版本:", torch.__version__)
    print("PyTorch 编译使用的 CUDA 版本:", torch.version.cuda)
    print("当前是否能使用 GPU:", torch.cuda.is_available())
    print("当前使用的 GPU:", torch.cuda.get_device_name(0))

def checkmel():
    mel = torch.load("/home/tang/PPG-Mel/fac-via-ppg/src/script/output/synthesis/ac_mel.npy")
    mel = mel.detach().cpu().squeeze(0).numpy()
    plt.imshow(mel, aspect='auto', origin='lower')
    # plt.show()
    plt.savefig("/home/tang/PPG-Mel/fac-via-ppg/src/script/output/synthesis/mel_plot.png")



if __name__ == "__main__":
    # pythorchVersion()
    checkmel()