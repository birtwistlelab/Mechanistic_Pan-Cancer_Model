python test2.py

echo "Got:"
md5 t_deterministic.csv xoutG_deterministic.csv xoutS_deterministic.csv
echo "----"
echo "Expect:"
cat md5sums.txt

rm t_deterministic.csv rm xoutG_deterministic.csv xoutS_deterministic.csv
