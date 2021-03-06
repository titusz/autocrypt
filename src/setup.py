from setuptools import setup

def main():
    setup(
        name='autocrypt',
        description='Autocrypt: E-mail Encryption for Everyone example implementation',
        version="0.1",
        url='https://autocrypt.org',
        license='MIT license',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
        author='holger krekel and the autocrypt team',
        author_email='autocrypt at lists.mayfirst.org',
        classifiers=['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Utilities',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python'],
        packages=['autocrypt'],
        zip_safe=False,
    )

if __name__ == '__main__':
    main()

