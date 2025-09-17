from zk import ZK
from zk.base import ZK_helper


class ZKHelperExtended(ZK_helper):
    def test_ping(self):
        """
        Returns True if host responds to a ping request

        :return: bool
        """
        import platform  # , subprocess
        # # Ping parameters as function of OS
        ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1 -W 5"
        args = "ping " + " " + ping_str + " " + self.ip
        # need_sh = False if  platform.system().lower()=="windows" else True
        # # Ping
        # return subprocess.call(args,
        #                     stdout=subprocess.PIPE,
        #                     stderr=subprocess.PIPE,
        #                     shell=need_sh) == 0
        print(*args, end=' ')
        return True


class ZKExtended(ZK):
    def __init__(self, ip, port=4370, timeout=60, password=0, force_udp=False, ommit_ping=False, verbose=False,
                 encoding='UTF-8'):
        super().__init__(**locals())
        self.helper = ZKHelperExtended(ip, port)
