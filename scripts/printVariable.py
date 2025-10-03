from netCDF4 import Dataset
from wrf import getvar

ncfile = Dataset("wrfout_d01_2016-10-07_00_00_00")

# Get the Sea Level Pressure (slp) for others variables see https://wrf-python.readthedocs.io/en/latest/diagnostics.html
slp = getvar(ncfile, "slp")

print(slp)
