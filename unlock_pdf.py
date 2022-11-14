import os
import argparse
import pikepdf
from tqdm import tqdm


def main():
    passwords = []

    cwd = os.getcwd()
    # Argument and command-line options parsing
    parser = \
        argparse.ArgumentParser(
            description='Unlock dictionary attack for a PDF file.')
    parser.add_argument('-l', required=True, metavar='file',
                        dest='dictionary',
                        help='Specify dictionary file')
    parser.add_argument('-f', required=True, metavar='file',
                        dest='pdffilename', help='Specify ZIP file')
    args = parser.parse_args()
    pdf_file = args.pdffilename
    pathZip = os.getcwd()
    os.chdir(cwd)
    # Brute force through dictionary entries
    with open(args.dictionary, 'r') as f:
        os.chdir(pathZip)
        for line in f.readlines():
            passwords.append(line.strip('\n'))
        # Test passwords
    for password in tqdm(passwords, 'Cracking PDF File'):
        try:
            # open PDF file and check each password
            with pikepdf.open(pdf_file, password=password) as p:
                # If password is correct, break the loop
                print('[+] Password found:', password)
                break
        except pikepdf._qpdf.PasswordError as e:
            # If password will not match, it will raise PasswordError
            print("[-] Tried Password:", password,
                  " and FAILED in opening password protected file")


if __name__ == '__main__':
    main()
