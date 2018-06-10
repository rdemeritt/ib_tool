import  config
import ib_insync


class IBConnector(ib_insync.IB):
    def start_session(self, ip='127.0.0.1', port=7497, client_id=0):
        config.logger.info('starting IB session')
        ib_session = None

        try:
            ib_session = ib_insync.IB().connect(ip, port, client_id)
        except Exception as e:
            config.logger.error('unable to start IB ib_session: %s' % e)
            exit(3)

        ib_session.reqAutoOpenOrders()
        return ib_session
