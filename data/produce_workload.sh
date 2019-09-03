size=$1
# your can choose your own suitable datasize

for ((flod=4;flod<=8;flod++));
do
for((time=size;time>=0;time--))
do
temp=$[$flod-1];
cat lda_gendata_$temp.txt>>lda_gendata_$flod.txt;
cat linear_gendata_$temp.txt>>linear_gendata_$flod.txt;
cat matrix_kind1_$temp.txt>>matrix_kind1_$flod.txt;
cat matrix_kind2_$temp.txt>>matrix_kind2_$flod.txt;
cat text_$temp.txt>>text_$flod.txt;


done
done
