import subprocess
import os


source = 'Source'
result = 'Result'
target_size = '200'


if not os.path.exists(result):
    os.makedirs(result)


def resize(source='Source', result='Result', target_size='200'):
    source_file = os.path.join(source, filename)
    result_file = os.path.join(result, filename)
    subprocess.run('convert.exe {0} -resize {2} {1}'.format(source_file, result_file, target_size))


for filename in os.listdir(source):
    resize(source, result, target_size)
