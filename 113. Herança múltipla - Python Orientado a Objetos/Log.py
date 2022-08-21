class LogMixin:
    def write(self,msg):
        with open('log.log','a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self,msg):
      self.write(f'Info {msg}')

    def log_error(self,msg):
        self.write(f'ERROR {msg}')
