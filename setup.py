from setuptools import setup

setup(name='recommender_ibmws',
      version='0.1',
      author= 'Joana Martins dos Santos'
      author_email= 'joanamlmsantos@gmail.com'
      description='Recommender System for IBM Watson Studio',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    Homepage = "https://github.com/joanamdsantos/recommender_ibmws_pkg"
    zip_safe=False)
