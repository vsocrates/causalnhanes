# Causal Nhanes
EECS 442 Causal Learning Project


## Installing packages
To install the necessary packages to run the analysis, run the following command. First, ensure that you have atleast miniconda or anaconda using [this guide](https://conda.io/docs/user-guide/install/download.html) installed on your computer.
 1. `conda create --name <env> --file requirements.txt`
 2. Install [xport](https://pypi.python.org/pypi/xport/): `pip install xport`

## Updating packages
If you need to install Python or R packages, install via conda using `conda install --name <env> <pkg>` and update the requirements accordingly using `conda list --export > requirements.txt`.

## Datasets
 - National Health and Nutrition Examination Survey ([NHANES](https://www.cdc.gov/nchs/nhanes/index.htm)) - [Data + Documentation](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2015)
 - National Longitudinal Study of Adolescent to Adult Health ([Add Health](http://www.cpc.unc.edu/projects/addhealth)) - [Data + Documentation](https://www.icpsr.umich.edu/icpsrweb/DSDR/studies/21600)