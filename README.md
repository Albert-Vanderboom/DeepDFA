# Reproduction package for "Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection"

This repository includes the code to reproduce our experiments on DeepDFA, LineVul, LineVul+DeepDFA, UniXcoder, and CodeT5, accepted at ICSE 2024.

Links:
* Paper: https://www.computer.org/csdl/proceedings-article/icse/2024/021700a166/1RLIWqviwEM
* ArXiv preprint: https://arxiv.org/abs/2212.08108
* Data package: https://doi.org/10.6084/m9.figshare.21225413
* GitHub repo: https://github.com/ISU-PAAL/DeepDFA

# Changelog

- Initial data package creation: September 20, 2023
- Cleanup for artifact evaluation: January 04, 2024

# Organization

```bash
├── CodeT5: the code for the CodeT5 and CodeT5+DeepDFA models.
├── DDFA: the code for the DeepDFA model.
├── LineVul: the code for the LineVul and LineVul+DeepDFA models.
├── scripts: miscellaneous scripts we used to report the results.
└── README.md: this file
```

# Setup

Use these scripts to set up your environment for running the experiments.
We ran the experiments on an AMD Ryzen 5 1600 3.2 GHz processor with 48GB of RAM and an Nvidia 3090 GPU with 24GB of GPU memory and CUDA 11.3.

## Set up dependencies

```bash
# Create virtual environment
conda create --name deepdfa python=3.10 -y
conda activate deepdfa
# Install requirements
conda install cudatoolkit=11.6 -y
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"
pip install -r requirements.txt
# Add project files to import path
export PYTHONPATH="$PWD/DDFA:$PYTHONPATH"
# Install joern and add it to the executable path
bash scripts/install_joern.sh
export PATH="$PWD/joern/joern-cli:$PATH"
```

## Unpack data

```bash
# TODO: remove
# # Download raw CSV format of the Big-Vul dataset
# mkdir -p DDFA/storage/external/
# gdown --fuzzy 'https://drive.google.com/file/d/1-0VhnHBp9IGh90s2wCNjeCMuy70HPl8X/view?usp=sharing' -O DDFA/storage/external/MSR_data_cleaned.csv
# We included an archive containing the preprocessed files in the data package on Figshare.
# TODO: add link.
unzip preprocessed_data.zip 'DDFA/storage/*' -d DeepDFA/DDFA/storage/
unzip preprocessed_data.zip 'LineVul/data/*' -d LineVul/data/
```

# Run main experiments

## Train DeepDFA

This script trains DeepDFA based on the dataset of source code already processed into CFGs.
It reports the performance at the end, comparable to Table 3b in our paper.

```bash
cd DDFA
# Train DeepDFA
bash scripts/train.sh --seed_everything 1
```

## Train LineVul baseline or DeepDFA+LineVul

These scripts report performance of the LineVul and DeepDFA+LineVul models, comparable to Table 3b in our paper.

```bash
cd LineVul/linevul
# Train LineVul
bash scripts/msr_train_linevul.sh 1 MSR
# Train DeepDFA+LineVul
bash scripts/msr_train_combined.sh 1 MSR
```

# Run end-to-end processing

The above scripts use the preprocessed data included in our data archive, for ease of replicability. The instructions below show how to run the code end-to-end.

## Sample data

The current prototype scripts take some time to process data into the format for our dataset, so we provide instructions how to do it with sample mode or full data mode.

```bash
cd DDFA
bash scripts/run_prepare.sh --sample
bash scripts/run_getgraphs.sh --sample
bash scripts/run_dbize.sh --sample
bash scripts/run_abstract_dataflow.sh --sample
bash scripts/run_absdf.sh --sample
# Train DeepDFA
bash scripts/train.sh --seed_everything 1 --data.sample_mode True

cd ../LineVul/linevul
# Train DeepDFA+LineVul
bash scripts/msr_train_combined.sh 1 MSR --sample --epochs 1
```

## Full data preprocessing

To run the full preprocessing from the raw MSR dataset to training DeepDFA, unpack only `storage/external/MSR_data_cleaned.csv` (skipping the preprocessed data such as the CFGs in `storage/processed`) and run these steps.

```bash
cd DDFA
bash scripts/run_prepare.sh
bash scripts/run_getgraphs.sh # Make sure Joern is installed!
bash scripts/run_dbize.sh
bash scripts/run_abstract_dataflow.sh
bash scripts/run_absdf.sh
# Train DeepDFA
bash scripts/train.sh --seed_everything 1
```

# Extended README for all experiments

See README.extended.md in the Github repo for the extended instructions on running other experiments.

# Citation

If you used our code in your research, please consider citing our paper:

> Benjamin Steenhoek, Hongyang Gao, and Wei Le. 2024. Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection. In 2024 IEEE/ACM 46th International Conference on Software Engineering (ICSE ’24), April 14–20, 2024, Lisbon, Portugal. ACM, New York, NY, USA, 13 pages. https://doi.org/10.1145/3597503.3623345
