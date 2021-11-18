from prj import *

import cProfile
import pstats
with cProfile.Profile() as pr:
    simula_ecossistema('test208.txt', 20, True)

stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()