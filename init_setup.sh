echo[$(data)]:"START"
echo[$(date)]:"Creating Conda Environment with  python 3.9"
conda create --prefix ./env python=3.9  -y
echo[$(date)]:"Activating ENV"
source activate  ./env
echo[$(date)]:"Installing Dev requirements"
pip install -r requirements_dev.txt
echo[$(date)]:"END"


