for i in $(seq 37)
do
    python3 main.py ${i}*.txt >> output.txt
done