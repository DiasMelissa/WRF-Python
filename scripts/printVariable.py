from netCDF4 import Dataset
from wrf import getvar

ncfile = Dataset("wrfout_d01_2018-02-18_00_00_00")

# Get the Sea Level Pressure (slp). See more variables: https://wrf-python.readthedocs.io/en/latest/diagnostics.html
slp = getvar(ncfile, "slp")

print(slp)
