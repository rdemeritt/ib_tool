import config
import cmd2 as cmd
from utilities import whoami
from IBOrders import showAllOrders, showWorkingOrders,\
    showFilledOrders, showExecutions
from IBPositions import showPositions, showPNL
from IBTrades import showOpenTrades, showTrades
from IBAccounts import showAccountSummary, showAccountValues
from TradeCalc import calcEntryStopShares


class IBShell(cmd.Cmd):
    intro = "Now go and make some R's!"
    prompt = "ibsh:> "

    show_cmds = ['positions', 'orders', 'trades', 'accounts']
    show_orders_cmds = ['all', 'working', 'filled', 'canceled', 'executions']
    show_accounts_cmds = ['values', 'summary']
    order_cmds = ['add', 'del', 'modify']
    trade_cmds = ['all', 'open']

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.allow_cli_args = False

    def do_calc(self, element):
        config.logger.debug(f'{whoami()} element: {element}')
        if element.endswith(''):
            calc_cli = calc()
            calc_cli.cmdloop()
        else:
            print(calcEntryStopShares(element))

    def do_show(self, element):
        """group of 'show' commands"""
        config.logger.debug(f'{whoami()} element: {element}')

        if 'orders' in element:
            if element.endswith('orders'):
                showWorkingOrders(config.session)
            elif element.endswith('all'):
                showAllOrders(config.session)
            elif element.endswith('working'):
                showWorkingOrders(config.session)
            elif element.endswith('filled'):
                showFilledOrders(config.session)
            elif element.endswith('canceled'):
                print('not yet implemented')
            elif element.endswith('executions'):
                showExecutions(config.session)

        elif 'positions' in element:
            if element.endswith('positions'):
                showPositions(config.session)

        elif 'trades' in element:
            if element.endswith('all'):
                showTrades(config.session)
            elif element.endswith('open'):
                showOpenTrades(config.session)

        elif 'accounts' in element:
            if element.endswith('accounts'):
                showAccountSummary(config.session)
            elif element.endswith('values'):
                showAccountValues(config.session)
            elif element.endswith('summary'):
                showAccountSummary(config.session)

        elif 'pnl' in element:
            showPNL(config.session)

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

        if 'show accounts' in line:
            if line.endswith('accounts '):
                completions = [f for f in self.show_accounts_cmds
                               if f.startswith(text)]
            else:
                for a_cmd in self.show_accounts_cmds:
                    if line.endswith(a_cmd + ' '):
                        return False
                completions = [f for f in self.show_accounts_cmds
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

    def do_orders(self, action):
        config.logger.debug(f'{whoami()} action: {action}')
        order_cli = orders()
        order_cli.cmdloop()

    def complete_orders(self, text, line, begidx, endidx):
        if not text:
            completions = self.order_cmds[:]
        else:
            completions = [f for f in self.order_cmds
                           if f.startswith(text)]
        return completions

class orders(IBShell):
    intro = 'Manage IB Orders'
    prompt = '(orders):> '

    def __init__(self):
        IBShell.__init__(self)

    def do_show(self, element):
        config.logger.debug(f'{whoami()} element: {element}')
        IBShell.do_show(IBShell(), 'orders' + element)

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

class calc(IBShell):
    intro = 'Trade Calculator'
    prompt = '(calc):>'

    def __init__(self):
        IBShell.__init__(self)

    def default(self, element):
        config.logger.debug(f'{whoami()} element: {element}')
        IBShell.do_calc(IBShell(), 'calc' + element)
