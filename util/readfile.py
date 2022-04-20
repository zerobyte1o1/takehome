import yaml
class YamlHandle:
    def __init__(self,file):
        self.file = file
    def load_file(self):
        """
        read yaml file
        :return: dict
        """
        with open(file=self.file,encoding='utf-8') as f:
            data=yaml.load(f,yaml.FullLoader)
        return data
    def get_data(self,node):
        """
        get the node data
        :param node:node name
        :return: dict or str
        """
        return self.load_file()[node]


if __name__ == '__main__':
    p = YamlHandle('../data/use_case.yaml').get_data('add')
    print(p)