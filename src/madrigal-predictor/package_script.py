import argparse
from parrot import encode_sequence
from madrigal-predictor.run_query import run
from madrigal-predictor.process_runs import get_runs, get_runs_coords
# TODO: Add file parsing
# TODO: Add docstrings and type hints

def analyze_fasta_file(file_path, threshold=0.6):
    # Read file path
    # Seperate into sequences


def read_sequence(data, threshold=0.6):
    data = sanitize(data)
    query_input = encode_sequence.one_hot(data).float().unsqueeze(0)
    output = run(query_input).squeeze().tolist()
    sequence = ''.join(data.upper().split())
    above_runs, below_runs, above_starts, below_starts= get_runs_coords(sequence, output, threshold)
    return above_runs, below_runs, above_starts, below_starts

def sanitize(sequence):
    return ''.join(sequence.upper().split())

def read_sequences(data, threshold=0.6):
    lines = data.splitlines()

    titles = []
    above_runs = []
    below_runs = []
    above_starts = []
    below_starts = []

    seq = ''
    for line in lines:
        if line.startswith('>'):
            if seq != '':
                seq = sanitize(seq)
                above_run, below_run, above_start, below_start = read_sequence(seq, threshold)
                above_runs.append(above_run)
                below_runs.append(below_run)
                above_starts.append(above_start)
                below_starts.append(below_start)
                seq = ''
            titles.append(line[1:])
        else:
            seq += line

    if seq != '':
        seq = sanitize(seq)
        above_run, below_run, above_start, below_start = read_sequence(seq, threshold)
        above_runs.append(above_run)
        below_runs.append(below_run)
        above_starts.append(above_start)
        below_starts.append(below_start)
        seq = ''


    return titles, above_runs, below_runs, above_starts, below_starts
