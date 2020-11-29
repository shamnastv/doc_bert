#!/bin/sh
#SBATCH --job-name=nlp # Job name
#SBATCH --ntasks=4 # Run on a single CPU
#SBATCH --time=1:50:00 # Time limit hrs:min:sec
#SBATCH --output=test_job%j.out # Standard output and error log
#SBATCH --gres=gpu:4
#SBATCH --partition=cl1_2h-4G

#printf "min freq 1\n"

python3 -m models.bert --dataset music --model bert-base-uncased --max-seq-length 256 --batch-size 16 --lr 2e-5 --epochs 30
