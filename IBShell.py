import config
import cmd2 as cmd
from IBOrders import showAllOrders, showWorkingOrders, showFilledOrders
from IBPositions import showPositions
from IBTrades import showOpenTrades
from IBAccounts import showAccountSummary, showAccountValues

class IBShell(cmd.Cmd):
    intro = "Now go and make some R's!"
    prompt = "ibsh:> "

    show_cmds = ['positions', 'orders', 'trades', 'account']
    show_orders_cmds = ['all', 'working', 'filled', 'canceled']
    order_cmds = ['add', 'del']
    trade_cmds = ['all', 'open']

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.allow_cli_args = False

    def do_show(self, element):
        """group of 'show' commands"""
        config.logger.debug('element: %s' % element)

        if 'orders' in element:
            config.logger.debug('orders: %s' % element)
            if element.endswith('orders'):
                showWorkingOrders(config.session)
            if element.endswith('all'):
                showAllOrders(config.session)
            if element.endswith('working'):
                showWorkingOrders(config.session)
            if element.endswith('filled'):
                showFilledOrders(config.session)
            if element.endswith('canceled'):
                print('not yet implemented')

        if 'positions' in element:
            config.logger.debug('positions: %s' % element)
            showPositions(config.session)

        if 'trades' in element:
            config.logger.debug('trades: %s' % element)
            showOpenTrades(config.session)

        if 'account' in element:
            config.logger.debug('accounts: %s' % element)
            showAccountSummary(config.session)

    def complete_show(self, text, line, begidx, endidx):
        # 'show orders' completion
        if 'show orders' in line:
            if line.endswith('orders '):
                completions = [f for f in self.show_orders_cmds
                               if f.startswith(text)]
            else:
                for o_cmd in self.show_orders_cmds:
                    if line.endswith(o_cmd + ' '):
                        return False
                completions = [f for f in self.show_orders_cmds
                               if f.startswith(text)]
            return completions

        if 'show positions' in line:
            if line.endswith('positions '):
                return False

        if 'show trades' in line:
            if line.endswith('trades '):
                return False

        if not text:
            completions = self.show_cmds[:]
        else:
            completions = [f for f in self.show_cmds
                           if f.startswith(text)]
        return completions

    def do_order(self, action):
        config.logger.debug('order %s' % action)

    def complete_order(self, text, line, begidx, endidx):
        if not text:
            completions = self.order_cmds[:]
        else:
            completions = [f for f in self.order_cmds
                           if f.startswith(text)]
        return completions
