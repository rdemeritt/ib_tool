import  config
import ib_insync


class IBConnector(ib_insync.IB):
    def start_session(self, ip='127.0.0.1', port=7497, client_id=1):
        config.logger.info('starting IB session')

        try:
            ib_session = ib_insync.IB().connect(ip, port, client_id)
            return ib_session
        except Exception as e:
            config.logger.error('unable to start IB session: %s' % e)
            exit(3)
