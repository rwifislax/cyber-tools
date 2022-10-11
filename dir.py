# Directory listing tool.
# Usage: python3 dir.py -f/--file dictionary.txt -u/--url https://evilcorp.com

import os,requests,sys,argparse,re

def help():
    print('''
    Directory listing Utility by wifislax.

    usage: 
        python3 dir.py -f/--file dictionary.txt -u/--url https://evilcorp.com
    
    ''')

    sys.exit(0)

def dirlisting(dictionary, url):
    file = f"{dictionary}"

    sub_list = open(file).read() 
    directories = sub_list.splitlines()

    for dir in directories:

        dir_enum = f"{url}/{dir}"
        r = requests.get(dir_enum)
        if r.status_code == 404: 
            pass
        elif r.status_code == 403:
            print("Forbidden directory:" ,dir_enum)
        else:
            print("Possible valid directory [Code " + str(r.status_code) + "]:" ,dir_enum)

def main():

    parser = argparse.ArgumentParser(description='Accept a file as a dictionary')

    parser.add_argument('-f','--file', dest='dictionary', required=True, help='Dictionary to use')
    parser.add_argument('-u','--url', dest='target_url', required=True, help='URL to do directory listing. Ex: https://evilcorp.com')
    
    args = parser.parse_args()

    if not re.match('^http|https://\S+$', args.target_url):
        help()

    dirlisting(args.dictionary,args.target_url)

if __name__ == '__main__':
    main()
