# Abstraction
# Inheritance - It is one
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implement log method')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('Anything')
    l.log_success('Amazing')
