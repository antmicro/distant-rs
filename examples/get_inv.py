import sys
from distantrs.viewer import InvocationViewer

if __name__ == '__main__':
    try:
        iid = sys.argv[1]
    except:
        sys.exit(1)

    i = InvocationViewer(iid)

    print(i.get_invocation())
