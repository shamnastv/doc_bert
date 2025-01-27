#!/bin/sh
#SBATCH --job-name=nlp # Job name
#SBATCH --ntasks=4 # Run on a single CPU
#SBATCH --time=2:00:00 # Time limit hrs:min:sec
#SBATCH --output=test_job%j.out # Standard output and error log
#SBATCH --gres=gpu:4
#SBATCH --partition=cl1_2h-4G

#printf "min freq 1\n"

python3 -m models.bert --dataset music --model bert-base-uncased --max-seq-length 512 --batch-size 16 --lr 1.5e-5 --epochs 5
#python3 -m models.bert --dataset music --model bert-large-uncased --max-seq-length 300 --batch-size 16 --lr 2e-5 --epochs 5


#python3 -m models.bert --dataset music --model bert-base-uncased --max-seq-length 256 --batch-size 16 --lr 2e-5 --epochs 6 --trained-model model_checkpoints/bert/music/2020-11-29_13-48-48.pt
