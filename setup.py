from setuptools import setup, find_packages

setup(
    name='anfis',
    version='0.3.2',
    description='Custom Adaptive Neuro Fuzzy Inference System (ANFIS)',
    url='https://github.com/ClementNdome/anfis_custom',
    author='Clement Ndome Mwakavi',
    author_email='clementndome202@gmail.com',
    license='MIT',

    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.txt'],
    },

    keywords='anfis, fuzzy logic, neural networks, pytorch',

    install_requires=[
        'numpy',
        'matplotlib',
        'scikit-fuzzy',
        'torch',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
