import time
import argparse

from selenium import webdriver

import elearndriver



def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-u', '--username', required=True)
    parse.add_argument('-p', '--password', required=True)
    args = parse.parse_args()
    
    elearn = elearndriver.ELearn()

    elearn.login(args.username, args.password)

    elearn.take_exam(9001)
    time.sleep(20)

    elearn.logout()

    time.sleep(3)

    elearn.quit()




if __name__ == '__main__':
    main()

