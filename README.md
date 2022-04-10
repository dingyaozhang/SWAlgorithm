
> # SWAlgorithm
>
> Smith-Waterman Algorithm for CB&B 752: Biomedical Data Science: Mining and Modeling
>
> Python3 is required.
>
> ## Installation
>
> The script can be directly downloaded from Github using the following commands:
>
> ```
> git clone https://github.com/dingyaozhang/SWAlgorithm.git
> cd SWAlgorithm
> ```
>
> You could directly use hw1.py in the folder.
>
> If you want to install the package in the python:
>
> ```
> pip install git+https://github.com/dingyaozhang/SW_Algorithm.git
> ```
>
> 
>
> ## Quick Start
>
> If you directly download the script folder, you could use it directly
>
> ```
> python hw1.py -i <input file> -s blosum62.txt 
> # if you have your own substitution matrix file, you could change blosum62.txt.
> # you could use > to output data to a file.
> ```
>
> You could try the sample data:
>
> ```
> python hw1.py -i tests/input.txt -s blosum62.txt > output.txt
> python hw1.py -i tests/sample-input1.txt -s blosum62.txt > output1.txt 
> diff -E -b output1.txt tests/sample-output1.txt #compare with standard results
> python hw1.py -i tests/sample-input2.txt -s blosum62.txt > output2.txt
> diff -E -b output2.txt tests/sample-output2.txt #compare with standard results
> ```
>
> --------------------------------
>
> If you install the package in the python, then in the command line:
>
> ```
> python -c "from SWAlgorithm.hw1 import runSW;runSW('<input file>','blosum62.txt',-2,-1)" > output.txt
> ```
>
> You could try the sample data:
>
> ```
> python -c "from SWAlgorithm.hw1 import runSW;runSW('tests/input.txt','blosum62.txt',-2,-1)" > output.txt
> python -c "from SWAlgorithm.hw1 import runSW;runSW('tests/sample-input1.txt','blosum62.txt',-2,-1)" > output1.txt
> diff -E -b output1.txt tests/sample-output1.txt #compare with standard results
> python -c "from SWAlgorithm.hw1 import runSW;runSW('tests/sample-input2.txt','blosum62.txt',-2,-1)" > output2.txt
> diff -E -b output2.txt tests/sample-output2.txt #compare with standard results
> ```
>
> You could also use it in python like:
>
> ```
> import sys
> sys.stdout = open('file.txt', 'w')
> from SWAlgorithm.hw1 import runSW
> runSW('tests/input.txt','blosum62.txt',-2,-1)
> sys.stdout.close()
> ```
>
> 
>
> ## Usage and Options
>
> ```
> Usage: python hw1.py -i <input file> -s <score file>  [OPTION...]
> 
> input file (-i --input):
> The name of input file.
> score file (-s --score):
> The name of score file.
> 
> Options (need to include values after the option switches):
> --opengap:
> The number of open gap penalty used. Default is -2.
> --extgap:
> The number of extension gap penalty used. Default is -1.
> ```
>
> For installation by pip: 
>
> ```
> Usage: runSW('<input file>','<score file>',opengap,extgap)
> python hw1.py -i  -s blosum62.txt  [OPTION...]
> 
> input file:
> The name of input file.
> score file:
> The name of score file.
> opengap:
> The number of open gap penalty used. We suggest to use -2.
> extgap:
> The number of extension gap penalty used. We suggest to use -1.
> ```
>
> 
