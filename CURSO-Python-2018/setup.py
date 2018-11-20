# setup
# python setup.py sdist
# pip3 install nombredelpaquete.tgz
# pip3 uninstall nombredelpaquete.tgz

from setuptools import setup

setup(
	name='paquete_ejemplo',
	version='1.0',
	description='Esta es una versión de pruebas con un par de clases y funciones',
	author='David',
	author_email='dblancoformaciones@gmail.com',
	url='www.alpeformacion.es',
	packages=['paquetes'],
	)