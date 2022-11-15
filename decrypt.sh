#!/bin/bash

ccdecrypt target_info.txt -K $1
ccdecrypt target_info_with_osint.txt -K $1
ccdecrypt search_keywords.txt -K $1
ccdecrypt combined_keywords.txt -K $1
ccdecrypt final_keywords.txt -K $1