import pyotp, argparse, yaml, os


class OTP():
    def __init__(self):
        with open(os.path.dirname(os.path.abspath(__file__))+'/keys.yml') as self.yaml_file:
            self.yaml_data = yaml.safe_load(self.yaml_file)

    def show(self, name):
        if name == 'ALL':
            for name in self.yaml_data:
                self.totp = pyotp.TOTP(self.yaml_data[name]['key'])
                print(self.yaml_data[name]['name'], self.totp.now())
        elif name in self.yaml_data.keys():
            self.totp = pyotp.TOTP(self.yaml_data[name]['key'])
            print(self.totp.now())
        else:
            print(name+' does not exist.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=__file__)
    parser._action_groups.pop()
    #required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('--name', default='ALL', help='Name of AWS account (default: ALL)')
    args = parser.parse_args()

    OTP().show(args.name)
