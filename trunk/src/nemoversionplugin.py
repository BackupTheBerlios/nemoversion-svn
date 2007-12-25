import sys
#append nautilus lib
sys.path.append("/usr/lib/nautilus-python/")
#append nemoversion home
sys.path.append("/home/milestones/dev/berlios/nemoversion/trunk/src/")
from nemoversion import handler
nemo = handler.NemoversionHandler