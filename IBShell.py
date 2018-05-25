import config

import cmd2 as cmd
import ibapi


class IBShell(cmd.Cmd):
    intro = "Now go and make some R's!"
    prompt = "ibsh:> "

    show_cmds = ['positions', 'orders']
    show_orders_cmds = ['all', 'working', 'filled', 'canceled']
    order_cmds = ['add', 'del']

    def do_show(self, element):
        """group of 'show' commands"""


        config.logger.debug("show %s" % element)
        if element and element in self.show_cmds:
            pass

    def complete_show(self, text, line, begidx, endidx):
        config.logger.debug(line)
        if line.endswith('orders '):
            completions = [f
                           for f in self.show_orders_cmds
                           if f.startswith(text)
                           ]
            return completions

        if not text:
            completions = self.show_cmds[:]
        else:
            completions = [f
                           for f in self.show_cmds
                           if f.startswith(text)
                           ]
        return completions

    def do_order(self, action):
        config.logger.debug("order %s" % action)

    def complete_order(self, text, line, begidx, endidx):
        if not text:
            completions = self.order_cmds[:]
        else:
            completions = [f
                           for f in self.order_cmds
                           if f.startswith(text)
                           ]
        return completions
