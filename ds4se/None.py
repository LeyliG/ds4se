

# Cell
# Imports
import dit
import math
import os
import logging

import matplotlib.pyplot as plt
import pandas as pd
import sentencepiece as sp

from collections import Counter
from pathlib import Path
from scipy.stats import sem, t
from statistics import mean, median, stdev
from tqdm.notebook import tqdm

# ds4se
from .mgmnt.prep.bpe import *
from .exp.info import *
from .desc.stats import *

# Cell
# Imports
import dit
import math
import os
import logging

import matplotlib.pyplot as plt
import pandas as pd
import sentencepiece as sp

from collections import Counter
from pathlib import Path
from scipy.stats import sem, t
from statistics import mean, median, stdev
from tqdm.notebook import tqdm

# ds4se
from .mgmnt.prep.bpe import *
from .exp.info import *
from .desc.stats import *

# Cell
# Imports
import dit
import math
import os
import logging

import matplotlib.pyplot as plt
import pandas as pd
import sentencepiece as sp

from collections import Counter
from pathlib import Path
from scipy.stats import sem, t
from statistics import mean, median, stdev
from tqdm.notebook import tqdm

# ds4se
from .mgmnt.prep.bpe import *
from .exp.info import *
<<<<<<< HEAD
=======
from .desc.stats import *

# Cell
# Imports
import dit
import math
import os
import logging

import matplotlib.pyplot as plt
import pandas as pd
import sentencepiece as sp

from collections import Counter
from pathlib import Path
from scipy.stats import sem, t
from statistics import mean, median, stdev
from tqdm.notebook import tqdm

# ds4se
from .mgmnt.prep.bpe import *
from .exp.info import *
>>>>>>> SE_Proj2_Refactor
from .desc.stats import *

# Cell
# Imports
import dit
import math
import os
import logging

import matplotlib.pyplot as plt
import pandas as pd
import sentencepiece as sp

from collections import Counter
from pathlib import Path
from scipy.stats import sem, t
from statistics import mean, median, stdev
from tqdm.notebook import tqdm

# ds4se
from .mgmnt.prep.bpe import *
from .exp.info import *
from .desc.stats import *

# Cell
import os
import nbdev

if __name__ == '__main__':

    command_test1 = os.popen("nbdev_test_nbs --fname '.\nbs\1.0_exp.i.ipynb'")

    output = command_test1.read()