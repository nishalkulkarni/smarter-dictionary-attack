#!/bin/bash

ccencrypt target_info.txt -K $1
ccencrypt target_info_with_osint.txt -K $1
ccencrypt search_keywords.txt -K $1
ccencrypt combined_keywords.txt -K $1
ccencrypt final_keywords.txt -K $1