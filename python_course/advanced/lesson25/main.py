from log import LogFileMixin, LogPrintMixin
lp = LogPrintMixin()
lp.log_error('Anything')
lp.log_success('Amazing')
lf = LogFileMixin()
lf.log_error('Anything')
lf.log_success('Amazing')