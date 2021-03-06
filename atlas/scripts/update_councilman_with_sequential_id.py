import sys, os
import pandas as pd

sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atlas.settings")

import django
django.setup()

from councilman.models import Councilman

def update_sequential_id(row):
    c = Councilman.objects.get(name=row.loc['name'])
    c.sequential_id = row.loc['sequential_id']
    c.save()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = str(sys.argv[1])

        print("Reading file " + f)

        df = pd.read_csv(f)
        df['from_file'] = f.split("/")[-1]
        df.apply(update_sequential_id, axis=1)

    else:
        print("Please, provide the file path")
