import config
from IBShell import IBShell

def main():
    IBShell().cmdloop()


# kick off the whole thing
if __name__ == '__main__':
    config.init()
    config.logger.info('Starting')
    main()
