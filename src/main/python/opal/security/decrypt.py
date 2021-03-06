"""
Opal Encryption
"""

import opal.core
import sys


def add_arguments(parser):
    parser.add_argument('encrypted', help='Encrypted text to decrypt')


def do_command(args):
    try:
        request = opal.core.OpalClient.build(opal.core.OpalClient.LoginInfo.parse(args)).new_request()
        request.fail_on_error()

        if args.verbose:
            request.verbose()

        response = request.get().resource("/system/crypto/decrypt/" + args.encrypted).send()
        print(response.content)

    except Exception as e:
        print(e)
        sys.exit(2)
    except pycurl.error as error:
        errno, errstr = error
        print('An error occurred: ', errstr, file=sys.stderr)
        sys.exit(2)
