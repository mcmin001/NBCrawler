import logging
import logging.config
import os


def get_logger(name='root'):
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("NBCrawler\\") + len("NBCrawler\\")]  # 获取myProject，也就是项目的根路径
    conf_log = os.path.abspath(rootPath + "/resource/logger_config.ini")
    logging.config.fileConfig(conf_log)
    return logging.getLogger(name)


crawler_logger = get_logger(__name__)