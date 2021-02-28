import subprocess

class BajkowyManager:
    def __init__(self):
        self.service = "bajkowy.service"
        if not self.is_active():
            self.start()

    def stop(self):
        completed = False
        try:
            cmd = f'/bin/systemctl stop {self.service}.service'
            completed = subprocess.run( cmd, shell=True, check=True, stdout=subprocess.PIPE )
        except subprocess.CalledProcessError as err:
            print( 'ERROR:', err)
        return completed

    def start(self):
        completed = False
        try:
            cmd = f'/bin/systemctl start {self.service}.service'
            completed = subprocess.run( cmd, shell=True, check=True, stdout=subprocess.PIPE )
        except subprocess.CalledProcessError as err:
            print( 'ERROR:', err)
        return completed

    def is_active(self):
        """Return True if systemd service is running"""
        try:
            cmd = f'/bin/systemctl status {self.service}.service'
            completed = subprocess.run( cmd, shell=True, check=True, stdout=subprocess.PIPE )
        except subprocess.CalledProcessError as err:
            print( 'ERROR:', err )
        else:
            for line in completed.stdout.decode('utf-8').splitlines():
                if 'Active:' in line:
                    if '(running)' in line:
                        print('True')
                        return True
            return False