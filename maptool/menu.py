#!/usr/bin/env python
# coding: utf-8
from goto import with_goto
from maptool.util.utils import sepline,box_center,wait_sep,wait,your_choice
from maptool.submenu import select_function
from maptool.logo import logo
from maptool import NAME

try:
   from ._version import version as __version__
except ImportError:
   from .__about__ import __version__

def head():
    """show the logo and verion info 

    function description:

    Args:
        None

    Returns:
        None

    """
    box_center(ch='-',fill='-',sp="+")
    logo()
    box_center(ch='')
    box_center(__version__)
    box_center(ch='')
    box_center(ch='Written by Wang haidi')
    box_center(ch='URL  https://github.com/haidi-ustc')
    box_center(ch='Bug reports:(haidi@mail.ustc.edu.cn)')
    box_center(ch='-',fill='-',sp="+")

def tail():
    """show the citation info

    function description:

    Args:
        None

    Returns:
        None
    """

    box_center(ch='-',fill='-',sp="+")
    box_center(ch='*BYEBYE*')
    box_center(ch="Thanks for using "+NAME)
    box_center(ch="Have a nice day!!!")
    #box_center(ch="Please cite: Nanoscale 9 (2), 850-855")
    #box_center(ch="https://scholar.google.com/citations?hl=zh-CN&user=9PPScBEAAAAJ")
    box_center(ch='-',fill='-',sp="+")

def structural_operation():
    sepline(ch=" structural operation ",sp='=')
    print('{} >>> {}'.format('a1','random operation'))
    print('{} >>> {}'.format('a2','covert operation'))
    print('{} >>> {}'.format('a3','build operation'))
    print('{} >>> {}'.format('a4','cleave operation'))
    print('{} >>> {}'.format('a5','strain operation'))
    print('{} >>> {}'.format('a6','2D structure operation'))

def structural_analysis():
    sepline(ch=" structural analysis ",sp='=')
    print('{} >>> {}'.format('b1','structure symmetry'))
    print('{} >>> {}'.format('b2','structure finger print'))
    print('{} >>> {}'.format('b3','structure difference'))
    print('{} >>> {}'.format('b4','get primitive cell'))
    print('{} >>> {}'.format('b5','get conventional cell'))
    print('{} >>> {}'.format('b6','get XRD pattern'))

def vasp_inout():
    sepline(ch=" vasp in/out tools ",sp='=')
    print('{} >>> {}'.format('c1','prepare input files'))
    print('{} >>> {}'.format('c2','analysis output files'))
    print('{} >>> {}'.format('c3','summary output files'))

def vasp_workflow():
    sepline(ch=" vasp calclation workflow",sp='=')
    print('{} >>> {}'.format('d1','optimize structure'))
    print('{} >>> {}'.format('d2','calculate band structure'))
    print('{} >>> {}'.format('d3','calculate band structure HSE06'))
    print('{} >>> {}'.format('d4','calculate dos'))
    print('{} >>> {}'.format('d5','calculate dos by HSE06'))
    print('{} >>> {}'.format('d6','calculate elastic properties'))
    print('{} >>> {}'.format('d7','calculate phonon'))
    print('{} >>> {}'.format('d8','execute MD simulation'))

def MP_db():
    sepline(ch=" Materials Project database ",sp='=')
    print('{} >>> {}'.format('e1','get band/dos by mp-ID'))
    print('{} >>> {}'.format('e2','get structure from materialsproject database'))
    print('{} >>> {}'.format('e3','get properties by mp-ID'))
    print('{} >>> {}'.format('e4','get phase graph'))

def local_db():
    sepline(ch=" local database ",sp='=')
    print('{} >>> {}'.format('f1','check local database'))
    print('{} >>> {}'.format('f2','get entry by l-ID'))
    print('{} >>> {}'.format('f3','get entry by formula'))
    print('{} >>> {}'.format('f4','get entry by element'))
    print('{} >>> {}'.format('f5','insert entry into database'))

@with_goto
def menu():
    """show the first class menu

    function description:

    Args:
        None

    Returns:
        None
    """

    label .input
    structural_operation()
    structural_analysis()
    vasp_inout()
    vasp_workflow()
    MP_db()
    local_db()
    sepline(ch="=",sp='=')
    print("")
    print("")
    your_choice()
    in_str=wait()
    ret=select_function(in_str) 
    if ret is None:
        goto .input

#TODO
#    sepline(ch=" siesta tools ",sp='=')
#    print('{} >>> {}'.format('si1','prepare input files'))
#    sepline(ch=" gaussian tools ",sp='=')
#    print('{} >>> {}'.format('gi1','prepare input files'))
#    sepline(ch=" nwchem tools ",sp='=')
#    print('{} >>> {}'.format('ni1','prepare input files'))
#    sepline(ch=" quantum espresso tools ",sp='=')
#    print('{} >>> {}'.format('qi1','prepare input files'))
#    sepline(ch=" lammps tools ",sp='=')
#    print('{} >>> {}'.format('li1','prepare input files'))


if __name__=='__main__':
    head()
    menu()
    tail()
