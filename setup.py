from setuptools import setup, find_namespace_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='S1_NRB',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    description="Prototype processor for the Sentinel-1 Normalised Radar Backscatter (S1 NRB) product",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/SAR-ARD/S1_NRB",
    author="John Truckenbrodt, Marco Wolsza",
    author_email="john.truckenbrodt@uni-jena.de",
    packages=find_namespace_packages(where='.'),
    include_package_data=True,
    install_requires=['gdal>=3.5.0',
                      'click',
                      'lxml',
                      'pystac',
                      'pyroSAR>=0.19.0',
                      'spatialist>=0.11.1',
                      'scipy',
                      's1etad>=0.5.3',
                      's1etad_tools>=0.8.1'],
    extras_require={
          'docs': ['sphinx', 'sphinxcontrib-bibtex', 'nbsphinx', 'sphinx_rtd_theme', 'sphinx-toolbox'],
    },
    python_requires='>=3.8',
    license='MIT',
    zip_safe=False,
    entry_points={
        'console_scripts': ['s1_nrb=S1_NRB.cli:cli']
    }
)
