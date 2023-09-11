import os

## TODO: delete output '.ts' files and 'links.txt' for next batch of links

current_dir = os.path.dirname(os.path.abspath(__file__))
ts_output = os.path.dirname(current_dir)

def concatenate_ts_files(input_files, output_file):
    with open(output_file, 'wb') as output_ts:
        for input_file in input_files:
            with open(input_file, 'rb') as input_ts:
                output_ts.write(input_ts.read())

def get_ts_files_in_directory(directory):
    ts_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".ts"):
            ts_files.append(os.path.join(directory, filename))
    return sorted(ts_files, key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))

output_path = os.path.join(current_dir, 'output')
output_file = os.path.join(ts_output, 'output.ts')
ts_files = get_ts_files_in_directory(output_path)
concatenate_ts_files(ts_files, output_file)
print(f'Concatenated {len(ts_files)} .ts files into {output_file}')
exit(0)
