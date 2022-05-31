
# Create input dir to place input files

mkdir -p ./input

# Setup python venv

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

