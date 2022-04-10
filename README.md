
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
> python hw1.py -i data/input.txt -s blosum62.txt > output.txt
> python hw1.py -i data/sample-input1.txt -s blosum62.txt > output1.txt 
> diff -E -b output1.txt data/sample-output1.txt #compare with standard results
> python hw1.py -i data/sample-input2.txt -s blosum62.txt > output2.txt
> diff -E -b output2.txt data/sample-output2.txt #compare with standard results
> ```
>
> --------------------------------
>
> If you install the package in the python:
>
> ```
> python3
> 
> ```
>
> You could try the sample data:
>
> ```
> 
> ```
>
> 
>
> ## Usage and Options
>
> ```
> Usage: python hw1.py -i <input file> -s blosum62.txt  [OPTION...]
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
>Usage: python hw1.py -i <input file> -s blosum62.txt  [OPTION...]
> 
>input file (-i --input):
> The name of input file.
> score file (-s --score):
> The name of score file.
> 
>Options (need to include values after the option switches):
> --opengap:
> The number of open gap penalty used. Default is -2.
> --extgap:
> The number of extension gap penalty used. Default is -1.
> ```
>
> 
