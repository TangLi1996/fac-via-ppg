# Foreign Accent Conversion by Synthesizing Speech from Phonetic Posteriorgrams

This repository hosts the code we used to
prepare our interspeech'19 paper titled "[Foreign Accent Conversion by Synthesizing Speech from Phonetic Posteriorgrams](https://www.isca-archive.org/interspeech_2019/zhao19f_interspeech.pdf)"

### Install

This project uses `conda` to manage all the dependencies, you should install [anaconda](https://anaconda.org/) if you have not done so. 

```bash
# Clone the repo
git clone https://github.com/guanlongzhao/fac-via-ppg.git
cd $PROJECT_ROOT_DIR

# Install dependencies
conda env create -f environment.yml

# Activate the installed environment
conda activate ppg-speech
conda activate ppg-speech-cuda12

# Compile protocol buffer to get the data_utterance_pb2.py file
protoc -I=src/common --python_out=src/common src/common/data_utterance.proto

# Include src in your PYTHONPATH
export PYTHONPATH=$PROJECT_ROOT_DIR/src:$PYTHONPATH
```
Path on GPU
```bash
export PYTHONPATH='/home/tang/PPG-Mel/fac-via-ppg/src':'/home/tang/anaconda3/envs/ppg-speech/lib/python3.7'
```

If `conda` complains that some packages are missing, it is very likely that you can find a similar version of that package on anaconda's archive.

If you are using `pytorch >= 1.3`, you may need to remove the `byte()` method call in `src.common.utils.get_mask_from_lengths`.

### Run unit tests

```bash
cd test

# Remember to make this script executable
./run_coverage.sh
```

This only does a few sanity checks, don't worry if the test coverage looks low :)

Depending on your git configs, you may or may not need to recreate the symbolic links in `test/data`.

### Train PPG-to-Mel model
Change default parameters in `src/common/hparams.py:create_hparams()`.
The training and validation data should be specified in text files, see `data/filelists` for examples.

```bash
cd src
python script/train_ppg2mel.py
```
nohup python script/train_ppg2mel.py > train-koren-YKWK-2.log 2>&1 &
The `FP16` mode will not work, unfortunately :(

### Train WaveGlow model
Change the default parameters in `src/waveglow/config.json`. The training data should be specified in the same manner as the PPG-to-Mel model.

```bash
cd src/script
python train_waveglow.py
```
nohup python train_waveglow.py > train-waveglow.log 2>&1 &

### View training progress
You should find a dir `log` in all of your output dirs, that is the `LOG_DIR` you should use below.

```bash
tensorboard --logdir=${LOG_DIR}
```
tensorboard --logdir="/home/tang/PPG-Mel/fac-via-ppg/src/script/output/ppg-koren-YKWK/logs"

tensorboard --logdir="/home/tang/PPG-Mel/fac-via-ppg/src/script/output/waveglow/log"

### Generate speech synthesis
Use `src/script/generate_synthesis.py`, you can find pre-trained models in the [Links](#Links) section.

```bash
python generate_synthesis.py --ppg2mel_model "/home/tang/PPG-Mel/fac-via-ppg/src/script/output/ppg-koren-YKWK/checkpoint_40000" --waveglow_model "/home/tang/PPG-Mel/fac-via-ppg/src/script/output/waveglow/waveglow_1210000" --teacher_utterance_path "/home/tang/PPG-Mel/fac-via-ppg/recordings/L1/arctic_b0498.wav" --output_dir "/home/tang/PPG-Mel/fac-via-ppg/src/script/output/synthesis"
```
```bash
generate_synthesis.py [-h] --ppg2mel_model PPG2MEL_MODEL
                           --waveglow_model WAVEGLOW_MODEL
                           --teacher_utterance_path TEACHER_UTTERANCE_PATH
                           --output_dir OUTPUT_DIR
```

### Links

- Demo: [link to audio samples](https://guanlongzhao.github.io/demo/fac-via-ppg)

### Citation
Please kindly cite the following paper if you use this code repository in your work,

```
@inproceedings{zhao2019ForeignAC,
  author={Guanlong Zhao and Shaojin Ding and Ricardo Gutierrez-Osuna},
  title={{Foreign Accent Conversion by Synthesizing Speech from Phonetic Posteriorgrams}},
  year=2019,
  booktitle={Proc. Interspeech 2019},
  pages={2843--2847},
  doi={10.21437/Interspeech.2019-1778},
  url={http://dx.doi.org/10.21437/Interspeech.2019-1778}
}
```
