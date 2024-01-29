from datetime import date
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save

# Download bhavcopy
bhavcopy_save(date(2024,1,25), "./")

# Download bhavcopy for futures and options
bhavcopy_fo_save(date(2024,1,25), "./")
