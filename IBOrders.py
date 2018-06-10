from ib_insync import util
import config
from utilities import whoami


class IBOrders():
    def do_show(self, element):
        config.logger.debug(f'{whoami()} element: {element}')
        # IBShell.do_show(IBShell(), 'orders' + element)

        if 'orders' in element:
            if element.endswith('orders'):
                self.showWorkingOrders(config.ib_session)
            elif element.endswith('all'):
                self.showAllOrders(config.ib_session)
            elif element.endswith('working'):
                self.showWorkingOrders(config.ib_session)
            elif element.endswith('filled'):
                self.showFilledOrders(config.ib_session)
            elif element.endswith('canceled'):
                print('not yet implemented')
            elif element.endswith('executions'):
                self.showExecutions(config.ib_session)

    def complete_show(self, text, line, begidx, endidx):
        # 'show orders' completion
        if 'show' in line:
            if line.endswith('show '):
                completions = [f for f in self.show_orders_cmds
                               if f.startswith(text)]
            else:
                for o_cmd in self.show_orders_cmds:
                    if line.endswith(o_cmd + ' '):
                        return False
                completions = [f for f in self.show_orders_cmds
                               if f.startswith(text)]
            return completions

    def showAllOrders(self, _session):
        config.logger.debug(whoami())
        print(util.tree(_session.orders()))


    def showWorkingOrders(self, _session):
        config.logger.debug(whoami())
        print(util.tree(_session.openOrders()))


    def showFilledOrders(self, _session):
        config.logger.debug(whoami())
        print(util.tree(_session.fills()))

    def showExecutions(self, _session):
        config.logger.debug(whoami())
        print(util.tree(_session.executions()))
