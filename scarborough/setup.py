from setuptools import setup

setup(
        name="scarborough",
        version="0.1",
        packages=['scarborough', 'scarborough.services', 'scarborough.utils', ],
        zip_safe=True,
        install_requires=['apscheduler>=3.0.5', "rx>=1.5.2", "cython"],
        author="bin.li",
        author_email="binli9106@163.com",
        url="http://example.com/"
    )
