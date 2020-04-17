import os
import uuid
import glob
from ase.io import read 
from goto import with_goto
from pymatgen import Structure,Molecule
from maptool.util.utils import sepline,wait_sep,wait
from pymatgen.io.ase import AseAtomsAdaptor

def ase2pmg(atoms):
    aaa=AseAtomsAdaptor()
    return  aaa.get_structure(atoms) 

def pmg2ase(structure):
    aaa=AseAtomsAdaptor()
    return aaa.get_atoms(structure)
 
@with_goto
def read_structures(cls=None):
    print('Input the structure filename')
    print('supported structure format: xsf .vasp POSCAR .nc .json .xyz ... ')
    print('paramter format, i.e. :')
    print('a.vasp')
    print('paramter format, i.e. :')
    print('a.vasp b.vasp')
    print('paramter format, i.e. :')
    print('*.cif')
    structs=[] 
    wait_sep()
    label .input
    in_str=wait()

    if in_str=="0":
        return None,None

    if '*' in in_str or '[' in in_str or '?' in in_str:
        fnames=glob.glob(in_str)
        if len(fnames)==0:
            print("Cannot match any files, check your input format")
            goto .input
    else:
        fnames=in_str.split()
        if not os.path.exists(fnames[0]):
            print("Cannot match any files, check your input format")
            goto .input
    #print(fnames)
    structures=read_structures_from_files(fnames)
    if len(structures)==0:
       print("Cannot parse file format, check the file concent")
       goto .input
    return structures

def read_structures_from_file(fname):
    #print(fname)
    try:
      atom=read(fname)
      return  ase2pmg(atoms)
    except:
       try:
           return Molecule.from_file(fname)
       except:
           try:
               return Structure.from_file(fname)
           except:
               print("Parsing error: %s"%fname)
               return None

def read_structures_from_files(fnames):
    structures=[]
    final_fnames=[]
    assert isinstance(fnames,list)
    for fname in fnames:
        structure=read_structures_from_file(fname)
        #print(structure)
        if structure is not None:
            structures.append(structure)
            final_fnames.append(fname)
    return structures,final_fnames

if __name__=='__main__':
  sts,fn=read_structures()
  print(sts,fn)
  for f, st in zip(fn,sts):
      print(f)
      print(st)